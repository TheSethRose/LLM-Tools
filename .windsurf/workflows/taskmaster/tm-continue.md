---
description: Continue progressing through your current task and its subtasks, marking each as in progress or done as you complete them. Use task-master commands to manage and track your workflow efficiently.
---

1. Get the next task by running: task-master next
2. Note the Task ID shown (replace <ID> with this value in the following steps).
3. View the details and subtasks for this task: task-master show <ID> --with-subtasks
4. If the task <ID> has subtasks:

   - For each subtask (<subID>):
     1. Mark the subtask as in progress: task-master set-status --id=<ID>.<subID> --status=in-progress
     2. Work the subtask.
     3. When finished, mark the subtask as done: task-master set-status --id=<ID>.<subID> --status=done

5. Once all subtasks are complete, or if there are no subtasks:

   - Mark the main task as done: task-master set-status --id=<ID> --status=done

6. If there are no remaining tasks ready to work on (for example, if all current tasks and subtasks are marked done, but the next task is pending or blocked by dependencies):

   - Use task-master list to view all remaining tasks and their statuses.
   - Identify the next task to work on.

7. Otherwise, move on to the next task by running: task-master next
8. Repeat this process to continue working through your tasks and subtasks.
