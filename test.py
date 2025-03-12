import re

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
    matches = sorted(matches, key=lambda match: match['start'], reverse=True)
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



# Test with example
markdown = """
## a
#### b
### c
###### d
### e 
"""

print(normalize_headers(markdown))



"""
## a
#### b
### c
###### d
### e
"""

"""
# a
## b
## c
### d
## e 
"""