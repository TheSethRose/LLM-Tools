---
trigger: always_on
description: Comprehensive reference for Taskmaster MCP tools and CLI commands.
globs: **/*
---

# Taskmaster Tool and Command Reference

This file lists all Taskmaster MCP tools and their CLI equivalents. Use MCP tools for integrations like Windsurf for better performance and structured data. CLI commands are for direct use or fallback.

AI-powered tools: parse_prd, analyze_project_complexity, update_subtask, update_task, update, expand_all, expand_task, add_task.

---

## Initialization and Setup

### 1. Initialize Project

MCP: initialize_project
CLI: task-master init
Sets up Taskmaster config and file structure in the current directory.
Options:
--name, --description, --version, --author, --skip-install, --aliases, -y
Run once at project start.
After init, parse a PRD to generate tasks. Use scripts/example_prd.txt as a template if needed.

### 2. Parse PRD

MCP: parse_prd
CLI: task-master parse-prd [file]
Parses a PRD or requirements file to generate tasks.json.
Options:
-i, -o, -n, -f
Strictly follows PRD requirements, fills gaps, avoids over-engineering.
AI call, may take up to a minute.

---

## AI Model Configuration

MCP: models
CLI: task-master models
View or set AI models for main, research, fallback roles.
Options:
--set-main, --set-research, --set-fallback, --ollama, --openrouter, --setup
Config stored in .taskmasterconfig.
API keys must be in .env (CLI) or .Windsurf/mcp.json (MCP).
Model costs are in dollars.
Do not edit .taskmasterconfig manually.

---

## Task Listing and Viewing

MCP: get_tasks
CLI: task-master list
Lists tasks, filter by status, show subtasks.
Options:
-s, --with-subtasks, -f

MCP: next_task
CLI: task-master next
Shows the next available task based on status and dependencies.

MCP: get_task
CLI: task-master show [id]
Shows details for a task or subtask by ID.

---

## Task Creation and Modification

MCP: add_task
CLI: task-master add-task
Describe a new task, AI structures it.
Options:
-p, -d, --priority, -r, -f
AI call, may take up to a minute.

MCP: add_subtask
CLI: task-master add-subtask
Add a subtask or convert a task to subtask.
Options:
-p, -i, -t, -d, --details, --dependencies, -s, --skip-generate, -f

MCP: update
CLI: task-master update
Update multiple tasks from a given ID based on new context.
Options:
--from, -p, -r, -f
AI call, may take up to a minute.

MCP: update_task
CLI: task-master update-task
Update a specific task or subtask by ID.
Options:
-i, -p, -r, -f
AI call, may take up to a minute.

MCP: update_subtask
CLI: task-master update-subtask
Append timestamped notes to a subtask.
Options:
-i, -p, -r, -f
Review current details before appending.
AI call, may take up to a minute.

MCP: set_task_status
CLI: task-master set-status
Update status of tasks or subtasks.
Options:
-i, -s, -f

MCP: remove_task
CLI: task-master remove-task
Permanently remove a task or subtask.
Options:
-i, -y, -f
Cannot be undone. Cleans up dependencies.

---

## Task Structure and Breakdown

MCP: expand_task
CLI: task-master expand
AI breaks down a task into subtasks.
Options:
-i, -n, -r, -p, --force, -f
Appends by default. AI call, may take up to a minute.

MCP: expand_all
CLI: task-master expand --all
Expand all eligible tasks.
Options:
-n, -r, -p, --force, -f
AI call, may take up to a minute.

MCP: clear_subtasks
CLI: task-master clear-subtasks
Remove all subtasks from parent tasks.
Options:
-i, --all, -f

MCP: remove_subtask
CLI: task-master remove-subtask
Remove a subtask or convert to top-level task.
Options:
-i, -c, --skip-generate, -f

---

## Dependency Management

MCP: add_dependency
CLI: task-master add-dependency
Make one task depend on another.
Options:
-i, -d, -f

MCP: remove_dependency
CLI: task-master remove-dependency
Remove a dependency between tasks.
Options:
-i, -d, -f

MCP: validate_dependencies
CLI: task-master validate-dependencies
Check for dependency issues.
Options:
-f

MCP: fix_dependencies
CLI: task-master fix-dependencies
Auto-fix dependency issues.
Options:
-f

---

## Analysis and Reporting

MCP: analyze_project_complexity
CLI: task-master analyze-complexity
Analyze tasks for complexity, suggest breakdowns.
Options:
-o, -t, -r, -f
AI call, may take up to a minute.

MCP: complexity_report
CLI: task-master complexity-report
Show complexity analysis report.
Options:
-f

---

## File Management

MCP: generate
CLI: task-master generate
Create or update Markdown files for each task.
Options:
-o, -f

---

## Environment Variables and Configuration

Taskmaster uses .taskmasterconfig (project root) for config, managed via task-master models --setup.
Environment variables are only for API keys and some provider endpoints.

API keys (set in .env for CLI, .Windsurf/mcp.json for MCP):
ANTHROPIC_API_KEY
PERPLEXITY_API_KEY
OPENAI_API_KEY
GOOGLE_API_KEY
MISTRAL_API_KEY
AZURE_OPENAI_API_KEY (needs AZURE_OPENAI_ENDPOINT)
OPENROUTER_API_KEY
XAI_API_KEY
OLLANA_API_KEY (needs OLLAMA_BASE_URL)

Endpoints:
AZURE_OPENAI_ENDPOINT
OLLAMA_BASE_URL (default: http://localhost:11434/api)

All other settings (model, tokens, temperature, log level, endpoints) are managed in .taskmasterconfig.

---

For workflow integration, see Development Workflow Guide in .Windsurf/rules/dev_workflow.mdc.

---
