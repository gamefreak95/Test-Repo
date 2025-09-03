import os

def find_files_with_text(files_list , search_text, files_with_text_list):

    matching_files = []

    with open(files_list , 'r', encoding='utf-8') as f:
        for line in f:
            file_path = line.strip()
            if not file_path or not os.path.isfile(file_path):
                continue

            try:
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as fr:
                    content = fr.read()
                    if search_text in content:
                        matching_files.append(file_path)
            except Exception as e:
                print(f"Could not read {file_path}: {e}")

    with open(files_with_text_list, 'w', encoding='utf-8') as fw:
        for mf in matching_files:
            fw.write(mf + "\n")

    print(f"Found {len(matching_files)} file(s) containing '{search_text}'.")
    print(f"Results saved to: {files_with_text_list}")

if __name__ == "__main__":

    files_list = r"C:\temp\files.txt"
    search_text = "Insert text to search for here"
    files_with_text_list = r"C:\temp\found_files.txt"

    find_files_with_text(files_list , search_text, files_with_text_list)
