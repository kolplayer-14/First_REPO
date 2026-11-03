# 07 — Git internals

## Goal
Understand the object database, index, refs, and HEAD.

## Exercises
1. Run `git cat-file -t HEAD` and `git cat-file -p HEAD`.
2. Inspect a commit, tree, and blob with `git cat-file`.
3. Run `git hash-object` on a sample file.
4. Compare the working tree, staging area, and latest commit.
5. Inspect `.git/HEAD`, `.git/refs`, and `.git/objects` (do not edit them manually).
6. Explain what a branch name points to.

## Commands
```bash
git cat-file -t <object>
git cat-file -p <object>
git hash-object <file>
git ls-files
git rev-parse HEAD
```
