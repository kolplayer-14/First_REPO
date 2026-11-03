# Advanced Git Learning

A hands-on repository for learning Git beyond the basic `add`, `commit`, and `push` workflow.

## Learning goals

By completing the exercises here, you should be able to:
- Create, rename, compare, and delete branches safely.
- Merge branches and resolve conflicts.
- Rebase and use interactive rebase to clean up local history.
- Cherry-pick selected commits.
- Use stash, reflog, reset, and revert appropriately.
- Understand Git objects and inspect repository history.
- Work with remotes, upstream branches, tags, and releases.
- Use Git hooks and a pull-request workflow.

## Repository map

| Folder | What to practise |
|---|---|
| `01-branching/` | Branch creation, switching, tracking, deletion |
| `02-merging/` | Fast-forward, three-way merge, conflict resolution |
| `03-rebase/` | Rebase and interactive rebase |
| `04-cherry-pick/` | Apply selected commits |
| `05-stash-reflog/` | Save work temporarily and recover references |
| `06-reset-revert/` | Understand safe and destructive history changes |
| `07-git-internals/` | Objects, HEAD, index, and refs |
| `08-remote-workflows/` | Fetch, pull, push, upstream, and remote branches |
| `09-tags-releases/` | Annotated tags and release workflow |
| `10-git-hooks/` | Local automation with hooks |
| `11-real-world-workflows/` | Feature branches and pull requests |

## Suggested order

Follow the numbered folders. Read the task, perform it in a temporary practice repository, and record the commands and observations in that folder.

## Safety rules

- Practise destructive commands in a disposable repository first.
- Before using `reset --hard`, confirm that you do not need the uncommitted work.
- Prefer `revert` for undoing commits that have already been shared.
- Never force-push to a shared branch unless the team has explicitly agreed.
- Use `git status` and `git log --oneline --graph --decorate --all` frequently.

## Useful inspection commands

```bash
git status
git log --oneline --graph --decorate --all
git diff
git diff --staged
git show <commit>
git branch -vv
git remote -v
git reflog
```

## Progress tracker

- [ ] 01 — Branching
- [ ] 02 — Merging and conflicts
- [ ] 03 — Rebase
- [ ] 04 — Cherry-pick
- [ ] 05 — Stash and reflog
- [ ] 06 — Reset and revert
- [ ] 07 — Git internals
- [ ] 08 — Remote workflows
- [ ] 09 — Tags and releases
- [ ] 10 — Git hooks
- [ ] 11 — Real-world workflows

**Learning rule:** do the command yourself before reading a solution. Keep a short note of what changed in the repository after each command.
