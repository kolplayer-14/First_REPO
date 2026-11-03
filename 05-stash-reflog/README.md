# 05 — Stash and reflog

## Goal
Temporarily save uncommitted work and recover references after mistakes.

## Exercises
1. Modify a tracked file without committing.
2. Save it with `git stash push -m "practice work"`.
3. Inspect `git stash list` and `git stash show -p`.
4. Apply the stash, then repeat using `pop`.
5. Create and move between several commits.
6. Inspect `git reflog` and identify an earlier HEAD position.
7. In a disposable repository, recover a commit that is no longer on the branch tip.

## Commands
```bash
git stash
git stash list
git stash apply
git stash pop
git reflog
```

## Record
Explain the difference between `apply` and `pop`.
