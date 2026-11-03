# 08 — Remote workflows

## Goal
Understand remotes, fetch, pull, push, and upstream tracking.

## Exercises
1. Inspect remotes with `git remote -v`.
2. Fetch updates without merging them.
3. Compare your branch with its upstream.
4. Push a new branch and set its upstream.
5. Practise pulling with rebase in a personal practice repo.
6. Explain the difference between `fetch`, `pull`, and `push`.
7. Clone your repository into a second local folder and simulate two working copies.

## Commands
```bash
git remote -v
git fetch --all --prune
git branch -vv
git push -u origin <branch>
git pull --rebase
```

## Safety
Never force-push shared work without explicit agreement.
