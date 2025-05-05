# LLM Tools

A collection of tools designed to help with using a Large Language Model (LLM) to assist with development and debugging.

## Tools Overview

### 1. Code Tree Generator (`generate.py`)
Scans your project's directory and prints a tree-like structure along with the contents of each file, directly to your terminal. Files and directories matching `.gitignore` rules or custom excludes are skipped.

#### Features
- Prints a clean directory tree structure to stdout (the terminal)
- Includes file contents with line numbers for each non-ignored file
- Respects `.gitignore` rules
- Supports custom path exclusions (see `CUSTOM_EXCLUDES` in `generate.py`)

#### Usage
```bash
python generate.py
```

The output will be displayed in your terminal. (If you wish to save the output to a file, you can redirect it:)

```bash
python generate.py > output/code_tree.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TheSethRose/LLM-Tools.git
cd LLM-Tools
```

2. No additional dependencies required! All tools use Python standard library.

## Output Directory

The output can be saved to the `output/` directory if redirected:
- `output/code_tree.md` - Code tree and file contents (if redirected)

The `output/` directory is git-ignored by default.

## Configuration

### Code Tree Generator
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
- Improve existing tools
- Add more configuration options
- Improve documentation
