from typing import List, Dict, Any
from collections import defaultdict
from pathlib import Path


def group_files_by_section(scan_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Groups files by their top-level folder into sections.

    Args:
        scan_data (dict): Output from scanner.py containing 'files' key.

    Returns:
        dict: Grouped sections with file lists.
    """
    sections = defaultdict(list)

    for file in scan_data.get("files", []):
        file_path = file["path"]
        top_level = (
            Path(file_path).parts[0] if len(Path(file_path).parts) > 1 else "root"
        )
        sections[top_level].append(file_path)

    return {
        "sections": [
            {"name": section, "files": sorted(files)}
            for section, files in sorted(sections.items())
        ]
    }


# Optional CLI preview
# if __name__ == "__main__":
#     from scanner import scan_project_directory
#     import json
#
#     scanned = scan_project_directory("./examples/sample_project")
#     grouped = group_files_by_section(scanned)
#     print(json.dumps(grouped, indent=2))
