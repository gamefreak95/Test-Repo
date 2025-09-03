#!/usr/bin/env python3

import os
import glob
import time
import shutil


def cleanup_releases(release_dir="/releases"):
    # 1. Resolve the real path of the "current" symlink
    current_symlink = os.path.join(release_dir, "current")
    if os.path.islink(current_symlink):
        current_version = os.path.realpath(current_symlink)
    else:
        current_version = None

    # 2. Find all "ver*" directories under /releases
    #    Then sort by modification time (descending)
    ver_dirs = [d for d in glob.glob(os.path.join(release_dir, "ver*")) if os.path.isdir(d)]
    ver_dirs.sort(key=os.path.getmtime, reverse=True)

    # 3. Take the top 3 most recently modified directories
    keep_list = ver_dirs[:3]

    # Also keep the current symlink target (if it exists and is a directory)
    if current_version and os.path.isdir(current_version):
        keep_list.append(current_version)

    # Make a set for quick membership checks
    keep_set = set(keep_list)

    # 4. Determine cutoff for "older than 30 days"
    now = time.time()
    thirty_days = 30 * 24 * 60 * 60

    # 5. Loop through all ver* directories
    #    If not in keep_set and older than 30 days, delete
    for d in ver_dirs:
        if d not in keep_set:
            mtime = os.path.getmtime(d)
            age = now - mtime
            if age > thirty_days:
                print(f"Deleting old version: {d}")
                shutil.rmtree(d, ignore_errors=True)


if __name__ == "__main__":
    cleanup_releases("/releases")