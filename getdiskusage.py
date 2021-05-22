import os, sys, json
from pathlib import Path

# Receive arguments from the CLI and set into mount_point variable.
# If no mountpoint is specified, return error and exit.
try:
    mount_point = sys.argv[1]
except IndexError:
    print(json.dumps({"error": "No mountpoint specified."}, indent=4))
    exit()

# Dictionary used to hold output of file paths and file sizes.
disk_usage = {"files": []}


def find_file_sizes(mount_point):
    """
    Uses the mount_point argument to obtain and loop through the contents of a directory.
    If an item is not a directory, the files size will be determined and then added to the disk_usage["files"] list.
    If an item is a directory, recursion is used to loop through the contents and perform the steps above.
    Returns an error and exits if no mount point was found.
    """

    try:
        contents = os.listdir(mount_point)

        for file in contents:
            path = os.path.join(mount_point, file)

            if not os.path.isdir(path):
                disk_usage["files"].append(
                    {"path": path, "size": Path(path).stat().st_size}
                )
            else:
                find_file_sizes(path)

    except FileNotFoundError:
        print(json.dumps({"error": f"No mountpoint '{mount_point}' found."}, indent=4))
        exit()


# Execute function with mount_point variable taken from CLI.
find_file_sizes(mount_point)

# Return dictionary containing files and file sizes in JSON format.
print(json.dumps(disk_usage, indent=4))
