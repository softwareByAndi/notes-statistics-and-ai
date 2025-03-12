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
               file_dict[full_path.split('.md')[0]] = full_path
               
               # Also update the previous entry with the same key
               old_path = file_dict[key]
               del file_dict[key]
               file_dict[old_path.split('.md')[0]] = old_path
           else:
               file_dict[key] = full_path

   return file_dict


def read_file(file_path):
    global lookup_file_by_link_name
    try:
        file_name = file_path.split('/')[-1].split('.md')[0]
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        wiki_link_pattern = r'\[\[(.*?)\]\]'
        link_positions = []
        lines = []

        char_index = 0
        line_index = 0
        for line in content.split('\n'):
            end_index = char_index + len(line)
            lines.append({
                'start_index': char_index,
                'end_index': end_index,
                'content': line,
                'line_index': line_index
            })
            char_index += len(line) + 1
            line_index += 1
    
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

for key, path in lookup_file_by_link_name.items():
   if 'llm/' in path:
       print(f"{key}: {path}")

queue = []
documents = []
visited = {}

head_doc = read_file(head_file_path)
queue.append(head_doc)

count = 10;
for doc in queue:
    count -= 1;
    if count < 0:
        print('test - count reach 10 iterations')
        break;
    file_path = doc['file_path']
    print('file_path: ', file_path)
    if not visited.get(file_path):
        index = len(documents)
        doc['index'] = index
        parent_index = doc.get('parent_index')
        if parent_index:
            parent = documents[parent_index]

        visited[file_path] = doc
        documents.append(doc)
        for link in doc['links']:
            file_key = link['file_key']
            print(f"  - searching for file: '{file_key}'")
            linked_doc_path = lookup_file_by_link_name.get(file_key)
            print(f"    doc_path: '{linked_doc_path}'")
            linked_doc = read_file(linked_doc_path)
            print(f"    adding to queue: {linked_doc.get('file_path')}")
            linked_doc['parent_index'] = index
            linked_doc['link_data'] = link
            linked_doc['sort_index'] = link['line']['line_index']
            queue.append(linked_doc)