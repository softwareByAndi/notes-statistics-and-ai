import re

def adjust_headers_sequential(markdown_text):
    header_pattern = re.compile(r'^(#{1,6})\s+(.*?)$', re.MULTILINE)
    matches = []
    for match in re.finditer(header_pattern, markdown_text):
        current_header = match.group(1)
        header_text = match.group(2)
        

# Test with example
markdown = """## hello
#### test
### asdf
##### dddd"""

print(adjust_headers_sequential(markdown))