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


def parse_file(file_path):
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

        # strip first header, as it will be replaced with file name
        content = content.strip()
        if (content[0] == '#'):
            content = '\n'.join(content.split('\n')[1:]).strip()

        return {
            'file_path': file_path,
            'file_name': re.sub('^_', '', file_name),
            'extension': file_path.split('.')[-1],
            'content': content,
            'links': link_positions
        }

    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found")
        return None


def wrap_non_md_file(file):
    content = ''
    if file['extension'] == 'ipynb':
        data = json.loads(file['content'])
        for cell in data['cells']:
            if cell['cell_type'] == 'markdown':
                content += ''.join(cell['source']) + '\n\n'
            elif cell['cell_type'] == 'python':
                code = f"``` python\n{''.join(cell['source'])}"
                content += code + '\n\n'
            else:
                code = f"``` {cell['cell_type']}\n{''.join(cell['source'])}"
                content += code + '\n\n'
    else:
        content = f"``` {file['extension']}\n{file[content]}\n```"
    return content
def find_markdown_headers(markdown_text):
    blocks = markdown_text.split('```')
    # Step 2: Only apply the header pattern to non-code blocks
    header_pattern = re.compile(r'^(#{1,6})\s+(.*?)$', re.MULTILINE)
    headers = []
    
    i = 0
    char_index = 0
    content = ''
    while i < len(blocks):
        if i % 2 == 1:
            content += f"``` {blocks[i].strip()} ```"
            char_index = len(content) - 1
        else:
            content += blocks[i]
            for match in re.finditer(header_pattern, blocks[i]):
                level = len(match.group(1))
                match_content = match.group(2)
                start = match.start() + char_index
                end = match.end() + char_index
                length = end - start
                headers.append({
                    'level': level,
                    'start': start, 
                    'end': end,
                    'length': length,
                    'content': match_content
                })
        i += 1
    return sorted(headers, key=lambda match: match['start'])


def normalize_headers(markdown_text):
    by_level = {}
    matches = find_markdown_headers(markdown_text)
    matches.reverse()
    # get matches
    for match in matches:
        origin_level = match['level']
        if by_level.get(origin_level) is None:
            by_level[origin_level] = []
        by_level[origin_level].append(match)
    # normalize
    current_level = 1
    normalized_level_by_origin_level = {}
    for i in sorted(by_level.keys()):
        normalized_level_by_origin_level[i] = current_level
        current_level += 1

    for match in matches:
        new_level = normalized_level_by_origin_level[match['level']]
        new_level = min(new_level, 7)
        if new_level < 7:
            new_header = f"{'#'*new_level} {match['content']}"
        else:
            new_header = f"**{match['content']}:**"
        markdown_text = ''.join([
            markdown_text[:match['start']],
            new_header,
            markdown_text[match['end']:]
        ])
    return markdown_text


def adjust_headers(master_level, content):
    if not isinstance(master_level, int) or master_level < 1 or master_level > 6:
        raise ValueError("Master level must be an integer between 1 and 6")
    normalized_content = normalize_headers(content)
    matches = find_markdown_headers(normalized_content)
    matches.reverse()
    for match in matches:
        new_level = master_level + match['level']
        new_level = min(new_level, 7)
        if new_level < 7:
            new_header = f"{'#' * new_level} {match['content']}"
        else:
            new_header = f"**{match['content']}:**"
        normalized_content = ''.join([
            normalized_content[:match['start']],
            new_header,
            normalized_content[match['end']:]
        ])
        origin_content = f"{'#' * match['level']} {match['content']}"
        print(origin_content)
    return normalized_content






# Example usage
directory_path = "./"
head_file_path = 'llm/modules/mod 1/1.6 Hands-On Project - Using an Existing LLM via API.md'
data = parse_file(head_file_path)['content']
# norm_content = normalize_headers(data)
# print(norm_content)

adj_content = adjust_headers(3, data)
print(adj_content)
