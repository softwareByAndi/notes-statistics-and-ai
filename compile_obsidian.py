import os
import re
import sys
from pathlib import Path
import string

class ObsidianCompiler:
    def __init__(self, head_file_path, output_file="compiled_course.md"):
        self.head_file_path = Path(head_file_path).resolve()
        self.output_file = output_file
        
        # Find vault root - go up until we find a .obsidian folder or use parent dir
        vault_path = self.head_file_path.parent
        while not (vault_path / ".obsidian").exists() and vault_path != vault_path.parent:
            vault_path = vault_path.parent
        self.vault_path = vault_path
        
        # Track processed files and references
        self.processed_files = {}  # Maps file path to its processed content
        self.file_references = {}  # Counts references to each file
        self.linked_content = []   # Content to append at the end
        
        # Regular expression patterns
        self.link_pattern = re.compile(r'\[\[(.*?)\]\]')
        self.header_pattern = re.compile(r'^(#+)\s+(.*?)$', re.MULTILINE)
        
    def compile_document(self):
        """Main method to compile the document"""
        print(f"Starting compilation from {self.head_file_path}")
        print(f"Vault root detected at {self.vault_path}")
        
        if not self.head_file_path.exists():
            print(f"Error: Head file not found at {self.head_file_path}")
            return False
        
        # First pass: Process the main document and collect links
        main_content = self.process_main_document(self.head_file_path)
        
        # Combine main content with linked content
        full_content = main_content
        if self.linked_content:
            full_content += "\n\n## Linked Content\n\n"
            full_content += "\n\n".join(self.linked_content)
        
        # Write output
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"Compilation complete! Output written to {self.output_file}")
        print(f"Processed {len(self.processed_files)} unique files")
        return True
    
    def process_main_document(self, file_path):
        """Process the main document and prepare linked content"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove frontmatter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            
            # Ensure file has a header
            content = self.ensure_header(content, file_path)
            
            # Replace links with anchors and collect linked content
            content = self.replace_links_with_anchors(content)
            
            return content
            
        except Exception as e:
            print(f"Error processing main document {file_path}: {str(e)}")
            return f"[Error processing main document: {str(e)}]"
    
    def replace_links_with_anchors(self, content):
        """Replace Obsidian links with Markdown links to anchors"""
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
            
            # Create a unique anchor ID for this reference
            anchor_id = self.create_anchor_id(linked_file)
            
            # Process the linked file content if not already processed
            if str(linked_file) not in self.processed_files:
                linked_content = self.process_linked_file(linked_file)
                self.linked_content.append(linked_content)
                self.processed_files[str(linked_file)] = linked_content
            
            # Return a markdown link to the anchor
            return f"[{display_text}](#{anchor_id})"
        
        # Replace all links
        return self.link_pattern.sub(replace_link, content)
    
    def process_linked_file(self, file_path):
        """Process a linked file and prepare it for appending"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Remove frontmatter
            content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
            
            # Ensure file has a header
            content = self.ensure_header(content, file_path)
            
            # Create anchor for this content
            anchor_id = self.create_anchor_id(file_path)
            anchor_tag = f'<a id="{anchor_id}"></a>'
            
            # Process links in this file recursively
            content = self.replace_links_with_anchors(content)
            
            # Add the anchor tag before the content
            return f"{anchor_tag}\n{content}"
            
        except Exception as e:
            print(f"Error processing linked file {file_path}: {str(e)}")
            return f"<a id=\"{self.create_anchor_id(file_path)}\"></a>\n[Error processing {file_path.name}: {str(e)}]"
    
    def create_anchor_id(self, file_path):
        """Create a unique anchor ID for a file reference"""
        # Get the file name without extension
        file_name = file_path.stem
        if file_name.startswith('_'):
            file_name = file_name[1:]
        
        # Convert to a valid ID (lowercase, no spaces or special chars)
        anchor_base = re.sub(r'[^\w-]', '-', file_name.lower())
        
        # Count references to this file
        str_path = str(file_path)
        if str_path in self.file_references:
            self.file_references[str_path] += 1
            return f"{anchor_base}-{self.file_references[str_path]}"
        else:
            self.file_references[str_path] = 1
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