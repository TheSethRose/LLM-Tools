#!/usr/bin/env python3
"""
generate.py

Scans the current directory and prints a tree-like directory structure including
the contents of each file. Files and directories matching the .gitignore rules are skipped.

The output is in two parts:
1. A directory tree (similar to the sample output).
2. For each file (non-ignored), its relative path and content with line numbers.
"""

import os
import fnmatch

# Additional paths to exclude beyond .gitignore
CUSTOM_EXCLUDES = [
    '.devcontainer/',
    '.github/',
    '.vscode/',
    'node_modules/',
]

# ------------------------
# .gitignore parsing
# ------------------------
def load_gitignore(base_dir):
    """Load .gitignore patterns from the base directory.

    Returns a tuple of (ignore_patterns, negative_patterns)
    """
    gitignore_path = os.path.join(base_dir, '.gitignore')
    ignore_patterns = []
    negative_patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                # If pattern begins with !
                if line.startswith('!'):
                    negative_patterns.append(line[1:].strip())
                else:
                    ignore_patterns.append(line)
    return ignore_patterns, negative_patterns

def matches_pattern(rel_path, pattern, is_dir):
    """
    Check if the given file/directory relative path matches a single pattern.
    All paths are converted to Unix style (forward slashes).
    """
    # Normalize to Unix style paths.
    rel_path = rel_path.replace(os.sep, '/')
    pattern = pattern.replace(os.sep, '/')

    # If the pattern ends with a slash, match directories.
    if pattern.endswith('/'):
        # For directories, the pattern without trailing slash should either exactly match
        # or be a prefix.
        if is_dir and (rel_path == pattern[:-1] or rel_path.startswith(pattern)):
            return True
        return False
    else:
        # Otherwise, use fnmatch for wildcard matching.
        return fnmatch.fnmatch(rel_path, pattern)

def is_ignored(rel_path, is_dir, ignore_patterns, negative_patterns):
    """
    Return True if `rel_path` (a file or folder relative to repository root)
    should be ignored based on the .gitignore rules or custom excludes.
    """
    # First check custom excludes
    rel_path_unix = rel_path.replace(os.sep, '/')
    for pattern in CUSTOM_EXCLUDES:
        pattern = pattern.replace(os.sep, '/')
        if pattern.endswith('/'):
            if is_dir and (rel_path_unix == pattern[:-1] or rel_path_unix.startswith(pattern)):
                return True
        else:
            if fnmatch.fnmatch(rel_path_unix, pattern):
                return True

    # Then check gitignore patterns
    ignored = False
    for pat in ignore_patterns:
        if matches_pattern(rel_path, pat, is_dir):
            ignored = True
            break
    for pat in negative_patterns:
        # Negative patterns override the ignore decision
        if matches_pattern(rel_path, pat, is_dir):
            ignored = False
            break
    return ignored

# ------------------------
# Directory scanning and tree printing
# ------------------------
def scan_directory(base_dir, ignore_patterns, negative_patterns, relative=""):
    """
    Scan the directory at base_dir/relative and return a sorted list of entries.
    Each entry is a tuple: (name, relative_path, is_dir)
    """
    full_path = os.path.join(base_dir, relative)
    entries = []
    try:
        for entry in sorted(os.listdir(full_path)):
            entry_rel = os.path.join(relative, entry) if relative else entry
            full_entry = os.path.join(full_path, entry)
            is_dir = os.path.isdir(full_entry)
            if is_ignored(entry_rel, is_dir, ignore_patterns, negative_patterns):
                continue
            entries.append((entry, entry_rel, is_dir))
    except PermissionError:
        # Skip directories that cannot be accessed.
        pass
    return entries

def build_tree_lines(base_dir, relative, ignore_patterns, negative_patterns, prefix=""):
    """
    Recursively build a list of tree lines from base_dir/relative.
    Returns a tuple (tree_lines, file_paths) where:
      - tree_lines is a list of strings representing the tree
      - file_paths is a list of relative file paths for non-ignored files
    """
    items = scan_directory(base_dir, ignore_patterns, negative_patterns, relative)
    total = len(items)
    tree_lines = []
    file_paths = []

    for index, (name, rel_path, is_dir) in enumerate(items):
        connector = "└──" if index == total - 1 else "├──"
        tree_lines.append(prefix + connector + " " + name)
        if is_dir:
            extension = "    " if index == total - 1 else "│   "
            sub_lines, sub_files = build_tree_lines(base_dir, rel_path, ignore_patterns, negative_patterns, prefix + extension)
            tree_lines.extend(sub_lines)
            file_paths.extend(sub_files)
        else:
            file_paths.append(rel_path)
    return tree_lines, file_paths

def print_tree(base_dir, ignore_patterns, negative_patterns):
    """Build the directory tree and return the list of non-ignored file paths."""
    tree_lines, file_paths = build_tree_lines(base_dir, "", ignore_patterns, negative_patterns)
    return tree_lines, file_paths

# ------------------------
# File content printing
# ------------------------
def print_file_contents(file_path):
    """Format the file contents with line numbers enclosed by borders."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        lines = [f"Error reading file: {e}"]

    # Normalize file path: display relative to repository root
    rel_file_path = os.path.relpath(file_path, os.getcwd()).replace(os.sep, '/')
    output_lines = []

    # Create a minimal header with just the filename in a code block
    output_lines.append(f"\n```{rel_file_path}")

    # Add line numbers with minimal formatting
    num_digits = len(str(len(lines)))
    for i, line in enumerate(lines, start=1):
        output_lines.append(f"{str(i).rjust(num_digits)} │ {line.rstrip()}")

    # Close the code block
    output_lines.append("```\n")
    return output_lines

# ------------------------
# Main function
# ------------------------
def main():
    base_dir = os.getcwd()
    ignore_patterns, negative_patterns = load_gitignore(base_dir)

    # Open output file
    with open('output.md', 'w', encoding='utf-8') as outfile:
        # Add a minimal header
        outfile.write("# Project Structure\n\n")

        # Generate and write directory tree
        tree_lines, file_paths = print_tree(base_dir, ignore_patterns, negative_patterns)
        outfile.write("```\n")
        outfile.write("\n".join(tree_lines))
        outfile.write("\n```\n\n")

        # Add a simple section header for file contents
        outfile.write("# File Contents\n")

        # For each non-ignored file, write its path and contents
        for rel_path in file_paths:
            full_path = os.path.join(base_dir, rel_path)
            if os.path.isfile(full_path):
                content_lines = print_file_contents(full_path)
                outfile.write("\n".join(content_lines))

    print("Output written to output.md")

if __name__ == "__main__":
    main()
