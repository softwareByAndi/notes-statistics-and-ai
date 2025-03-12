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
    # Step 1: Split the text into code blocks and non-code blocks
    parts = []
    in_code_block = False
    current_part = ""
    
    for line in markdown_text.split('\n'):
        if line.strip().startswith('```'):
            # Add the current part to our list
            parts.append((current_part, in_code_block))
            current_part = line + '\n'
            in_code_block = not in_code_block
        else:
            current_part += line + '\n'
    
    # Add the final part
    parts.append((current_part, in_code_block))
    
    # Step 2: Only apply the header pattern to non-code blocks
    header_pattern = re.compile(r'^(#{1,6})\s+(.*?)$', re.MULTILINE)
    headers = []
    
    for text, is_code_block in parts:
        if not is_code_block:
            for match in header_pattern.finditer(text):
                level = len(match.group(1))
                content = match.group(2)
                start = match.start()
                end = match.end()
                length = end - start
                headers.append({
                    'level': level,
                    'start': start, 
                    'end': end, 
                    'length': length, 
                    'content': content
                })
    return headers


def normalize_headers(markdown_text):
    by_level = {}
    matches = find_markdown_headers(markdown_text)
    matches = sorted(lambda match: match['start'], matches)
    matches.reverse()

    # get matches
    for match in matches:
        origin_level = len(match['level'])
        header_text = match['content']
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
        header_text = match['content']
        new_level = normalized_level_by_origin_level[match['level']]
        # Cap at 6 hashtags (markdown only supports h1-h6)
        new_level = min(new_level, 7)
        # Create the new header
        if new_level < 7:
            new_header = f"{'#'*new_level} {header_text}"
        else:
            new_header = f"**{header_text}:**"
        markdown_text[match['start']:match['end']] = new_header

    return markdown_text


def adjust_headers(master_level, content):
    if not isinstance(master_level, int) or master_level < 1 or master_level > 6:
        raise ValueError("Master level must be an integer between 1 and 6")
    # Regex to find markdown headers (# to ######)
    header_pattern = re.compile(r'^(#{1,6})\s+(.*?)$', re.MULTILINE)
    

    normalized_content = normalize_headers(content)
    for match in find_markdown_headers(normalized_content):
        new_level = master_level + match['level']
        new_level = min(new_level, 7)
        if new_level < 7:
            new_header = f"{'#'*new_level} {match['content']}"
        else:
            new_header = f"**{match['content']}:**"
        normalized_content[match['start']:match['end']] = new_header
    
    return normalized_content






# Example usage
directory_path = "./"
head_file_path = 'llm/modules/mod 1/1.6 Hands-On Project - Using an Existing LLM via API.md'
data = parse_file(head_file_path)['content']
# normalized_content = adjust_headers(2, data)
# print(normalized_content)
print(find_markdown_headers(data))