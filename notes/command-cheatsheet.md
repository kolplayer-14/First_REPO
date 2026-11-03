# Git command cheatsheet

## Inspect
```bash
git status
git log --oneline --graph --decorate --all
git show <commit>
git diff
git diff --staged
git branch -vv
git remote -v
git reflog
```

## Branches and integration
```bash
git switch -c <branch>
git switch <branch>
git merge <branch>
git rebase <branch>
git cherry-pick <commit>
```

## Temporary work and undo
```bash
git stash push -m "message"
git stash list
git stash pop
git revert <commit>
git reset --soft HEAD~1
```

## Remote and release
```bash
git fetch --all --prune
git pull --rebase
git push -u origin <branch>
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

**Rule:** Check `git status` before and after commands that change repository state.
