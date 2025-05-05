# LLM Tools

A collection of tools designed to help with using a Large Language Model (LLM) to assist with development and debugging.

## Tools Overview

### 1. Code Tree & File Contents Generator (`generate.py`)

Scans your project's directory and writes a Markdown file (`output.md`) containing:
- A tree-like directory structure (skipping files/folders per `.gitignore` and custom excludes)
- For each non-ignored file: a Markdown code block with the file's relative path as the code block language, and each line of the file prefixed with a line number

#### Features
- Outputs to `output.md` in the project root by default
- Prints a clean directory tree structure at the top
- Includes file contents for each file, formatted for easy reading and LLM analysis
- Skips files and folders per `.gitignore` and custom excludes (see `CUSTOM_EXCLUDES` in `generate.py`)
- Automatically ensures `generate.py` and `output.md` are listed in `.gitignore`

#### Usage
```bash
python generate.py
```

You will see:
```
Output written to /path/to/your/project/output.md
```

#### Output Format Example
The generated `output.md` will look like:

```
# Directory Tree
<tree structure here>

```relative/path/to/file.py
 1 │ import os
 2 │ def foo():
 3 │     pass
```
```

Each file is shown as a separate code block, using the relative path as the code block language for clarity.

## Output Directory

The output is saved as `output.md` in the project root. You can rename or move this file as needed. The file is automatically git-ignored.

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TheSethRose/LLM-Tools.git
cd LLM-Tools
```

2. No additional dependencies required! All tools use the Python standard library.

## Configuration

### Code Tree & File Contents Generator
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

## Requirements
- Python 3.6+
- No external dependencies required

## Contributing
Contributions are welcome! Feel free to:
- Improve the tool
- Add more configuration options
- Improve documentation
