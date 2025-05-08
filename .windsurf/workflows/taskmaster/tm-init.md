---
description: Initialize a new Taskmaster project and parse PRD
---

1. cd to project root
2. // turbo
   ```bash
   task-master init --yes
   ```
3. Place or update your PRD at `scripts/prd.txt`
4. // turbo
   ```bash
   task-master parse-prd --input=scripts/prd.txt --num-tasks=10
   ```
5. // turbo
   ```bash
   task-master generate
   ```
6. // turbo
   ```bash
   task-master next
   ```
7. Copy the “Next Task” ID and mark in-progress:
   ```bash
   task-master set-status --id=<ID> --status=in-progress
   ```
8. Open `tasks/<ID>.md` in your editor
