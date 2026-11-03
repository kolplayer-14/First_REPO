# 03 — Rebase

## Goal
Replay commits on a new base and practise cleaning up local history.

## Exercises
1. Create a feature branch and make two commits.
2. Add a new commit to `main`.
3. Rebase the feature branch onto the updated `main`.
4. Inspect the new commit IDs and explain why they changed.
5. In a disposable branch, run `git rebase -i HEAD~3`.
6. Reorder, reword, squash, or fix up commits.
7. Practise continuing and aborting a rebase.

## Commands to know
```bash
git rebase main
git rebase -i HEAD~3
git rebase --continue
git rebase --abort
```

## Safety
Do not rewrite commits that other people have already based work on unless the team agrees.
