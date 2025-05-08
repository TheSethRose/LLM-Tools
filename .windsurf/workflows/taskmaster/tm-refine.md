---
description: Analyze complexity and refine upcoming tasks
---

1. // turbo
   ```bash
   task-master analyze-complexity --threshold=7 --research
   ```
2. Review `scripts/task-complexity-report.json` and select high-score tasks
3. For each selected `<ID>`, run:
   ```bash
   task-master expand --id=<ID> --num=5 --research
   ```
4. // turbo
   ```bash
   task-master generate
   ```
5. Review new `tasks/` subtasks and update titles/details as needed
