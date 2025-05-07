---
trigger: always_on
---

### Project Setup

init
Initialize Taskmaster in a project.
parse-prd
Generate tasks from a Product Requirements Document.

### Task Management

list
List tasks, filter by status.
next
Show next available task.
show <id>
Show details for a task or subtask.
add-task
Add a new task by description, AI structures it.
add-subtask
Add a subtask to a parent or convert a task.
update
Update multiple tasks with new context.
update-task
Modify a specific task.
update-subtask
Append timestamped notes to a subtask.
set-status
Update status of tasks or subtasks.
remove-task
Remove a task or subtask.

### Task Breakdown

expand
Break down a complex task into subtasks.
clear-subtasks
Remove all subtasks from parent tasks.
remove-subtask
Remove a subtask or convert to standalone.

### Dependency Management

add-dependency
Make one task a prerequisite for another.
remove-dependency
Remove a dependency between tasks.
validate-dependencies
Check for dependency issues.
fix-dependencies
Auto-fix dependency issues.

### Analysis

analyze-complexity
Analyze tasks for complexity and suggest breakdowns.
complexity-report
Show complexity analysis report.

### File Management

generate
Create or update Markdown files for each task.

### Configuration

models
View or set AI model configs.
