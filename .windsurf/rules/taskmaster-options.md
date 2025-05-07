---
trigger: always_on
---

### Project Setup

init
--name Project name
--description Project description
--version Initial version
--skip-install Skip dependency install
--aliases Add shell aliases
--yes, -y Use defaults, skip prompts

parse-prd
--input, -i PRD file (default: sample-prd.txt)
--output, -o Output tasks.json (default: tasks/tasks.json)
--num-tasks, -n Number of top-level tasks
--force Overwrite output
--append Add to existing tasks

### Task Management

list
--status, -s Filter by status
--with-subtasks Include subtasks
--file, -f tasks.json path

next
--file, -f tasks.json path

show <id>
--id, -i Task or subtask ID
--file, -f tasks.json path

add-task
--prompt, -p Task description (required)
--dependencies, -d Prerequisite task IDs
--priority Task priority
--research, -r Use research
--file, -f tasks.json path

add-subtask
--parent, -p Parent task ID (required)
--task-id, -i Existing task to convert
--title, -t Subtask title
--description, -d Subtask description
--details Implementation details
--dependencies Dependency IDs
--status, -s Initial status
--skip-generate Skip file regen
--file, -f tasks.json path

update
--from Task ID to start from (required)
--prompt, -p Explanation of changes (required)
--research, -r Use research
--file, -f tasks.json path

update-task
--id, -i Task ID (required)
--prompt, -p New info (required)
--research, -r Use research
--file, -f tasks.json path

update-subtask
--id, -i Subtask ID (required)
--prompt, -p Info to append (required)
--research, -r Use research
--file, -f tasks.json path

set-status
--id, -i Task/subtask IDs (comma-separated, required)
--status, -s New status (required)
--file, -f tasks.json path

remove-task
--id, -i Task/subtask ID (required)
--yes, -y Skip confirmation
--file, -f tasks.json path

### Task Breakdown

expand
--id, -i Task ID
--all Expand all eligible tasks
--num, -n Target number of subtasks
--research, -r Use research
--prompt, -p Extra context
--force Replace existing subtasks
--file, -f tasks.json path

clear-subtasks
--id, -i Parent task IDs
--all Clear from all tasks
--file, -f tasks.json path

remove-subtask
--id, -i Subtask ID (required)
--convert, -c Convert to standalone
--skip-generate Skip file regen
--file, -f tasks.json path

### Dependency Management

add-dependency
--id, -i Dependent task (required)
--depends-on, -d Prerequisite task (required)
--file, -f tasks.json path

remove-dependency
--id, -i Task to remove from (required)
--depends-on, -d Prerequisite to remove (required)
--file, -f tasks.json path

validate-dependencies
--file, -f tasks.json path

fix-dependencies
--file, -f tasks.json path

### Analysis

analyze-complexity
--output, -o Report file (default: scripts/task-complexity-report.json)
--threshold, -t Complexity threshold (1-10)
--research, -r Use research
--file, -f tasks.json path

complexity-report
--file, -f Report file

### File Management

generate
--output, -o Output directory
--file, -f tasks.json path

### Configuration

models
--set-main Set main model
--set-research Set research model
--set-fallback Set fallback model
--ollama Use custom Ollama model
--openrouter Use custom OpenRouter model
--setup Interactive setup
