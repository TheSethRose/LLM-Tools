---
description: Review & either complete the current task and start the next one or continue working on the current incomplete task.
---

1. Identify your current task ID (e.g. 1), unless you already have it.
   ```bash
   task-master next
   ```
2. Carefully review the task & each subtask. Compare to the codebase to determine if the request has been completed or not.
   - If it has been completed (verified via the code), continue to mark it done.
   - If it has not been completed, we want to continue working on it.
3. If it has subtasks, mark each done:
   ```bash
   task-master set-status --id=<ID>.1,<ID>.2 --status=done
   ```
4. Mark the parent task done:
   ```bash
   task-master set-status --id=<ID> --status=done
   ```
5. // turbo
   ```bash
   task-master next
   ```
6. Copy the Next Task ID and mark in-progress:
   ```bash
   task-master set-status --id=<ID> --status=in-progress
   ```
7. Open `tasks/<ID>.md` in your editor
