---
title: Bedtime Routine
author:
- Kris Jordan
- Alyssa Lytle
---

Putting a cantankerous course to sleep is a process.

1. Establish semester directory in `zzz`
2. Make copies of: `site`, `.github`, for archive
   (e.g. `cp -r site zzz/<semester-folder>/`)
3. Setup a `code` directory. Setup some of the important children directories of `code`. For course specific things (exercises, quizzes, etc), `git mv` them to the corresponding directory in `zzz`. This way the `code` directory can be clean for the next offering while the files retain their histories.
   *. This is something that could be scripted once the directory structure of `code` settles down.
4. Make a git tag once the course is sound asleep.
 (`git tag -a <semester tag> -m "<message>"`)
