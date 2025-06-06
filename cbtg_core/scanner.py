import os
from pathlib import Path
from typing import List, Dict, Any


def scan_project_directory(root_path: str) -> Dict[str, Any]:
    """
    Walks through a project directory and collects metadata on files and folders.

    Args:
        root_path (str): Path to the root of the project to scan.

    Returns:
        dict: Structure containing file metadata and folder paths.
    """
    root = Path(root_path).resolve()

    if not root.exists() or not root.is_dir():
        raise ValueError(f"Invalid directory: {root_path}")

    files: List[Dict[str, Any]] = []
    folders: List[str] = []

    for dirpath, dirnames, filenames in os.walk(root):
        folders.append(os.path.relpath(dirpath, start=root))

        for filename in filenames:
            filepath = Path(dirpath) / filename
            rel_path = os.path.relpath(filepath, start=root)
            size_kb = round(filepath.stat().st_size / 1024, 2)
            ext = filepath.suffix

            files.append(
                {
                    "path": rel_path,
                    "size_kb": size_kb,
                    "ext": ext,
                }
            )

    return {
        "root": str(root),
        "files": files,
        "folders": folders,
    }


# Optional: quick test run
# if __name__ == "__main__":
#     import json
#
#     scan_result = scan_project_directory("./examples/sample_project")
#     print(json.dumps(scan_result, indent=2))
