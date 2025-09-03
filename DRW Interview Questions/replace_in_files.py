import os

def replace_in_files(files_list_path, old_string, new_string):

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

    files_list = r"C:\temp\files.txt"
    old_string   = "InsertOldStringHere"
    new_string   = "InsertNewStringHere"

    replace_in_files(files_list, old_string, new_string)