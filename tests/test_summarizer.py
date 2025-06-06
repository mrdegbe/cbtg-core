import pytest
from pathlib import Path
from cbtg_core.summarizer import summarize_section
from unittest.mock import patch, MagicMock
import tempfile


@pytest.fixture
def temp_project_dir():
    with tempfile.TemporaryDirectory() as tmpdirname:
        root = Path(tmpdirname)
        file_path = root / "test_file.py"
        file_path.write_text("def hello():\n    return 'Hello, world!'\n")
        yield root, ["test_file.py"]


@patch("cbtg_core.summarizer.client.chat.completions.create")
def test_summarize_section_returns_summary(mock_create, temp_project_dir):
    root_path, file_paths = temp_project_dir

    # Mock OpenAI response
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="This is a mock summary."))
    ]
    mock_create.return_value = mock_response

    result = summarize_section("test-section", file_paths, root_path)

    assert result["section"] == "test-section"
    assert "summary" in result
    assert result["summary"] == "This is a mock summary."
    mock_create.assert_called_once()
