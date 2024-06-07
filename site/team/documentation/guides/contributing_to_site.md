---
title: Contributing to the 110 Site
author:
  - Alyssa Lytle
  - Viktorya Hunanyan
page: logistics
template: overview
site-branch: team
---

# Making Contributions to the 110 Site

If you have already set up your [TA profile](/team/documentation/guides/ta_profile.html), you've already done all of these steps! This just generalizes the steps in case you are modifying anything else on the site!

## Create a branch

1. Make sure you're on the main branch (`git checkout main`) and run the command 
    `git pull origin main` 
to get the latest updates.
2. Checkout a new `git` branch. In your terminal run the following command, replacing `branch-name` with a descriptive name, not using any spaces (e.g. `git checkout -b qz01-review-edits`):
    `git checkout -b branch-name`
3. In the terminal type: 
    `git branch`
This will give you all the branches you have created. You should now see the new branch you have created. 

Now you can go ahead and make any edits you want!

## Commit + Push Changes to Branch

1. Now you can add all your changes to stage them for committing! You can use
    `git add path/to/file` to add the file you modified.

2. In the terminal type: 
    `git status`

This will check the changes that we have made are ready to be committed. 

3. Commit your changes! In the terminal type: 
    `git commit -m "Message describing the changes we have made or add"`

4. In the terminal type: 
    `git push origin branch-name`

## Make a Pull Request

1. Open GitHub Pull Requests on the `comp110` repo: https://github.com/comp110-lytle/comp110/pulls
2. You might/should see a notification box: "Your recently pushed branches...". If so select "Compare & Pull Request". If not, select "New Pull Request", and in the Compare branch drop-down select your branch.
3. Scroll through the differences and confirm your latest changes were successfully pushed. If you don't see them, check that you committed everything you expected and pushed to your branch. Select "Create Pull Request".
4. In the description box, briefly describe your branch.
5. On the right-hand sidebar, select your Web Lead as a reviewer.
6. Create pull request!