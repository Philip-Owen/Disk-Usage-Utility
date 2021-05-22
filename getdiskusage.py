import os, sys, json
from pathlib import Path


mount_point = sys.argv[1]

disk_usage = {"files": []}


def find_file_sizes(mount_point):
    contents = os.listdir(mount_point)

    for file in contents:
        path = os.path.join(mount_point, file)

        if not os.path.isdir(path):
            disk_usage["files"].append(
                {"path": path, "size": Path(path).stat().st_size}
            )
        else:
            find_file_sizes(path)


find_file_sizes(mount_point)

print(json.dumps(disk_usage, indent=4))
