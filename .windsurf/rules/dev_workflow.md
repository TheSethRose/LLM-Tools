---
trigger: always_on
description: Guide for using Task Master to manage task-driven development workflows
globs: **/*
---

# Task Master Development Workflow

This guide summarizes how to use Task Master for software development project management. To fit within a 6000-character limit, some details are moved to taskmaster-advanced.md and taskmaster-fields.md.

## Interaction: MCP Server vs CLI

Task Master can be used via:

1. MCP Server (for AI agents, IDEs like Windsurf)
    - Exposes tools such as get_tasks, add_subtask.
    - Offers structured data, better performance, richer error handling.
    - See mcp.mdc and taskmaster.mdc for tool/command mapping.
    - Restart MCP server after changes to scripts/modules or tool definitions.

2. CLI (for users, fallback)
    - Use task-master command in terminal.
    - Install globally (npm install -g task-master-ai) or use npx.
    - CLI commands mirror MCP tools (e.g., task-master list = get_tasks).
    - See taskmaster.mdc for command reference.

## Standard Workflow

- Initialize: Run initialize_project/tool or task-master init, or parse_prd/task-master parse-prd --input='<prd-file.txt>' to create tasks.json.
- List tasks: get_tasks/task-master list.
- Find next task: next_task/task-master next.
- Analyze complexity: analyze_project_complexity/task-master analyze-complexity --research.
- Review complexity: complexity_report/task-master complexity-report.
- Select tasks: Based on dependencies (all done), priority, ID.
- Clarify: Check tasks/ directory or ask user.
- Show task: get_task/task-master show <id>.
- Expand tasks: expand_task/task-master expand --id=<id> [--force] [--research].
- Clear subtasks: clear_subtasks/task-master clear-subtasks --id=<id>.
- Implement code per task details and dependencies.
- Verify: Use test strategies before marking done (see tests.mdc).
- Mark done: set_task_status/task-master set-status --id=<id> --status=done.
- Update tasks: update/task-master update --from=<id> --prompt="..." or update_task/task-master update-task --id=<id> --prompt="...".
- Add tasks: add_task/task-master add-task --prompt="..." [--research].
- Add subtasks: add_subtask/task-master add-subtask --parent=<id> --title="...".
- Append notes: update_subtask/task-master update-subtask --id=<subtaskId> --prompt='...'.
- Generate files: generate/task-master generate.
- Manage dependencies: add_dependency/remove_dependency tools or commands, validate_dependencies/fix_dependencies.
- Respect dependency chains and priorities.
- Report progress: get_tasks/task-master list.

## Task Complexity and Breakdown

- Run analyze_project_complexity/task-master analyze-complexity --research.
- Review with complexity_report/task-master complexity-report.
- Focus on high-complexity tasks (score 8-10).
- Use expand_task/task-master expand --id=<id> [--num=<n>] [--research] [--force] [--prompt="..."].
- Use expand_all/task-master expand --all for batch expansion.
- Clear subtasks first if full replacement needed.

## Implementation Drift

- If implementation diverges from plan or new dependencies arise:
    - update/task-master update --from=<futureTaskId> --prompt='...' [--research] for multiple tasks.
    - update_task/task-master update-task --id=<taskId> --prompt='...' [--research] for one task.

## Task Status

- pending: ready to work
- done: completed and verified
- deferred: postponed
- Custom statuses allowed

## Configuration

- .taskmasterconfig (project root): Main config (models, params, logging, etc). Use task-master models --setup. Do not edit manually.
- Environment variables (.env or .Windsurf/mcp.json): Only for API keys and endpoints. CLI uses .env, MCP uses mcp.json env section.
- Non-API settings (models, MAX_TOKENS, LOG_LEVEL) are not in env vars.
- If AI commands fail, check API key in correct location.

## Next Task

- Use next_task/task-master next.
- Shows tasks with dependencies satisfied, prioritized by priority, dependency count, ID.
- Displays details, subtasks, suggested actions.
- Ensures correct sequence and dependency respect.

## Viewing Task Details

- Use get_task/task-master show <id> (dot notation for subtasks).
- Shows all info for task or subtask, including parent/child relationships and suggested actions.

## Managing Dependencies

- add_dependency/task-master add-dependency --id=<id> --depends-on=<id>
- remove_dependency/task-master remove-dependency --id=<id> --depends-on=<id>
- Prevents circular/duplicate dependencies.
- Regenerates task files after changes.
- Visualizes dependencies with status indicators.

## Iterative Subtask Implementation

1. Understand: get_task/task-master show <subtaskId> to review requirements.
2. Plan: Explore codebase, identify files/lines to change, gather all details.
3. Log: update_subtask/task-master update-subtask --id=<subtaskId> --prompt='<plan>'.
4. Verify: get_task/task-master show <subtaskId> to confirm plan is logged.
5. Implement: set_task_status/task-master set-status --id=<subtaskId> --status=in-progress, then code.
6. Refine: Regularly update_subtask/task-master update-subtask --id=<subtaskId> --prompt='<progress>\n- What worked\n- What did not work', logging findings, code snippets, decisions, deviations.
7. Review rules: After completion, update rules as needed.
8. Mark done: set_task_status/task-master set-status --id=<subtaskId> --status=done.
9. Commit: git add ., git commit -m 'feat: Implement subtask <subtaskId> ...', run changeset if needed.
10. Next: Use next_task/task-master next.

## Code Analysis

- To find exported functions/constants: rg "export (async function|function|const) w+".
- Useful for module structure, refactoring, migration, or naming conflicts.

For advanced details and full task field definitions, see taskmaster-advanced.md and taskmaster-fields.md.

This workflow is a guideline. Adapt as needed for your project and team.
