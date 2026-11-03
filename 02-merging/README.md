# 02 — Merging and conflicts

## Goal
Understand fast-forward merges, three-way merges, and conflict resolution.

## Exercises
1. Create `feature/merge-practice` from `main`.
2. Commit a change on the feature branch.
3. Merge it into `main`; identify whether Git used a fast-forward.
4. Create two branches that edit the same line differently.
5. Merge one branch into the other and resolve the conflict manually.
6. Stage the resolution and complete the merge.

## Inspect
```bash
git status
git diff
git show --stat
git log --oneline --graph --decorate --all
```

## Record
Save the conflict markers you encountered and explain how you chose the final content.
