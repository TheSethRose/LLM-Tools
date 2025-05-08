---
description: Streamlined Git workflow for committing and pushing changes with proper conventions
---

# Git Workflow Assistant

I'll help you commit and push your changes to GitHub following proper conventions and best practices. This workflow ensures clean commits with meaningful messages and proper branch handling, aligned with modern development practices.

## Pre-Commit Preparation

1. **Verify Current Branch** - Make sure you're on the correct branch before making changes:

   ```bash
   git branch  # Shows all local branches with current branch marked with *
   ```

2. **Check Repository Status** - Review all modified, added, and deleted files:

   ```bash
   git status
   ```

3. **Review Changes** - Examine the specific changes you've made:
   ```bash
   git diff                 # Shows unstaged changes
   git diff --staged        # Shows staged changes ready to commit
   ```

## Optimized Commit Process

1. **Stage Changes** - Add modified files to the staging area:

   ```bash
   git add .               # Add all changes (use with caution)
   git add <file-path>     # Add specific files (preferred for precision)
   git add -p              # Interactively choose which chunks to stage
   ```

2. **Commit with Conventional Format** - Follow the standardized commit message pattern:

   ```bash
   git commit -m "type(scope): concise description

   - Detailed change #1
   - Detailed change #2
   - Related to task #123"
   ```

   **Commit Types Reference**:

   - `feat`: New feature or functionality
   - `fix`: Bug fix
   - `docs`: Documentation changes
   - `style`: Formatting, white-space, styling (no code change)
   - `refactor`: Code restructuring (no feature/behavior change)
   - `perf`: Performance improvements
   - `test`: Adding/updating tests
   - `build`: Build system or dependency changes
   - `ci`: CI configuration changes
   - `chore`: Maintenance tasks

3. **Amend Last Commit** - Fix mistakes in your most recent commit (before pushing):
   ```bash
   git commit --amend -m "type(scope): corrected message"  # Change message
   git commit --amend --no-edit                           # Add staged files to last commit
   ```

## Syncing with Remote Repository

1. **Fetch Remote Changes** - Retrieve updates without merging:

   ```bash
   git fetch origin
   ```

2. **Pull with Rebase** - Get updates and apply your changes on top (prevents merge commits):

   ```bash
   git pull --rebase origin <branch-name>
   ```

3. **Push Changes** - Send your commits to GitHub:

   ```bash
   git push origin <branch-name>
   ```

4. **Handle Push Rejection** - If push is rejected due to remote changes:
   ```bash
   git pull --rebase origin <branch-name>  # Update your branch
   git push origin <branch-name>           # Try pushing again
   ```

## Branch Management

1. **Create & Switch to New Branch** (branching from current branch):

   ```bash
   git checkout -b feature/new-feature-name
   ```

2. **List All Branches**:

   ```bash
   git branch -a  # Shows local and remote branches
   ```

3. **Switch Between Branches**:

   ```bash
   git checkout <branch-name>
   ```

4. **Delete Local Branch** (after merging):
   ```bash
   git branch -d <branch-name>  # Safe delete (prevents deleting unmerged work)
   ```

## Quick Commit & Push Workflow

I can streamline your Git workflow with a single command. Just provide a brief description, and I'll:

1. Check status to show what will be committed
2. Stage all changes
3. Create a properly formatted commit message
4. Pull the latest changes with rebase
5. Push to the current branch

Example:

```
/git "feat(auth): implement GitHub OAuth redirect flow"
```

## Best Practices & Safety Measures

- **One Logical Change Per Commit** - Keep commits focused and reviewable
- **Descriptive Commit Messages** - Clearly explain what and why, not how
- **Task References** - Include task/issue IDs in commit messages
- **Pull Before Push** - Always get latest changes before pushing to avoid conflicts
- **Regular Pushing** - Push changes regularly to prevent data loss
- **Branch Naming** - Use descriptive prefixes like `feature/`, `fix/`, `docs/`
- **Stash Uncommitted Changes** - Before switching branches: `git stash` and `git stash pop`

I'll guide you step-by-step through this workflow to ensure your changes are properly tracked, committed, and pushed to GitHub while following software engineering best practices.
