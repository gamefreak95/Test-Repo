import os
import glob
import sys
def delete_matching_files(matching_string):
    string = matching_string

    if not string:
        print("Enter valid file name")
        sys.exit(1)

    files_deleted = 0

    matching_files = glob.glob(f"*{string}*")

    for files in matching_files:
        if os.path.isfile(files):
            os.remove(files)
            files_deleted +=1

    sys.exit(files_deleted)

if __name__ == "__main__":
    search_string = sys.argv[1]
    delete_matching_files(search_string)