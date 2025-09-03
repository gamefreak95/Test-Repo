import os
import shutil

def collect_files(hostname_list, remote_subpath, local_directory):

    #For each hostname in hostname_list, copy \\<hostname>\c$\<remote_subpath>
    #to local_directory\<computer>-output.txt

    # Ensure the local directory exists
    if not os.path.exists(local_directory):
        os.makedirs(local_directory)

    with open(hostname_list, 'r') as f:
        for line in f:
            host = line.strip()
            if not host:
                continue  # skip blank lines

            # Build UNC path: \\<computer>\c$\<remote_subpath>
            unc_path = fr"\\{host}\c$\{remote_subpath.strip('\\/')}"

            # Destination file named after the computer
            local_destination = os.path.join(local_directory, f"{host}-output.txt")

            # Check if the file actually exists remotely
            if os.path.exists(unc_path):
                try:
                    shutil.copy2(unc_path, local_destination)
                    print(f"Copied file from {host} to {local_destination}")
                except Exception as e:
                    print(f"Failed to copy from {host}: {e}")
            else:
                print(f"File not found on {host}: {unc_path}")

if __name__ == "__main__":
    # Example usage
    hostname_list = r"C:\\temp\\hostname_list.txt"
    # The remote file path relative to c$, e.g. 'temp\output.txt'
    remote_file = r"temp\output.txt"
    # Where to store collected files locally
    local_directory = r"C:\temp\collected"

    collect_files(hostname_list, remote_file, local_directory)

-------------------------------------------------------

import os

def replace_in_files(files_list_path, old_string, new_string):
    """
    For each file listed in files_list_path, replace old_string with new_string.
    """
    # Read list of files from the text file
    with open(files_list_path, 'r', encoding='utf-8') as f:
        file_paths = [line.strip() for line in f if line.strip()]

    # Process each file
    for path in file_paths:
        if not os.path.isfile(path):
            print(f"File not found: {path}")
            continue

        try:
            # Read file content
            with open(path, 'r', encoding='utf-8', errors='ignore') as fr:
                content = fr.read()

            # Replace text
            updated_content = content.replace(old_string, new_string)

            # Write updated content back to the file
            with open(path, 'w', encoding='utf-8', errors='ignore') as fw:
                fw.write(updated_content)

            print(f"Replaced '{old_string}' with '{new_string}' in {path}")

        except Exception as e:
            print(f"Error processing {path}: {e}")

if __name__ == "__main__":
    # Example usage
    files_list = r"C:\temp\files.txt"   # each line = full path to a file
    old_text   = "oldString"
    new_text   = "newString"

    replace_in_files(files_list, old_text, new_text)

-------------------------------------------------------

import os

def find_files_with_text(input_file_list, search_text, output_file_list):
    """
    Reads file paths from 'input_file_list'.
    Checks each file for 'search_text'.
    Writes matching paths to 'output_file_list'.
    """
    matching_files = []

    with open(input_file_list, 'r', encoding='utf-8') as f:
        for line in f:
            file_path = line.strip()
            if not file_path or not os.path.isfile(file_path):
                continue  # Skip empty or invalid entries

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as fr:
                    content = fr.read()
                    if search_text in content:
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Could not read {file_path}: {e}")

    # Write all matching files to the output list
    with open(output_file_list, 'w', encoding='utf-8') as fw:
        for mf in matching_files:
            fw.write(mf + "\n")

    print(f"Found {len(matching_files)} file(s) containing '{search_text}'.")
    print(f"Results saved to: {output_file_list}")

if __name__ == "__main__":
    # Example usage:
    input_file_list  = r"C:\temp\files.txt"         # The text file listing file paths, one path per line
    search_text      = "ERROR 404"                  # The string to look for
    output_file_list = r"C:\temp\found_files.txt"   # Where to write the matching file paths

    find_files_with_text(input_file_list, search_text, output_file_list)
