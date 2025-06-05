from pathlib import Path
from onboardly_core.scanner import scan_project_directory
from onboardly_core.structure_mapper import group_files_by_section
from onboardly_core.summarizer import summarize_section

# 1. Scan the directory
scan = scan_project_directory("examples/sample_project")

# 2. Group files into sections
sections = group_files_by_section(scan)

# 3. Summarize each section

# for section in sections["sections"]:
#     result = summarize_section(
#         section_name=section["name"],
#         file_paths=section["files"],
#         root_path=Path(scan["root"]),
#     )
#     print(f"\n🧠 SECTION: {result['section']}\n{result['summary']}\n{'-'*60}")

summaries = []

for section in sections["sections"]:
    result = summarize_section(
        section_name=section["name"],
        file_paths=section["files"],
        root_path=Path(scan["root"]),
    )
    summaries.append(result)
    print(f"\n🧠 SECTION: {result['section']}\n{result['summary']}\n{'-'*60}")

# 4. Write summaries to a Markdown file
output_file = Path(scan["root"]) / "project_summary.md"
with open(output_file, "w", encoding="utf-8") as f:
    for summary in summaries:
        f.write(f"## 🧠 {summary['section'].capitalize()} Section\n\n")
        f.write(summary["summary"] + "\n\n")
        f.write("---\n\n")

print(f"\n✅ Summary also written to {output_file}")
