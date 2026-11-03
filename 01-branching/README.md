# 01 — Branching

## Exercises

1. Create a branch named `feature/profile`.
2. Switch to it and add a file named `profile.txt`.
3. Make three separate commits with meaningful messages.
4. Rename the branch to `feature/user-profile`.
5. Create a second branch from `main` and compare the two branches.
6. Inspect local and remote tracking branches with `git branch -vv`.
7. Delete a merged local branch, then practise deleting a remote branch in a test repository.

## Commands to understand

```bash
git switch -c feature/profile
git switch main
git branch -m feature/profile feature/user-profile
git branch -vv
git diff main...feature/user-profile
git branch -d feature/user-profile
```

Explain in your notes the difference between `git switch` and `git checkout`.
