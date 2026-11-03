# 06 — Reset and revert

## Goal
Choose the correct way to undo changes without losing work accidentally.

## Exercises
1. Create three commits in a disposable repository.
2. Compare `git reset --soft HEAD~1`, `--mixed`, and `--hard`.
3. Inspect the working tree and staging area after each reset mode.
4. Undo a commit with `git revert <commit>`.
5. Explain why revert is generally safer for shared history.

## Commands
```bash
git status
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
git revert <commit>
```

## Safety
Only use `reset --hard` in a disposable practice repo. It can permanently discard uncommitted work.
