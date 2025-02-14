#!/usr/bin/env python3
"""
error_extractor.py

Extracts relevant context around Python errors to help LLMs with debugging.
Features:
1. Parses stack traces
2. Extracts relevant code snippets
3. Includes function definitions and related imports
4. Formats everything in a way that's optimal for LLM analysis
"""

import os
import sys
import traceback
import inspect
import ast
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

class ErrorContextExtractor:
    def __init__(self, project_root: str, context_lines: int = 5):
        self.project_root = Path(project_root)
        self.context_lines = context_lines
        self.analyzed_files: Set[Path] = set()
        self.related_functions: Dict[str, str] = {}

    def extract_traceback(self, error: Exception) -> List[Dict]:
        """Extract information from a traceback."""
        frames = []
        for frame in traceback.extract_tb(error.__traceback__):
            frames.append({
                'filename': frame.filename,
                'line': frame.lineno,
                'function': frame.name,
                'code': frame.line
            })
        return frames

    def get_file_content(self, file_path: str, start_line: int) -> Tuple[List[str], int, int]:
        """Get file content with context around the error line."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            start_idx = max(0, start_line - self.context_lines - 1)
            end_idx = min(len(lines), start_line + self.context_lines)

            return lines[start_idx:end_idx], start_idx + 1, end_idx
        except Exception as e:
            print(f"Error reading file {file_path}: {e}")
            return [], 0, 0

    def find_function_definition(self, file_path: str, function_name: str) -> Optional[Tuple[int, int]]:
        """Find the start and end lines of a function definition."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef) and node.name == function_name:
                    # Handle the case where end_lineno might be None
                    if node.end_lineno is None:
                        # Count lines in the function's body
                        end_line = node.lineno
                        for child in ast.walk(node):
                            if isinstance(child, ast.AST) and hasattr(child, 'lineno'):
                                child_line = getattr(child, 'lineno')
                                end_line = max(end_line, child_line)
                        return node.lineno, end_line
                    return node.lineno, node.end_lineno

        except Exception as e:
            print(f"Error parsing {file_path}: {e}")

        return None

    def analyze_imports(self, file_path: str) -> List[str]:
        """Find all imports in a file."""
        imports = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        imports.append(f"import {name.name}")
                elif isinstance(node, ast.ImportFrom):
                    names = ", ".join(n.name for n in node.names)
                    imports.append(f"from {node.module} import {names}")

        except Exception as e:
            print(f"Error analyzing imports in {file_path}: {e}")

        return imports

    def format_code_context(self, lines: List[str], start_line: int) -> str:
        """Format code context with line numbers."""
        return "\n".join(f"{i} │ {line.rstrip()}"
                        for i, line in enumerate(lines, start_line))

    def generate_error_report(self, error: Exception) -> str:
        """Generate a formatted error report for LLM analysis."""
        frames = self.extract_traceback(error)

        lines = [
            "# Error Analysis Report\n",
            f"## Error Type: {type(error).__name__}",
            f"## Error Message: {str(error)}\n",
            "## Stack Trace Analysis\n"
        ]

        for i, frame in enumerate(frames, 1):
            file_path = frame['filename']
            lines.append(f"### Frame {i}: {os.path.basename(file_path)}")
            lines.append(f"Function: {frame['function']}")
            lines.append(f"Line: {frame['line']}\n")

            # Get code context
            content, start, end = self.get_file_content(file_path, frame['line'])
            if content:
                lines.append("#### Code Context:")
                lines.append("```python")
                lines.append(self.format_code_context(content, start))
                lines.append("```\n")

            # Get function definition
            if frame['function'] != '<module>':
                func_lines = self.find_function_definition(file_path, frame['function'])
                if func_lines:
                    start, end = func_lines
                    content, _, _ = self.get_file_content(file_path, start)
                    if content:
                        lines.append("#### Complete Function Definition:")
                        lines.append("```python")
                        lines.append(self.format_code_context(content, start))
                        lines.append("```\n")

            # Get imports
            if file_path not in self.analyzed_files:
                self.analyzed_files.add(Path(file_path))
                imports = self.analyze_imports(file_path)
                if imports:
                    lines.append("#### File Imports:")
                    lines.append("```python")
                    lines.extend(imports)
                    lines.append("```\n")

        return "\n".join(lines)

def main():
    # Example usage
    try:
        # Your code that might raise an exception
        raise ValueError("Example error for demonstration")
    except Exception as e:
        extractor = ErrorContextExtractor(os.getcwd())
        report = extractor.generate_error_report(e)

        # Save the report
        output_file = Path("output") / "error_context.md"
        output_file.parent.mkdir(exist_ok=True)

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"Error analysis saved to {output_file}")

if __name__ == "__main__":
    main()
