# 📦 Codebase Tour Guide (`cbtg`) - core


**Codebase Tour Guide Core** (`cbtg-core`) is the Python backend engine for generating intelligent codebase summaries and guided tours. It is designed to be used alongside the `cbtg` CLI written in Go.

---

### 🚀 Features

* 📂 Scans any Python project and groups files by structure (e.g. modules or folders)
* 🧠 Summarizes each section using AI
* 🧭 Generates guided codebase tours in plain text or Markdown
* 🔌 Modular and extensible for integration with other tools

---

### 🛠️ Installation

```bash
git clone https://github.com/mrdegbe/cbtg-core.git
cd cbtg-core
pip install -r requirements.txt
```

---

### 📁 Folder Structure

```
cbtg_core/
├── scanner.py           # Recursively scans a Python project
├── structure_mapper.py  # Groups files into logical sections
├── summarizer.py        # Generates summaries for each section
├── tour_guide.py        # Generates full code tours
run_summary.py           # CLI: summarize the entire codebase
run_tour.py              # CLI: generate a guided tour
```

---

### ⚙️ Usage

#### 🔍 To summarize a project:

```bash
python run_summary.py path/to/project
```

#### 🧭 To generate a guided tour:

```bash
python run_tour.py path/to/project --format text
# or
python run_tour.py path/to/project --format md
```

---

### 📄 Output Formats

* `text`: CLI-friendly, human-readable summary
* `md`: Markdown-formatted output for docs

---

### 🧪 Example Output

```markdown
### auth
This module handles authentication, including token verification and user login.

### utils
Utility functions for validation, file I/O, and string manipulation.
```

---

### 🧰 Requirements

* Python 3.8+
* OpenAI or OpenRouter key (for AI summaries)

---

### 🧠 Coming Soon

* JSON output for programmatic use
* Local model fallback for offline environments
* API-ready module

---

### 🛡 License

MIT License © 2025 Raymond Degbe

---