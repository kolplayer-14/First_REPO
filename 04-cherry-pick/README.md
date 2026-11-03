# 04 — Cherry-pick

## Goal
Apply one specific commit from another branch.

## Exercises
1. Create branches `feature/a` and `feature/b`.
2. Make two commits on `feature/a`.
3. Copy the SHA of the second commit.
4. Switch to `feature/b` and cherry-pick that commit.
5. Inspect the new commit and compare its SHA with the original.
6. Practise resolving a cherry-pick conflict.
7. Practise `git cherry-pick --abort` in a disposable repo.

## Commands
```bash
git log --oneline
git show <commit>
git cherry-pick <commit>
git cherry-pick --continue
```
