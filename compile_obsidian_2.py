import os
import re
import sys
import uuid
import logging
from pathlib import Path
from collections import defaultdict, deque

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger('obsidian_compiler')

class ObsidianCompiler:
    def __init__(self, head_file_path, output_file="compiled_document.md", verbose=False):
        """Initialize the Obsidian compiler with the head file and output destination.
        
        Args:
            head_file_path (str): Path to the starting document
            output_file (str): Path where the compiled document will be saved
            verbose (bool): Whether to print detailed progress messages
        """
        # Basic setup
        self.head_file_path = Path(head_file_path).resolve()
        self.output_file = output_file
        self.verbose = verbose
        
        if self.verbose:
            logger.setLevel(logging.DEBUG)
        
        # Collections for document processing
        self.documents = {}  # path -> document entity
        self.sections = {}   # id -> section entity
        self.link_map = {}   # link text -> document path
        self.sections_to_include = set()  # sections referenced in lists but not rendered inline
        
        # Track rendered sections to prevent circular references
        self.rendering_in_progress = set()
        
        # Find vault root (directory containing .obsidian folder)
        self.vault_path = self.find_vault_root()
        logger.info(f"Vault root detected at {self.vault_path}")
        
        # Compile regex patterns for better performance
        self.link_pattern = re.compile(r'\[\[(.*?)\]\]')
        self.header_pattern = re.compile(r'^(#+)\s+(.*?)$', re.MULTILINE)
        self.list_item_pattern = re.compile(r'^(\s*)[-*+]\s+(.*?)$', re.MULTILINE)
        self.frontmatter_pattern = re.compile(r'^---\n.*?\n---\n', re.DOTALL)
        
    def find_vault_root(self):
        """Find the Obsidian vault root by looking for .obsidian folder"""
        current_path = self.head_file_path.parent
        
        # Navigate up until we find .obsidian folder or reach filesystem root
        while not (current_path / ".obsidian").exists():
            if current_path == current_path.parent:  # We've reached the root
                logger.warning(f"Could not find .obsidian folder. Using {self.head_file_path.parent} as vault root.")
                return self.head_file_path.parent
            current_path = current_path.parent
            
        return current_path
    
    def compile_document(self):
        """Main method to compile the document through the various processing phases"""
        logger.info(f"Starting compilation from {self.head_file_path}")
        
        if not self.head_file_path.exists():
            logger.error(f"Error: Head file not found at {self.head_file_path}")
            return False
        
        try:
            # Phase 1: Parse all documents
            logger.info("Phase 1: Parsing documents...")
            self.parse_document(self.head_file_path)
            logger.info(f"Parsed {len(self.documents)} documents")
            
            # Phase 2: Resolve all links between documents
            logger.info("Phase 2: Resolving document links...")
            self.resolve_links()
            logger.info(f"Resolved {len(self.link_map)} link entries")
            
            # Phase 3: Extract sections from all documents
            logger.info("Phase 3: Extracting document sections...")
            self.extract_sections()
            logger.info(f"Extracted {len(self.sections)} sections")
            
            # Phase 4: Assemble the final document
            logger.info("Phase 4: Assembling final document...")
            content = self.assemble_document()
            
            # Write output
            with open(self.output_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            logger.info(f"Compilation complete! Output written to {self.output_file}")
            return True
            
        except Exception as e:
            logger.error(f"Error during compilation: {str(e)}", exc_info=True)
            return False
    
    def parse_document(self, file_path, already_visited=None):
        """Parse a single document into a document entity.
        
        Args:
            file_path (Path): Path to the document to parse
            already_visited (set): Set of already visited paths to prevent circular references
        """
        if already_visited is None:
            already_visited = set()
            
        file_path = Path(file_path).resolve()
        str_path = str(file_path)
        
        # Skip if already processed
        if str_path in self.documents:
            return
            
        # Prevent circular references
        if str_path in already_visited:
            logger.warning(f"Circular reference detected for {file_path}")
            return
            
        already_visited.add(str_path)
        
        try:
            # Check if file exists
            if not file_path.exists():
                logger.warning(f"File not found: {file_path}")
                return
                
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Strip frontmatter and extract title
            clean_content = self.strip_frontmatter(content)
            title = self.extract_title(clean_content, file_path)
            
            # Create document entity
            document = {
                'path': str_path,
                'filename': file_path.stem,
                'title': title,
                'content': clean_content,
                'sections': [],
                'links': []
            }
            
            # Store document
            self.documents[str_path] = document
            
            # Find links and parse linked documents
            links = self.find_links(clean_content)
            document['links'] = links
            
            # Process linked documents recursively
            for link in links:
                linked_file = self.find_file(link)
                if linked_file:
                    self.parse_document(linked_file, already_visited.copy())
        
        except Exception as e:
            logger.error(f"Error parsing document {file_path}: {str(e)}")
    
    def strip_frontmatter(self, content):
        """Remove YAML frontmatter from content"""
        return self.frontmatter_pattern.sub('', content)
    
    def extract_title(self, content, file_path):
        """Extract title from first header or use filename"""
        # Check for first header
        match = self.header_pattern.search(content)
        if match:
            return match.group(2)
        
        # Use filename as title if no header
        title = file_path.stem
        # Remove leading underscore if present (common in Obsidian for index files)
        if title.startswith('_'):
            title = title[1:]
        return title
    
    def find_links(self, content):
        """Find all Obsidian links in content and normalize them"""
        links = []
        for match in self.link_pattern.finditer(content):
            link_text = match.group(1)
            
            # Clean up link text (remove aliases and sections)
            if '|' in link_text:
                link_text = link_text.split('|', 1)[0]
            if '#' in link_text:
                link_text = link_text.split('#', 1)[0]
                
            links.append(link_text.strip())
        
        return links
    
    def find_file(self, link_text):
        """Find a file based on link text, handling various link formats"""
        link_text = link_text.strip()
        
        # Try as a relative path first
        if '/' in link_text:
            # This is a path-like link
            full_path = self.vault_path / f"{link_text}.md"
            if full_path.exists():
                return full_path
        
        # Try to find by exact filename match
        # First check in current directory
        current_dir = self.head_file_path.parent
        current_file = current_dir / f"{link_text}.md"
        if current_file.exists():
            return current_file
            
        # Then search the whole vault, handling spaces and special characters
        possible_matches = []
        for file_path in self.vault_path.rglob("*.md"):
            if file_path.stem == link_text or file_path.stem.lower() == link_text.lower():
                possible_matches.append(file_path)
        
        if possible_matches:
            return possible_matches[0]  # Return the first match
            
        logger.warning(f"Could not find file for link '{link_text}'")
        return None
    
    def resolve_links(self):
        """Build mapping from link text to document path for quick lookups"""
        for path, doc in self.documents.items():
            # Register this document with its filename as key
            self.link_map[doc['filename']] = path
            
            # Also register with title (useful for "pretty" links)
            if doc['title'] and doc['title'] != doc['filename']:
                self.link_map[doc['title']] = path
            
            # Register path variations for robustness
            rel_path = str(Path(path).relative_to(self.vault_path))
            if rel_path.endswith('.md'):
                rel_path = rel_path[:-3]  # Remove .md extension
            self.link_map[rel_path] = path
    
    def extract_sections(self):
        """Extract sections from all documents, building the section hierarchy"""
        # Process documents in a consistent order (important for reproducibility)
        ordered_documents = sorted(self.documents.items(), key=lambda x: x[0])
        
        for path, doc in ordered_documents:
            # Create the root section for this document
            section_id = str(uuid.uuid4())
            root_section = {
                'id': section_id,
                'title': doc['title'] or doc['filename'],  # Fallback to filename if no title
                'level': 0,  # Root level
                'content': '',
                'children': [],
                'document': path,
                'parent': None,
                'order_id': len(self.sections)  # Global section ordering
            }
            
            # Store this section
            self.sections[section_id] = root_section
            
            # Link document to its root section
            doc['root_section'] = section_id
            
            # Parse the content into a section tree
            content = doc['content']
            
            # Remove existing anchor tags before parsing
            content = re.sub(r'<a id="[^"]+"></a>\s*', '', content)
            
            self.parse_sections(content, root_section)
    
    def parse_sections(self, content, parent_section):
        """Parse content into a hierarchy of sections using a stack-based approach
        
        Args:
            content (str): Document content to parse
            parent_section (dict): Parent section to attach parsed sections
        """
        lines = content.split('\n')
        sections_stack = [parent_section]  # Stack to track section hierarchy
        content_buffer = []
        
        # Track the order of sections with a global counter
        section_counter = 0
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check if this is a header
            header_match = self.header_pattern.match(line)
            if header_match:
                # Found a header, create a new section
                level = len(header_match.group(1))
                title = header_match.group(2)
                
                # If we were building content for a section, save it
                if content_buffer:
                    sections_stack[-1]['content'] = '\n'.join(content_buffer)
                    content_buffer = []
                
                # Find the appropriate parent for this level by popping the stack
                # until we find a section with a lower level
                while len(sections_stack) > 1 and sections_stack[-1]['level'] >= level:
                    sections_stack.pop()
                
                # Create the new section
                section_id = str(uuid.uuid4())
                new_section = {
                    'id': section_id,
                    'title': title,
                    'level': level,
                    'content': '',
                    'children': [],
                    'document': parent_section['document'],
                    'parent': sections_stack[-1]['id'],
                    'order': section_counter  # Local order within document
                }
                section_counter += 1
                
                # Store this section
                self.sections[section_id] = new_section
                
                # Add to parent's children
                sections_stack[-1]['children'].append(section_id)
                
                # Push the new section onto the stack
                sections_stack.append(new_section)
            else:
                # Regular content, add to buffer
                content_buffer.append(line)
            
            i += 1
        
        # Save any remaining content to the last section
        if content_buffer:
            sections_stack[-1]['content'] = '\n'.join(content_buffer)
    
    def assemble_document(self):
        """Assemble the final document from sections, handling appendix for list links"""
        # Start with the head document's root section
        head_doc = self.documents[str(self.head_file_path)]
        root_section_id = head_doc['root_section']
        
        # Keep track of all rendered sections
        rendered_sections = set()
        
        # Process the content recursively
        result = self.render_section(root_section_id, 1, rendered_sections)
        
        # Check if we need to add an appendix for section references
        appendix_sections = list(self.sections_to_include - rendered_sections)
        
        if appendix_sections:
            # Sort appendix sections by document order
            appendix_sections.sort(key=lambda section_id: (
                self.sections[section_id]['document'],
                self.sections[section_id].get('order', 0)
            ))
            
            result += "\n\n## Appendix\n\n"
            for section_id in appendix_sections:
                section_content = self.render_section(section_id, 2, rendered_sections)
                result += section_content
                result += "\n\n"
        
        # Post-processing - remove any existing anchor tags that might conflict with our new ones
        result = re.sub(r'<a id="[^"]+"></a>\s*\n<a id="[^"]+"></a>', 
                        lambda m: m.group(0).split('\n')[0], result)
        
        return result
    
    def render_section(self, section_id, level, rendered_sections):
        """Render a section with proper header level
        
        Args:
            section_id (str): ID of the section to render
            level (int): Header level to use for this section
            rendered_sections (set): Set of already rendered sections
            
        Returns:
            str: Rendered section content with proper header formatting
        """
        # Check if we've already rendered this section
        if section_id in rendered_sections:
            # Already rendered this section, just create a link to it
            section = self.sections[section_id]
            return f"[{section['title']}](#{self.create_anchor_id(section)})"
        
        # Check for circular references during rendering
        if section_id in self.rendering_in_progress:
            # We have a circular reference
            section = self.sections[section_id]
            logger.warning(f"Circular reference detected for section '{section['title']}'")
            return f"[{section['title']}](#{self.create_anchor_id(section)})"
        
        # Mark as rendering in progress
        self.rendering_in_progress.add(section_id)
        
        # Get the section and mark it as rendered
        section = self.sections[section_id]
        rendered_sections.add(section_id)
        
        # Determine the appropriate header level
        actual_level = max(1, level)  # Ensure minimum level of 1
        
        # Create header with proper level
        header = '#' * actual_level + ' ' + section['title']
        
        # Create anchor for this section
        anchor = f'<a id="{self.create_anchor_id(section)}"></a>'
        
        # Process content to replace links
        content = self.process_links_in_content(section['content'], actual_level, rendered_sections)
        
        # Start with the anchor and header
        parts = []
        parts.append(anchor)
        parts.append(header)
        
        # Add content if it exists
        if content.strip():
            parts.append(content)
        
        # Join the parts
        result = '\n\n'.join(parts)
        
        # Process child sections IN ORDER
        for child_id in sorted(section['children'], 
                              key=lambda sid: self.sections[sid].get('order', 0)):
            child_content = self.render_section(child_id, actual_level + 1, rendered_sections)
            if child_content:
                result += '\n\n' + child_content
        
        # We're done rendering this section
        self.rendering_in_progress.remove(section_id)
        
        return result
    
    def process_links_in_content(self, content, level, rendered_sections):
        """Process Obsidian links in content, either expanding them inline or creating references
        
        Args:
            content (str): Content to process
            level (int): Current header level
            rendered_sections (set): Set of already rendered sections
            
        Returns:
            str: Content with processed links
        """
        # First pass: identify any list items with links to avoid inline expansion
        list_item_links = set()
        
        def identify_list_links(match):
            link_text = match.group(1)
            if self.is_in_list_item(content, match.start()):
                # Just record this is in a list item
                if '|' in link_text:
                    link_text = link_text.split('|', 1)[0]
                if '#' in link_text:
                    link_text = link_text.split('#', 1)[0]
                list_item_links.add(link_text.strip())
            return match.group(0)  # Return unchanged
            
        # First identify list links
        self.link_pattern.sub(identify_list_links, content)
        
        # Second pass: process all links
        def replace_link(match):
            link_text = match.group(1)
            display_text = link_text
            
            # Handle aliases
            if '|' in link_text:
                link_text, display_text = link_text.split('|', 1)
            
            # Handle section references
            section_reference = None
            if '#' in link_text:
                link_parts = link_text.split('#', 1)
                link_text = link_parts[0]
                if len(link_parts) > 1 and link_parts[1]:
                    section_reference = link_parts[1]
            
            # Find the linked document
            link_text = link_text.strip()
            if link_text in self.link_map:
                doc_path = self.link_map[link_text]
                doc = self.documents[doc_path]
                section_id = doc['root_section']
                
                # Check if this link is in a list item (identified in first pass)
                is_list_item = link_text in list_item_links
                
                if is_list_item:
                    # For list items, add to sections_to_include but don't expand inline
                    self.sections_to_include.add(section_id)
                    section = self.sections[section_id]
                    return f"[{display_text}](#{self.create_anchor_id(section)})"
                else:
                    # For inline links, check if already rendered
                    if section_id in rendered_sections:
                        section = self.sections[section_id]
                        return f"[{display_text}](#{self.create_anchor_id(section)})"
                    else:
                        # Check for circular references
                        if section_id in self.rendering_in_progress:
                            section = self.sections[section_id]
                            logger.warning(f"Circular reference detected for section '{section['title']}'")
                            return f"[{display_text}](#{self.create_anchor_id(section)})"
                        
                        # Mark as rendered first to prevent duplicate rendering
                        rendered_sections.add(section_id)
                        
                        # Inline expansion - render the section here
                        return self.render_section(section_id, level, rendered_sections)
            
            # If we can't resolve the link, just return the display text
            return display_text
        
        # Replace all links
        return self.link_pattern.sub(replace_link, content)
    
    def is_in_list_item(self, content, position):
        """Check if a position in content is within a list item
        
        Args:
            content (str): The content to check
            position (int): Position in the content to check
            
        Returns:
            bool: True if position is within a list item
        """
        # Find the start of the line containing this position
        line_start = content.rfind('\n', 0, position) + 1
        if line_start < 0:  # If no newline found before position
            line_start = 0
            
        line_end = content.find('\n', position)
        if line_end == -1:  # If no newline found after position
            line_end = len(content)
        
        line = content[line_start:line_end]
        return bool(self.list_item_pattern.match(line))
    
    def create_anchor_id(self, section):
        """Create a unique anchor ID for a section
        
        Args:
            section (dict): Section to create anchor for
            
        Returns:
            str: Unique anchor ID
        """
        # Use title to create a slug - simplify for readability
        title = section['title']
        slug = re.sub(r'[^\w-]', '-', title.lower())
        slug = re.sub(r'-+', '-', slug)  # Replace multiple dashes with single dash
        slug = slug.strip('-')  # Remove leading/trailing dashes
        
        # Check if this document already has this slug
        doc_path = section['document']
        doc = self.documents[doc_path]
        filename = doc['filename']
        if filename.startswith('_'):
            filename = filename[1:]
            
        # Create a simpler anchor format that's more predictable
        return f"{slug}-{section['id'][:8]}"


def main():
    """Main entry point for the script."""
    if len(sys.argv) < 2:
        print("Usage: python obsidian_compiler.py <path_to_head_file> [output_file] [--verbose]")
        return
    
    head_file_path = sys.argv[1]
    
    # Parse optional arguments
    output_file = "compiled_document.md"
    verbose = False
    
    for arg in sys.argv[2:]:
        if arg == "--verbose":
            verbose = True
        elif not arg.startswith("--"):
            output_file = arg
    
    # Create and run the compiler
    compiler = ObsidianCompiler(head_file_path, output_file, verbose)
    success = compiler.compile_document()
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()