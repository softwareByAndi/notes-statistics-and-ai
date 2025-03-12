import os
import re
import sys
from pathlib import Path

class ObsidianCompiler:
    def __init__(self, head_file_path, output_file="compiled_course.md"):
        # Store the head file path directly
        self.head_file_path = Path(head_file_path)
        # Determine the vault path from the head file
        self.vault_path = self.find_vault_root(self.head_file_path)
        self.output_file = output_file
        self.visited_files = set()  # Track files we've already processed
        self.compiled_content = ""  # Store the compiled content as a single string
        self.link_pattern = re.compile(r'\[\[(.*?)\]\]')  # Pattern to find Obsidian links
        
        # Track current header level context
        self.current_level = 0

    def find_vault_root(self, file_path):
        """Try to determine the vault root from the head file path"""
        # For now, we'll use the parent directory of the parent directory
        return file_path.parent.parent
    
    def compile_vault(self):
        """Start the compilation process from the head file"""
        print(f"Starting compilation from {self.head_file_path}")
        
        if not self.head_file_path.exists():
            print(f"Error: Head file not found at {self.head_file_path}")
            return False
        
        # Process the head file first
        processed_content = self.process_file(self.head_file_path)
        self.compiled_content = processed_content
        
        # Write the compiled content to the output file
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(self.compiled_content)
        
        print(f"Compilation complete! Output written to {self.output_file}")
        return True
    
    def process_file(self, file_path, parent_level=0):
        """Process a Markdown file and replace any links with the file contents"""
        # Convert to Path object if it's not already
        file_path = Path(file_path)
        
        # Skip if we've already processed this file
        if str(file_path) in self.visited_files:
            return ""
        
        # Mark as visited
        self.visited_files.add(str(file_path))
        print(f"Processing: {file_path}")
        
        try:
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if the file starts with a header, if not, add one
            content = self.ensure_has_header(content, file_path)
            
            # Adjust header levels based on parent level
            content = self.adjust_header_levels(content, parent_level)
            
            # Process links and replace them with file contents
            # We use a while loop because the pattern of links might change after each replacement
            while True:
                match = self.link_pattern.search(content)
                if not match:
                    break
                
                # Get the link text
                link_text = match.group(1)
                original_link = match.group(0)  # The full [[link]] text
                
                # Remove any #section or |alias parts from the link
                if '#' in link_text:
                    link_text = link_text.split('#')[0]
                if '|' in link_text:
                    link_text = link_text.split('|')[0]
                
                # Find the linked file
                linked_file = self.find_file(link_text.strip())
                
                if linked_file and str(linked_file) not in self.visited_files:
                    # Find the current max header level up to the link position
                    max_level = self.find_max_header_level_up_to(content, match.start())
                    
                    # Process the linked file
                    linked_content = self.process_file(linked_file, parent_level=max_level)
                    
                    # Replace the link with the content
                    content = content.replace(original_link, linked_content, 1)
                else:
                    # If file not found or already visited, just remove the link brackets
                    clean_text = link_text
                    if '|' in link_text:
                        clean_text = link_text.split('|')[1]  # Use the alias if present
                    content = content.replace(original_link, clean_text, 1)
            
            return content
            
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            return f"[Error processing {file_path}: {e}]"
    
    def ensure_has_header(self, content, file_path):
        """Ensure the content starts with a header, using filename if needed"""
        # Check if content starts with a header
        header_pattern = re.compile(r'^#+\s+.*$', re.MULTILINE)
        has_header = header_pattern.match(content.lstrip())
        
        if not has_header:
            # Get the file name without extension
            file_name = file_path.stem
            
            # If the filename starts with an underscore, remove it
            if file_name.startswith('_'):
                file_name = file_name[1:]
                
            # Add a header to the beginning of the content
            content = f"# {file_name}\n\n{content}"
            print(f"Added header '{file_name}' to file without header")
        
        return content
    
    def find_file(self, link_text):
        """Find a file in the vault based on its link text"""
        # Case 1: If link is a full path
        if '/' in link_text:
            # Try direct path resolution
            full_path = self.vault_path / f"{link_text}.md"
            if full_path.exists():
                return full_path
        
        # Case 2: If link is just a filename (exact match search)
        else:
            # Search for exact filename match across the vault
            matches = list(self.vault_path.glob(f"**/{link_text}.md"))
            if matches:
                return matches[0]  # Return the first match if multiple are found
            
            # Also check if the file exists in the same directory as the current file
            current_dir = self.head_file_path.parent
            possible_file = current_dir / f"{link_text}.md"
            if possible_file.exists():
                return possible_file
        
        # If we can't find the file, print a warning
        print(f"Warning: Could not find file for link '{link_text}'")
        return None

    def adjust_header_levels(self, content, parent_level):
        """Adjust header levels in content based on parent level"""
        lines = content.split('\n')
        adjusted_lines = []
        
        # Get the current minimum header level in this content
        header_pattern = re.compile(r'^(#+)\s')
        header_levels = []
        
        for line in lines:
            match = header_pattern.match(line)
            if match:
                level = len(match.group(1))
                header_levels.append(level)
        
        # Determine how to adjust headers
        min_level = min(header_levels) if header_levels else 0
        level_adjustment = max(0, parent_level + 1 - min_level)
        
        # Now adjust each line
        for line in lines:
            match = header_pattern.match(line)
            if match:
                # Get current header level
                current_hashes = match.group(1)
                current_level = len(current_hashes)
                
                # Calculate new level
                new_level = current_level + level_adjustment
                
                # Replace header with adjusted level
                new_header = '#' * new_level
                line = line.replace(current_hashes, new_header, 1)
                
            adjusted_lines.append(line)
        
        return '\n'.join(adjusted_lines)
    
    def find_max_header_level(self, content):
        """Find the maximum header level in the content"""
        max_level = 0
        header_pattern = re.compile(r'^(#+)\s', re.MULTILINE)
        
        for match in header_pattern.finditer(content):
            level = len(match.group(1))
            max_level = max(max_level, level)
        
        return max_level
    
    def find_max_header_level_up_to(self, content, position):
        """Find the maximum header level in content up to a specific position"""
        max_level = 0
        header_pattern = re.compile(r'^(#+)\s', re.MULTILINE)
        
        for match in header_pattern.finditer(content[:position]):
            level = len(match.group(1))
            max_level = max(max_level, level)
        
        return max_level

def main():
    if len(sys.argv) < 2:
        print("Usage: python compile_obsidian.py <path_to_head_file> [output_file]")
        return
    
    head_file_path = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "compiled_course.md"
    
    compiler = ObsidianCompiler(head_file_path, output_file)
    compiler.compile_vault()

if __name__ == "__main__":
    main()
    
"""
python compile_obsidian.py /path/to/llm/outline/_outline.md compiled_course.md

python compile_obsidian.py llm/outline/_outline.md llm/CURRENT_OUTLINE.md
"""