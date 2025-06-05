import os, sys, shutil
from onboardly_core.scanner import scan_project_directory
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))


def setup_sample_project(base_path: Path):
    """
    Creates a temporary sample project for testing.
    Structure:
    sample_project/
        main.py
        README.md
        utils/
            helper.py
    """
    os.makedirs(base_path / "utils", exist_ok=True)

    (base_path / "main.py").write_text("# main app")
    (base_path / "README.md").write_text("## Readme")
    (base_path / "utils" / "helper.py").write_text("# helper")


def teardown_sample_project(base_path: Path):
    if base_path.exists():
        shutil.rmtree(base_path)


def test_scan_project_directory():
    temp_path = Path("tests/temp_sample_project").resolve()

    try:
        setup_sample_project(temp_path)

        result = scan_project_directory(str(temp_path))

        assert result["root"] == str(temp_path)
        assert set(result["folders"]) == {".", "utils"}

        file_paths = [f["path"] for f in result["files"]]
        assert "main.py" in file_paths
        assert "README.md" in file_paths
        assert os.path.join("utils", "helper.py") in file_paths

        for file in result["files"]:
            assert file["size_kb"] > 0
            assert file["ext"] in [".py", ".md"]

    finally:
        teardown_sample_project(temp_path)
