import sys, io
from pathlib import Path
from cbtg.scanner import scan_project_directory
from cbtg.structure_mapper import group_files_by_section
from cbtg.summarizer import summarize_section

# 🔧 Force stdout to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.append(str(Path(__file__).resolve().parent.parent))

def main(project_path: str):
    path = Path(project_path).resolve()
    scan = scan_project_directory(str(path))
    sections = group_files_by_section(scan)

    for section in sections["sections"]:
        result = summarize_section(
            section_name=section["name"],
            file_paths=section["files"],
            root_path=Path(scan["root"]),
        )
        print(f"\n🧠 SECTION: {result['section']}\n{result['summary']}\n{'-'*60}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python run_summary.py <path_to_project>")
        sys.exit(1)

    project_path = sys.argv[1]
    print(f"✅ Scanning project at: {project_path}")
    main(project_path)
