# LLM Tools

A collection of tools designed to help with using a Large Language Model (LLM) to assist with development and debugging.

## Tools Overview

### 1. Code Tree Generator (`generate.py`)
Creates a Markdown file containing your project's directory structure and file contents in a format optimized for LLM analysis.

#### Features
- Generates a clean directory tree structure
- Includes file contents with line numbers
- Respects `.gitignore` rules
- Supports custom path exclusions

#### Usage
```bash
python generate.py
```

Output will be saved to `output/code_tree.md`

### 2. Dependency Analyzer (`dependency_analyzer.py`)
Analyzes Python project dependencies and creates a formatted report for LLM review.

#### Features
- Maps all internal module relationships
- Lists external package dependencies
- Parses requirements.txt for version information
- Creates a clean, hierarchical dependency report

#### Usage
```bash
python dependency_analyzer.py
```

Output will be saved to `output/dependencies.md`

### 3. Error Context Extractor (`error_extractor.py`)
Extracts relevant context around Python errors to help LLMs with debugging.

#### Features
- Captures full stack traces
- Shows code context around each error
- Includes complete function definitions
- Lists relevant imports
- Formats everything for optimal LLM analysis

#### Usage
To analyze a specific error, modify the example in `main()`:

```python
# In error_extractor.py
def main():
    try:
        # Your code that might raise an exception
        result = some_function()  # Replace with your code
    except Exception as e:
        extractor = ErrorContextExtractor(os.getcwd())
        report = extractor.generate_error_report(e)
        # Report is saved to output/error_context.md
```

Or import and use in your code:

```python
from error_extractor import ErrorContextExtractor

try:
    # Your code that might raise an exception
    result = some_function()
except Exception as e:
    extractor = ErrorContextExtractor(os.getcwd())
    report = extractor.generate_error_report(e)
    # Use the report or save it
    with open("output/error_context.md", "w") as f:
        f.write(report)
```

Output will be saved to `output/error_context.md`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/TheSethRose/LLM-Tools.git
cd LLM-Tools
```

2. No additional dependencies required! All tools use Python standard library.

## Output Directory

All tools save their output to the `output/` directory:
- `output/code_tree.md` - Code tree and file contents
- `output/dependencies.md` - Dependency analysis
- `output/error_context.md` - Error context and stack traces

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

### Error Context Extractor
You can adjust the number of context lines shown around errors:

```python
# Show more context lines around errors
extractor = ErrorContextExtractor(os.getcwd(), context_lines=10)
```

## Requirements
- Python 3.6+
- No external dependencies required

## Contributing
Contributions are welcome! Feel free to:
- Add new tools
- Improve existing tools
- Add more configuration options
- Improve documentation
