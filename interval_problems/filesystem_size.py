"""
Given a file system structure (nested dicts), return the total size of all files.

Structure rules:
  - A dict represents a directory. Keys are names, values are either:
      - another dict  → subdirectory
      - an int        → file with that size in bytes
"""

filesystem = {
    "home": {
        "me": {
            "foo.txt": 416,
            "metrics.txt": 5892,
            "src": {
                "site.html": 6051,
                "site.css": 5892,
                "data.csv": 332789,
            },
        },
        "you": {
            "dict.json": 4913364,
        },
    },
    "bin": {
        "bash": 618416,
        "cat": 23648,
        "ls": 38704,
    },
    "var": {
        "log": {
            "dmesg": 1783894,
            "wifi.log": 924818,
            "httpd": {
                "access.log": 17881,
                "access.log.0.gz": 4012,
            },
        },
    },
}


def total_size(node):
    """
    Recursively walk the filesystem tree.
      - If node is an int   → it's a file; its value IS the size.
      - If node is a dict   → it's a directory; sum the sizes of all children.
    """
    if isinstance(node, int):
        return node

    # It's a directory: recurse into every child and accumulate
    return sum(total_size(node=child) for child in node.values())


if __name__ == "__main__":
    result = total_size(filesystem)
    print(f"Total size: {result} bytes")   # expected: 8,769,781
