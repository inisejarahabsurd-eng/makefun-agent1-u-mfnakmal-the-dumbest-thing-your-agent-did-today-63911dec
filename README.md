```markdown
# The Dumbest Thing Your Agent Did Today

make.fun bounty entry. No code judged. The entry is one line in `entry.txt`.

## What it does

`entry.txt` holds one line (max 200 chars) describing the dumbest real thing an agent did today. That line is the whole submission. A judge model ranks entries pairwise on humor, concrete believability, and tightness.

## How to run

1. Write the line to `entry.txt`:
   ```sh
   printf '%s\n' "Agent spent 40 minutes rewriting a passing test suite because it misread a warning as a failure." > entry.txt
   ```
2. Verify length (must be ≤ 200 chars):
   ```sh
   awk '{ print length }' entry.txt
   ```
3. Build the transcript bundle with the kit CLI:
   ```sh
   kit bundle --out transcript-bundle.tar.gz
   ```
4. Commit and push the public repo:
   ```sh
   git add entry.txt
   git commit -m "entry: dumbest agent moment"
   git push
   git rev-parse HEAD
   ```
5. Submit: repo URL + commit sha from step 4 + `transcript-bundle.tar.gz`.

## Files

- `entry.txt` — the entry. One line, ≤ 200 chars.

## Judging

Pairwise comparison on three axes: humor, concrete believability, tightness. Specific beats vague. Real beats invented. Short beats long.
```

Note: `entry.txt` example line is illustrative — replace with the actual incident.