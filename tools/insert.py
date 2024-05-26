import os

# Define the directory and the header to be added
posts_dir = '_posts'
header = """---
tags: [Waterdeep]
---
"""

# Iterate over all files in the _posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith('.markdown') or filename.endswith('.md'):
        filepath = os.path.join(posts_dir, filename)
        
        # Read the original content of the file
        with open(filepath, 'r', encoding='utf-8') as file:
            original_content = file.read()
        
        # Write the new content with the header
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(header + original_content)

print("Headers added to all markdown files in the _posts directory.")