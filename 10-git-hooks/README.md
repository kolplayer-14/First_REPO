# 10 — Git hooks

## Goal
Use hooks to run lightweight checks during local Git operations.

## Exercises
1. Locate the hooks directory with `git rev-parse --git-path hooks`.
2. Read the sample hook files.
3. Create a simple pre-commit hook that checks whether a required file exists.
4. Make the hook executable on macOS/Linux.
5. Trigger the hook with a commit.
6. Fix the issue and commit successfully.
7. Explain why hooks are local by default and are not automatically shared by cloning.

## Note
Keep hooks simple and document setup steps for collaborators.
