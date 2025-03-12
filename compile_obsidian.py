import os
import re
import sys
from pathlib import Path
from collections import defaultdict

class ObsidianCompiler:
    def __init__(self, head_file_path, output_file="compiled_course.md"):
        self.head_file_path = Path(head_file_path).resolve()
        self.output_file = output_file
        
        # Find vault root - go up until we find a .obsidian folder or use parent dir
        vault_path = self.head_file_path.parent
        while not (vault_path / ".obsidian").exists() and vault_path != vault_path.parent:
            vault_path = vault_path.parent
        self.vault_path = vault_path
        
        # Track file references and processed content
        self.file_references = defaultdict(int)  # Counts references to each file
        self.processed_files = {}  # Cached processed content
        
        # Regular expression patterns
        self.link_pattern = re.compile(r'\[\[(.*?)\]\]')
        self.header_pattern = re.compile(r'^(#+)\s+(.*?)$', re.MULTILINE)
        
        print(f"Vault root detected at {self.vault_path}")
    
    def compile_document(self):
        """Main method to compile the document"""
        print(f"Starting compilation from {self.head_file_path}")
        
        if not self.head_file_path.exists():
            print(f"Error: Head file not found at {self.head_file_path}")
            return False
        
        # First pass: Process main document and build structure
        main_content, all_files = self.process_main_file(self.head_file_path)
        
        # Second pass: Process all linked files and build complete document
        final_content = main_content
        
        # Add the linked content after the main content
        if all_files:
            final_content += "\n\n"
            for file_path, parent_level in all_files:
                if str(file_path) not in self.processed_files:
                    linked_content = self.process_linked_file(file_path, parent_level)
                    self.processed_files[str(file_path)] = linked_content
                    final_content += linked_content + "\n\n"
        
        # Write output
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"Compilation complete! Output written to {self.output_file}")
        print(f"Processed {len(self.processed_files)} unique files")
        return True
    
    def process_main_file(self, file_path):
        """Process the main file and collect all linked files"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove frontmatter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            
            # Ensure file has a header
            content = self.ensure_header(content, file_path)
            
            # Process the content and collect all linked files
            linked_files = []
            content = self.replace_links_with_anchors(content, 0, linked_files)
            
            # Return the processed content and the list of linked files
            return content, linked_files
            
        except Exception as e:
            print(f"Error processing main file {file_path}: {str(e)}")
            return f"[Error processing main file: {str(e)}]", []
    
    def process_linked_file(self, file_path, parent_level):
        """Process a linked file, adjusting headers based on parent level"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove frontmatter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            
            # Ensure file has a header
            content = self.ensure_header(content, file_path)
            
            # Create anchor for this file
            anchor_id = self.create_anchor_id(file_path)
            anchor_tag = f'<a id="{anchor_id}"></a>'
            
            # Adjust headers based on parent level
            content = self.adjust_headers(content, parent_level)
            
            # Process links in this content
            linked_files = []  # We'll track further links within this file
            content = self.replace_links_with_anchors(content, parent_level, linked_files)
            
            # Add the anchor tag before the content
            result = f"{anchor_tag}\n{content}"
            
            # Process nested links
            for nested_file, nested_level in linked_files:
                if str(nested_file) not in self.processed_files:
                    nested_content = self.process_linked_file(nested_file, nested_level)
                    self.processed_files[str(nested_file)] = nested_content
                    result += "\n\n" + nested_content
            
            return result
            
        except Exception as e:
            print(f"Error processing linked file {file_path}: {str(e)}")
            return f"<a id=\"{self.create_anchor_id(file_path)}\"></a>\n[Error processing {file_path.name}: {str(e)}]"
    
    def replace_links_with_anchors(self, content, parent_level, linked_files):
        """Replace Obsidian links with Markdown links and track linked files"""
        def replace_link(match):
            link_text = match.group(1)
            display_text = link_text
            
            # Handle aliases
            if '|' in link_text:
                link_text, display_text = link_text.split('|', 1)
            
            # Remove section references
            if '#' in link_text:
                link_text = link_text.split('#', 1)[0]
            
            # Find the linked file
            linked_file = self.find_file(link_text.strip())
            if not linked_file:
                # If file not found, just remove the brackets
                return display_text
            
            # Determine the header level for this link
            # Find the current header level up to this point
            prev_text = content[:match.start()]
            current_level = self.find_highest_header_level(prev_text) or parent_level
            next_level = current_level + 1
            
            # Track this file for processing later
            linked_files.append((linked_file, next_level))
            
            # Create a unique anchor ID for this reference
            self.file_references[str(linked_file)] += 1
            anchor_id = self.create_anchor_id(linked_file)
            
            # Return a markdown link to the anchor
            return f"[{display_text}](#{anchor_id})"
        
        # Replace all links
        return self.link_pattern.sub(replace_link, content)
    
    def create_anchor_id(self, file_path):
        """Create a unique anchor ID for a file reference"""
        # Get the file name without extension
        file_name = file_path.stem
        if file_name.startswith('_'):
            file_name = file_name[1:]
        
        # Convert to a valid ID (lowercase, no spaces or special chars)
        anchor_base = re.sub(r'[^\w-]', '-', file_name.lower())
        
        # Only add index for repeated references (2+)
        ref_count = self.file_references[str(file_path)]
        if ref_count > 1:
            return f"{anchor_base}-{ref_count}"
        else:
            return anchor_base
    
    def ensure_header(self, content, file_path):
        """Ensure the content has a header, adding one if needed"""
        # Check if content has a header
        if not self.header_pattern.search(content.lstrip()):
            # Get file name (without extension and leading underscore)
            file_name = file_path.stem
            if file_name.startswith('_'):
                file_name = file_name[1:]
            
            # Add a header at the beginning
            content = f"# {file_name}\n\n{content}"
        
        return content
    
    def adjust_headers(self, content, parent_level):
        """Adjust header levels based on parent context"""
        if parent_level == 0:
            return content  # No adjustment needed for top-level document
            
        lines = content.split('\n')
        result = []
        
        # Find minimum header level in content
        min_level = 6  # Start with maximum possible header level
        for line in lines:
            match = self.header_pattern.match(line)
            if match:
                level = len(match.group(1))
                min_level = min(min_level, level)
        
        if min_level == 6:  # No headers found
            return content
            
        # Calculate adjustment needed
        adjustment = parent_level + 1 - min_level  # Want top header to be parent_level + 1
        
        # Adjust headers
        for line in lines:
            match = self.header_pattern.match(line)
            if match:
                level = len(match.group(1))
                new_level = level + adjustment
                new_header = '#' * new_level
                line = line.replace(match.group(1), new_header, 1)
            result.append(line)
            
        return '\n'.join(result)
    
    def find_highest_header_level(self, content):
        """Find the highest (numerically smallest) header level in content"""
        min_level = 6  # Start with maximum possible
        for match in self.header_pattern.finditer(content):
            level = len(match.group(1))
            min_level = min(min_level, level)
        return min_level if min_level < 6 else 0
    
    def find_file(self, link_text):
        """Find a file based on link text"""
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
            
        # Then search the whole vault
        matches = list(self.vault_path.rglob(f"{link_text}.md"))
        if matches:
            return matches[0]  # Return the first match
            
        # If we get here, file wasn't found
        print(f"Warning: Could not find file for link '{link_text}'")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python compile_obsidian.py <path_to_head_file> [output_file]")
        return
    
    head_file_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "compiled_course.md"
    
    compiler = ObsidianCompiler(head_file_path, output_file)
    compiler.compile_document()

if __name__ == "__main__":
    main()

"""
python compile_obsidian.py /path/to/llm/outline/_outline.md compiled_course.md

python compile_obsidian.py llm/outline/_outline.md llm/CURRENT_OUTLINE.md
"""