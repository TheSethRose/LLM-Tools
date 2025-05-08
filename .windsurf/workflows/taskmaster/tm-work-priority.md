---
description: List and start work on all high-priority tasks
---

1. // turbo
   ```bash
   task-master list --status=pending --with-subtasks
   ```
2. Review the output and note tasks with `Priority: high`
3. For each high-priority `<ID>`, run:
   ```bash
   task-master set-status --id=<ID> --status=in-progress
   ```
4. Open each `tasks/<ID>.md` in your editor to begin work
