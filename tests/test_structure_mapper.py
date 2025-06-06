from cbtg.structure_mapper import group_files_by_section


def test_group_files_by_section():
    # Simulated scan result (as from scanner.py)
    scan_data = {
        "files": [
            {"path": "main.py", "size_kb": 1.2, "ext": ".py"},
            {"path": "README.md", "size_kb": 0.5, "ext": ".md"},
            {"path": "auth/login.py", "size_kb": 0.9, "ext": ".py"},
            {"path": "auth/register.py", "size_kb": 1.0, "ext": ".py"},
            {"path": "utils/helpers.py", "size_kb": 0.8, "ext": ".py"},
        ]
    }

    result = group_files_by_section(scan_data)

    expected_sections = [
        {"name": "auth", "files": ["auth/login.py", "auth/register.py"]},
        {"name": "root", "files": ["README.md", "main.py"]},
        {"name": "utils", "files": ["utils/helpers.py"]},
    ]

    # Convert to dicts for comparison regardless of order
    actual_sections = {s["name"]: set(s["files"]) for s in result["sections"]}
    expected = {s["name"]: set(s["files"]) for s in expected_sections}

    assert actual_sections == expected
