import os
import re
import uuid

# Define a regex pattern for matching front matter
FRONTMATTER_PATTERN = re.compile(r'^---\s*$(.*?)^---\s*$', re.MULTILINE | re.DOTALL)

# Get the path to the desktop
# desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
desktop_path = "./"

# Recursively search through all directories on the desktop
for root, dirs, files in os.walk(desktop_path):
    # Loop through all the files
    for filename in files:
        # Check if the file is a Markdown file
        if filename.endswith('.md'):
            # Open the file and read its contents
            with open(os.path.join(root, filename), 'r') as f:
                contents = f.read()

            # Use the regex pattern to strip off the front matter
            contents = FRONTMATTER_PATTERN.sub('', contents)

            # Generate a unique file name
            new_filename = str(uuid.uuid1()) + '.md'

            # Save the modified file to the current directory
            with open(os.path.join(os.getcwd(), new_filename), 'w') as f:
                f.write(contents)
