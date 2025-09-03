#!/bin/bash

RELEASE_DIR="/releases"
CURRENT_VERSION=$(readlink -f "$RELEASE_DIR/current")

# Get the 3 most recent versions
VERSIONS=($(ls -dt "$RELEASE_DIR"/ver* 2>/dev/null | head -3))

# Ensure the current version is kept
KEEP_VERSIONS=("${VERSIONS[@]}" "$CURRENT_VERSION")

# Delete older versions not in KEEP_VERSIONS and older than 30 days
for version in "$RELEASE_DIR"/ver*; do
    if [[ -d "$version" && ! " ${KEEP_VERSIONS[*]} " =~ " $version " ]]; then
        # Check if it's older than 30 days
        if [[ -n "$(find "$version" -maxdepth 0 -type d -mtime +30 2>/dev/null)" ]]; then
            echo "Deleting old version: $version"
            rm -rf "$version"
        fi
    fi
done

----------------------------------------------------
