#!/usr/bin/env python3
"""
dependency_analyzer.py

Analyzes Python project dependencies and creates a formatted report suitable for LLM analysis.
This includes:
1. Direct imports in each file
2. Package dependencies from requirements.txt/setup.py
3. Internal module relationships
4. Dependency graph in a clean, formatted output
"""

import os
import ast
import re
from pathlib import Path
from typing import Dict, List, Set, Tuple

class DependencyAnalyzer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.internal_modules: Set[str] = set()
        self.external_deps: Dict[str, Set[str]] = {}
        self.module_relationships: Dict[str, Set[str]] = {}
        self.requirements: Dict[str, str] = {}

    def parse_requirements(self) -> None:
        """Parse requirements.txt if it exists."""
        req_file = self.project_root / "requirements.txt"
        if req_file.exists():
            with open(req_file, "r") as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        # Handle version specifiers
                        parts = re.split(r'[=<>~]', line)
                        package = parts[0].strip()
                        version = parts[1].strip() if len(parts) > 1 else "latest"
                        self.requirements[package] = version

    def analyze_file(self, file_path: Path) -> Tuple[Set[str], Set[str]]:
        """Analyze imports in a single Python file."""
        internal_imports = set()
        external_imports = set()

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                tree = ast.parse(f.read())

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for name in node.names:
                        module = name.name.split(".")[0]
                        if self._is_internal_module(module):
                            internal_imports.add(name.name)
                        else:
                            external_imports.add(module)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        module = node.module.split(".")[0]
                        if self._is_internal_module(module):
                            internal_imports.add(node.module)
                        else:
                            external_imports.add(module)

        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")

        return internal_imports, external_imports

    def _is_internal_module(self, module: str) -> bool:
        """Check if a module is internal to the project."""
        return any(
            (self.project_root / path).exists()
            for path in [
                f"{module}.py",
                str(Path(module).joinpath("__init__.py")),
            ]
        )

    def analyze_project(self) -> None:
        """Analyze the entire project directory."""
        self.parse_requirements()

        for file_path in self.project_root.rglob("*.py"):
            if any(part.startswith(".") for part in file_path.parts):
                continue

            rel_path = file_path.relative_to(self.project_root)
            module_name = str(rel_path.with_suffix("")).replace(os.sep, ".")

            internal, external = self.analyze_file(file_path)

            self.internal_modules.add(module_name)
            self.external_deps[module_name] = external
            self.module_relationships[module_name] = internal

    def generate_report(self) -> str:
        """Generate a formatted report for LLM analysis."""
        lines = ["# Project Dependency Analysis\n"]

        # Package Dependencies
        lines.append("## External Package Dependencies\n")
        if self.requirements:
            lines.append("From requirements.txt:")
            for package, version in sorted(self.requirements.items()):
                lines.append(f"- {package} (version: {version})")
        lines.append("")

        # Module Dependencies
        lines.append("## Module Dependencies\n")
        for module in sorted(self.internal_modules):
            lines.append(f"### {module}")

            if self.external_deps[module]:
                lines.append("\nExternal imports:")
                for dep in sorted(self.external_deps[module]):
                    lines.append(f"- {dep}")

            if self.module_relationships[module]:
                lines.append("\nInternal imports:")
                for dep in sorted(self.module_relationships[module]):
                    lines.append(f"- {dep}")

            lines.append("")

        return "\n".join(lines)

def main():
    # Use current directory as project root
    analyzer = DependencyAnalyzer(os.getcwd())
    analyzer.analyze_project()

    # Generate and save report
    report = analyzer.generate_report()
    output_file = Path("output") / "dependencies.md"
    output_file.parent.mkdir(exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Dependency analysis saved to {output_file}")

if __name__ == "__main__":
    main()
