import os
import re
import json

def normalize_headers(markdown_text):
    header_pattern = re.compile(r'^(#{1,6})\s+(.*?)$', re.MULTILINE)
    matches = []
    by_level = {}

    # get matches
    for match in re.finditer(header_pattern, markdown_text):
        origin_level = len(match.group(1))
        header_text = match.group(2)
        current_match = {
            'origin_level': origin_level,
            'header_text': header_text,
            'start_index': match.start()
        }
        matches.append(current_match)
        if by_level.get(origin_level) is None:
            by_level[origin_level] = []
        by_level[origin_level].append(match)

    # normalize
    current_level = 1
    normalized_level_by_origin_level = {}
    for i in sorted(by_level.keys()):
        normalized_level_by_origin_level[i] = current_level
        current_level += 1

    def update_header(match):
        # Get the current header level and text
        current_header = match.group(1)
        header_text = match.group(2)
        # Calculate the new header level
        origin_level = len(current_header)
        new_level = normalized_level_by_origin_level[origin_level]
        # Cap at 6 hashtags (markdown only supports h1-h6)
        new_level = min(new_level, 7)
        # Create the new header
        if new_level < 7:
            new_header = f"{'#'*new_level} {header_text}"
        else:
            new_header = f"**{header_text}:**"
        return new_header

    normalized_content = header_pattern.sub(update_header, markdown_text)
    return normalized_content
