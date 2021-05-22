# Disk Usage Utility

This program takes a mount point as an argument and returns a JSON object containing an array of all the files on the specified mount point including the size of each file.

Written using Python 3+.


## Example

Given a file structure like the one below:

```
\example
    file1.txt
    \folder1
        file2.txt
```

Run the program with `\example` as a CLI argument:

`% python getdiskusage.py \example`

Running the command above will produce an output similar to:

```
%  python getdiskusage.py /example
{
    "files": [
        {
            "path": "/example/file1.txt",
            "size": 12
        },
        {
            "path": "/example/folder1/file2.txt",
            "size": 18
        }
    ]
}
```
