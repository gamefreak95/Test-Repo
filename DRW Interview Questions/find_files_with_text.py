import os

def find_files_with_text(input_file_list, search_text, output_file_list):
    """
    Reads file paths from 'input_file_list'.
    Checks each file for 'search_text'.
    Writes matching paths to 'output_file_list'.
    """
    matching_files = []

    with open(input_file_list, 'r') as f:
        for line in f:
            file_path = line.strip()
            if not file_path or not os.path.isfile(file_path):
                continue  # Skip empty or invalid entries

            try:
                with open(file_path, 'r') as fr:
                    content = fr.read()
                    if search_text in content:
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Could not read {file_path}: {e}")

    # Write all matching files to the output list
    with open(output_file_list, 'w') as fw:
        for mf in matching_files:
            fw.write(mf + "\n")

    print(f"Found {len(matching_files)} file(s) containing '{search_text}'.")
    print(f"Results saved to: {output_file_list}")

if __name__ == "__main__":
    # Example usage:
    input_file_list  = r"C:\temp\files.txt"         # The text file listing file paths, one path per line
    search_text      = "Insert text to search for here"                  # The string to look for
    output_file_list = r"C:\temp\found_files.txt"   # Where to write the matching file paths

    find_files_with_text(input_file_list, search_text, output_file_list)
