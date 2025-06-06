# run_tour.py
import sys, io
from pathlib import Path
from cbtg.scanner import scan_project_directory
from cbtg.structure_mapper import group_files_by_section
from cbtg.summarizer import summarize_section

# 🔧 Force stdout to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.append(str(Path(__file__).resolve().parent.parent))

def format_tour(sections, fmt="text"):
    output = []
    for section in sections:
        title = f"### {section['section']}" if fmt == "md" else f"🔹 {section['section']}"
        summary = section["summary"]
        output.append(f"{title}\n{summary}\n")
    return "\n".join(output)

def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python run_tour.py <path> [--format text|md]")
        return

    target_path = Path(sys.argv[1]).resolve()
    fmt = "text"
    if "--format" in sys.argv:
        fmt_index = sys.argv.index("--format")
        if fmt_index + 1 < len(sys.argv):
            fmt = sys.argv[fmt_index + 1]

    scan = scan_project_directory(str(target_path))
    sections = group_files_by_section(scan)

    summaries = []
    for section in sections["sections"]:
        result = summarize_section(
            section_name=section["name"],
            file_paths=section["files"],
            root_path=Path(scan["root"]),
        )
        summaries.append(result)

    print(format_tour(summaries, fmt=fmt))

if __name__ == "__main__":
    main()
