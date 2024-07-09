---
title: Using Git and Git Tools
date: 2021-02-25
author:
  - Ezri White
  - Marc Lewis
  - Chiazo Agina
page: logistics
template: overview
site-branch: team
---

## Pulling

Before beginning new work, you should always pull from github to make sure your `team110` repo is up to date. This is important for avoiding merge conflicts and other annoying git problems.

- First, make sure you are on the `master` branch. Type `git branch --show-current` in your terminal. If the output is not master then type `git checkout master`.
- Once you are on master, you should be able to run `git pull` to bring your repo up to date.

## Beginning New Work

Once you have ensured that you have all recent changes pulled, you can create a new branch.

- First, if you are working on `tk110`, type `git checkout tk110` to switch to that branch, and run `git pull origin tk110` to
  bring that branch up to date. Do _not_ switch back to `master` before checking out your new branch below.
- In your terminal type `git checkout -b your-branch-name`. Make sure to choose a name that matches the work you will be doing.
- After running this command you will safely be on a new branch and ready to start your work.

## Making a Commit

After you have finished your work, or at least finished a completed piece of it, you can make a commit! Remember for larger changes it is common to have made multiple commits even before pushing or creating a PR.

Prepare the branch locally by running the following lines of code:

- `cd ..` (this moves you back to the team110 directory)
- `git add .` (this will prepare all your changes to be uploaded to github)
- `git commit -m "<commit message here>"` (a short statement describing what you did)

## Pushing

To save your changes to the `team110` repo on github, prepare for a PR or share your branch with someone you will need to **Push**. Run the following:

- `git push origin <branch-name>` (this uploads your draft to github)

## Making a Pull Request (PR)

If you believe your work is finished and ready for deployment follow these steps!

- Make sure all your commits have been pushed up to the `team110` github repo. If they havent then revisit [this step](/git-guide#Pushing).
- Navigate to the [team repo](https://github.com/comp110/team110) in GitHub and then click on the 'Pull Requests' tab.
- Click 'New Pull Request', select the name of your branch and then click 'Create Pull Request'.
- If you are working on tk110, make sure to select `tk110` as the `base` branch (It is initially marked as `master`).

> Once your PR is created make sure to request the appropriate reviewers.

- For work concerning the site: request Ezri, Claire or Aneka as a reviewer
- For work concerning `tk110`: request Marc
- For work concerning a special project: request your team mates & Kris or Kaki
