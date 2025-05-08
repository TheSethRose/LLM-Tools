---
trigger: always_on
---

### Task-Master Commands

#### Project Setup & Configuration

init
Initialize a new Taskmaster project. Options: `--name=<name>`, `--description=<desc>`, `-y` (skip prompts).

models
View current AI model configuration and available models.

models --setup
Run interactive setup to configure AI models.

models --set-main <model_id>
Set the primary model for task generation.

models --set-research <model_id>
Set the model for research operations.

models --set-fallback <model_id>
Set the fallback model (optional).

#### Task Generation

parse-prd --input=<file.txt> [--num-tasks=10]
Generate tasks from a Product Requirements Document (PRD).

generate
Create or update Markdown files for each task from `tasks.json`.

#### Task Management

list [--status=<status>] [--with-subtasks]
List all tasks, optionally filter by status or include subtasks.

set-status --id=<id> --status=<status>
Update the status of a task or subtask (e.g., done, pending).

update --from=<id> --prompt="<context>"
Update multiple tasks based on new requirements or context.

update-task --id=<id> --prompt="<context>"
Update a specific task with new information.

update-subtask --id=<parentId.subtaskId> --prompt="<context>"
Append timestamped notes or context to a subtask.

add-task --prompt="<text>" [--dependencies=<ids>] [--priority=<priority>]
Add a new task using AI to structure it, with optional dependencies and priority.

remove-task --id=<id> [-y]
Remove a task or subtask permanently.

#### Subtask Management

add-subtask --parent=<id> --title="<title>" [--description="<desc>"]
Add a new subtask to a parent task.

add-subtask --parent=<id> --task-id=<id>
Convert an existing task into a subtask under a parent.

remove-subtask --id=<parentId.subtaskId> [--convert]
Remove a subtask or convert it to a standalone task.

clear-subtasks --id=<id>
Remove all subtasks from the specified parent task.

clear-subtasks --all
Remove all subtasks from all tasks.

#### Task Analysis & Breakdown

analyze-complexity [--research] [--threshold=5]
Analyze tasks for complexity and suggest breakdowns.

complexity-report [--file=<path>]
Show the complexity analysis report.

expand --id=<id> [--num=5] [--research] [--prompt="<context>"]
Break down a complex task into detailed subtasks.

expand --all [--force] [--research]
Expand all pending tasks with subtasks.

#### Task Navigation & Viewing

next
Show the next available task to work on, considering dependencies.

show <id>
Display detailed information about a specific task or subtask.

#### Dependency Management

add-dependency --id=<id> --depends-on=<id>
Make one task a prerequisite for another.

remove-dependency --id=<id> --depends-on=<id>
Remove a dependency between tasks.

validate-dependencies
Check for invalid or circular dependencies.

fix-dependencies
Automatically fix detected dependency issues.

#### File & API Configuration

.taskmasterconfig
AI model configuration file (managed by `models` command).

API Keys (.env)
API keys for AI providers (e.g., ANTHROPIC_API_KEY) required in `.env`.

MCP Keys (mcp.json)
API keys for Cursor integration, required in `.cursor/`.
