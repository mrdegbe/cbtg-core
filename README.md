# Onboardly Core

🧠 Core engine for Onboardly – an AI-powered codebase tour guide.  
This module scans project directories, maps structures, and produces plain-English summaries of each part.

## Modules

- `scanner.py` – traverses file system and collects metadata
- `structure_mapper.py` – groups files logically
- `summarizer.py` – AI summaries (stubbed for now)
- `utils.py` – helper functions

## Usage (Coming Soon)

```bash
python -m onboardly_core.scanner ./examples/sample_project
