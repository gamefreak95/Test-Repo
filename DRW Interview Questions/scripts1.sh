#!/usr/bin/env bash

HOSTS_FILE="hosts.txt"

while read -r HOST; do
    # scp: copy from remote:/tmp/output.txt to local: /tmp/HOST-output.txt
    scp "$HOST:/tmp/output.txt" "/tmp/${HOST}-output.txt" && \
        echo "Collected file from $HOST" || \
        echo "Failed to collect file from $HOST"
done < "$HOSTS_FILE"

-------------------------------------------------------

#!/usr/bin/env bash

OLD="oldString"
NEW="newString"
FILES_LIST="files.txt"

while read -r file; do
    if [[ -f "$file" ]]; then
        sed -i "s/$OLD/$NEW/g" "$file"
        echo "Replaced text in: $file"
    else
        echo "File not found: $file"
    fi
done < "$FILES_LIST"

-------------------------------------------------------

#!/usr/bin/env bash

SEARCH="my search text"
FILES_LIST="files.txt"
OUTPUT_LIST="files_with_text.txt"

> "$OUTPUT_LIST"  # Empty or create the output list

while read -r file; do
    if [[ -f "$file" ]]; then
        # -q causes grep to be silent
        if grep -q "$SEARCH" "$file"; then
            echo "$file" >> "$OUTPUT_LIST"
        fi
    fi
done < "$FILES_LIST"

echo "Files containing '$SEARCH':"
cat "$OUTPUT_LIST"