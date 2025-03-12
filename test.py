import re

def adjust_headers_sequential(markdown_text):
    header_pattern = re.compile(r'^(#{1,6})\s+(.*?)$', re.MULTILINE)
    matches = []
    by_level = {}
    for match in re.finditer(header_pattern, markdown_text):
        origin_level = len(match.group(1))
        header_text = match.group(2)
        current_match = {
            'origin_level': origin_level,
            'header_text': header_text
        }
        matches.append(current_match)
        if by_level.get(origin_level) is None:
            by_level[origin_level] = []
        by_level[origin_level].append(match)
    i = 0
    while i < max_level:
        i += 1
        for match in matches:



# Test with example
markdown = """## hello
#### test
### asdf
##### dddd"""

print(adjust_headers_sequential(markdown))



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