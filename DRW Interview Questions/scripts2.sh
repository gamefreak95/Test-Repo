#!/bin/bash
# Ensure a search string is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <search_string>"
    exit 1
fi

SEARCH_STRING="$1"

# Initialize counter
FILES_DELETED=0

# Find and delete matching files in the current directory
for file in *"$SEARCH_STRING"*; do
    if [ -f "$file" ]; then
        rm "$file"
        ((FILES_DELETED++))
    fi
done

# Output the number of deleted files
echo "Deleted $FILES_DELETED file(s)."

# Return the number of deleted files as exit status
exit $FILES_DELETED
