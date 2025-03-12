import os
import re
import json

def build_file_dict(directory):
   file_dict = {}
   
   for root, dirs, files in os.walk(directory):
       for file in files:
           full_path = os.path.join(root, file).replace('./', '')
           
           # For .md files, use name without extension as key
           if file.endswith('.md'):
               key = os.path.splitext(file)[0]
           else:
               key = file
               
           # If key already exists, use the path as key
           if key in file_dict:
               file_dict[full_path] = full_path
               
               # Also update the previous entry with the same key
               old_path = file_dict[key]
               del file_dict[key]
               file_dict[old_path] = old_path
           else:
               file_dict[key] = full_path

   return file_dict


def read_file(file_path):
    global lookup_file_by_link_name
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            file_name = file.name
        wiki_link_pattern = r'\[\[(.*?)\]\]'
        link_positions = []
        lines = []

        line_index = 0
        for line in content.split('\n'):
            end_index = line_index + len(line)
            lines.append({
                'start_index': line_index,
                'end_index': end_index,
                'content': line
            })
            line_index += len(line) + 1

        for line in lines:
            print(line)
    
        for match in re.finditer(wiki_link_pattern, content):
            is_list_item = False
            if match.start() >= 2:
                is_list_item = content[match.start()-2:match.start()] == '- '
            
            start_index = match.start() if not is_list_item else match.start() - 2
            end_index = match.end() - 1
            
            # Find which line contains this match
            line = None
            for item in lines:
                if item['start_index'] <= start_index and item['end_index'] >= end_index:
                    line = item
                    break

            link_positions.append({
                'is_list_item': is_list_item,
                'match': match.group(0),
                'file_key': match.group(1),
                'start_index': start_index,
                'end_index': end_index,
                'line': line
            })

        return {
            'file_path': file_path,
            'file_name': file_name,
            'content': content,
            'links': link_positions
        }

    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found")
        return None


# Example usage
directory_path = "./"
head_file_path = 'llm/outline/_outline.md'
lookup_file_by_link_name = build_file_dict(directory_path)

# for key, path in lookup_file_by_link_name.items():
#    print(f"{key}: {path}")

file = read_file(head_file_path)
print(json.dumps(file, indent=2))