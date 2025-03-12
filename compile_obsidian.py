import os
import re

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
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        wiki_link_pattern = r'\[\[(.*?)\]\]'
        matches = re.findall(wiki_link_pattern, content, re.DOTALL)
        for match in matches:
            print(match);

    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found")
        return None


# Example usage
directory_path = "./"
head_file_path = 'llm/outline/_outline.md'
# lookup_file_by_link_name = build_file_dict(directory_path)

# for key, path in lookup_file_by_link_name.items():
#    print(f"{key}: {path}")

read_file(head_file_path)