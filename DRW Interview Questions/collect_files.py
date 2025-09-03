import os
import shutil

def collect_files(hosts_list, remote_subpath, local_dir):
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    with open(hosts_list, 'r') as f:
        for line in f:
            host = line.strip()
            if not host:
                continue  # skip blank lines

            unc_path = fr"\\{host}\C$\{remote_subpath.strip('\\/')}"

            local_dest = os.path.join(local_dir, f"{host}-output.txt")

            # Check if the file actually exists remotely
            if os.path.exists(unc_path):
                try:
                    shutil.copy2(unc_path, local_dest)
                    print(f"Copied file from {host} to {local_dest}")
                except Exception as e:
                    print(f"Failed to copy from {host}: {e}")
            else:
                print(f"File not found on {host}: {unc_path}")


if __name__ == "__main__":
    hosts_list = r"C:\\temp\\hosts.txt"
    remote_file = r"temp\output.txt"
    local_dir = r"C:\temp\collected"

    collect_files(hosts_list, remote_file, local_dir)