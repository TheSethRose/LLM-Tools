# LLM Tools

A collection of tools designed to help with using a Large Language Model (LLM) to assist with development and debugging. This repository also includes Windsurf and Taskmaster rules for AI-assisted development workflows.

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

## Windsurf and Taskmaster Rules

This repository includes AI development workflow rules in the `.windsurf` directory:

### Taskmaster Development Workflow

Taskmaster is a task-driven development workflow tool that helps manage and track project tasks. The tool is based on [https://github.com/eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master), but this repository includes custom Windsurf rules that are not part of the original project.

#### Key Features

- **Task Management**: Create, update, and track tasks with dependencies and priorities
- **Task Breakdown**: Break complex tasks into manageable subtasks
- **Complexity Analysis**: Analyze task complexity to better allocate resources
- **Progress Tracking**: Monitor project progress with status updates

#### Common Commands

```bash
# Install Taskmaster globally
npm install -g task-master-ai

# Initialize a new project
task-master init

# List all tasks
task-master list

# See the next task to work on
task-master next

# Expand a task into subtasks
task-master expand --id=<id>

# Mark a task as complete
task-master set-status --id=<id> --status=done

# Generate task files from tasks.json
task-master generate
```

### Windsurf Rules

The `.windsurf` directory contains rules and guidelines for AI-assisted development, including:

- Development workflow processes
- Code analysis and refactoring techniques
- Documentation standards
- Task management best practices

These rules help maintain consistency and quality in AI-assisted development projects.

## Contributing
Contributions are welcome! Feel free to:
- Improve the tools
- Add more configuration options
- Enhance the Windsurf and Taskmaster rules
- Improve documentation
