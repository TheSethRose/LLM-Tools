# LLM Tools

A collection of tools designed to help with Large Language Model (LLM) development and debugging.

## Code Tree Generator

The Code Tree Generator (`generate.py`) creates a Markdown file containing your project's directory structure and file contents in a format that's optimized for pasting into LLMs for debugging or analysis.

### Features

- Generates a clean directory tree structure
- Includes file contents with line numbers
- Respects `.gitignore` rules
- Supports custom path exclusions
- Outputs in Markdown format optimized for LLM consumption

### Usage

```bash
python generate.py
```

This will create an `output.md` file containing:
1. A tree view of your project structure
2. The contents of each file with line numbers

### Configuration

You can customize which files/directories to exclude by modifying the `CUSTOM_EXCLUDES` list in `generate.py`:

```python
CUSTOM_EXCLUDES = [
    '.devcontainer/',
    '.github/',
    '.vscode/',
    'node_modules/',
    # Add your custom excludes here
]
```

### Requirements

- Python 3.6+
- No external dependencies required

### Output Format

The generated `output.md` will look like this:

```
# Project Structure

```
├── README.md
├── src/
│   ├── main.py
│   └── utils.py
└── tests/
    └── test_main.py
```

# File Contents

```src/main.py
1 │ def main():
2 │     print("Hello World")
```
