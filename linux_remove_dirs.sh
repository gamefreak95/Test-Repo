#!/bin/bash

RELEASE_DIR="/releases"
CURRENT_VERSION=$(readlink -f "$RELEASE_DIR/current")

VERSIONS=($(ls -dt "$RELEASE_DIR"/ver* 2>/dev/null | head -3))

KEEP_VERSIONS=("${VERSIONS[@]}" "$CURRENT_VERSION")

for version in "$RELEASE_DIR"/ver*; do
  if [[ -d "$version" ]]; then
    if [[ ! "${KEEP_VERSIONS[*]}" =~ "$version" ]]; then
      if [[ -n "$(find "$version" -maxdepth 0 -type d -mtime +30 2>/dev/null)" ]]; then
        rm -rf "$version"
      fi
    fi
  fi
done

