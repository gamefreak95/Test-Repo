import os
import glob
import time
import shutil

def cleanup_releases(release_dir='/releases'):

# Resolve the real path of the 'current' symlink
# Find all the version directories under /releases
# Then sort by modification time (descending)
# Take top 3 more recently modified directories
# Also keep current if it exists in the directory
# Check membership of other files
# Determine 30 day cut off
# Loop through all version directories and delete

    symlink = os.path.join(release_dir,"current")
    if os.path.islink(symlink):
        current_version = os.path.realpath(symlink)
    else:
        current_version = None

    check_ver_directories = [
        dir for dir in glob.glob(os.path.join(release_dir, "ver*"))
            if os.path.isdir(dir)
    ]
    check_ver_directories.sort(key=os.path.getmtime(), reverse=True)

    keep_vers = check_ver_directories[:3]

    if current_version and os.path.isdir(current_version):
        keep_vers.append(current_version)

    keep_vers_set = set(keep_vers)

    now = time.time()
    thirty_days = 30 * 24 * 60 * 60

    for dir in check_ver_directories:
        if dir not in keep_vers_set:
            mtime = os.path.getmtime(dir)
            age = now - mtime
            if age > thirty_days:
                print(f"Deleting old version: {dir}")
                shutil.rmtree(dir, ignore_errors=True)

if __name__ == "__main__":
    cleanup_releases("/releases")

