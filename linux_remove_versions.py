import os
import shutil
import time
import glob

def cleanup_releases(directory_versions):
    ver_dirs = directory_versions

    current_symlink = os.path.join(ver_dirs,"current")

    if os.path.islink(current_symlink):
        current_version = os.path.realpath(current_symlink)
    else:
        current_version = None

    all_paths = glob.glob(os.path.join(ver_dirs, "ver*"))
    directories = []

    for dirs in all_paths:
        if os.path.isdir(dirs):
            directories.append(dirs)

    sorted_dirs = directories.sort(key=os.path.getmtime, reverse=True)
    keep_list = sorted_dirs[:3]

    if current_version and os.path.isdir(current_version):
        keep_list.append(current_version)

    keep_set = set(keep_list)
    current_time = time.time()
    thirty_days = 30 * 24 * 360

    for dirs in directories:
        if dirs not in keep_set:
            mtime = os.path.getmtime(dirs)
            age = current_time - mtime
            if age > thirty_days:
                shutil.rmtree(dirs, ignore_errors=True)


if __name__ == "__main__":
    cleanup_releases("/releases")