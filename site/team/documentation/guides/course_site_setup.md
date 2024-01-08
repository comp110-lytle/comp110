---
title: Course Site Setup
date: 2021-02-25
author:
  - Ezri White
  - Kaki Ryan
  - Chiazo Agina
page: logistics
template: overview
site-branch: team
---

If you have already cloned the team110 repo you can jump to **Install Packages**.

## Clone the team110 Repo

- Go to <https://github.com/comp110-lytle/comp110> and clone the repo by pressing the green code button.

  ![](/static/team/repo-instructions/step_1.png){width=500}

  <!-- > If you can't open this link, you have not been added to the team org on Github. Send your github username to Kris!

- Open the `Team 110.code-workspace` file in VSCODE as a Workspace (don't just open the top-level directory) -->

  ![](/static/team/repo-instructions/step_2.png){width=500}

<!-- - Make sure you're in the `team110` folder in your terminal and the master branch.

  ![](/static/team/repo-instructions/step_3.png){width=500} -->

## Install Packages

Note: You may have done this step before, but there are often new dependencies being added, so make sure to run the command again.

- Update pip by running: `python -m pip install -U pip`.
- Make sure your terminal is in the right directory. If you type `pwd` in the terminal it should print `/Some/Path/.../comp110/code`. If it says something like `/Some/Path/.../comp110`, then try typing `cd code` to navigate into the `code` directory.
- Install required PyPI packages in `requirements.txt` with the following command: `python -m pip install -r requirements.txt`.

## Install Pandoc

In order to run the dev server, pandoc is needed and can be downloaded [here](https://pandoc.org/installing.html). Follow the instructions to download. You may need to restart vscode in order to run the dev server.

## Run the Development Script

- Make sure your terminal is in the `site` directory. If you type `pwd` in the terminal it should print `/Some/Path/.../team110/site`. If you do not see this, trash the terminal and create a new one. Then try typing `cd site` to navigate into the `site` directory.
- In your terminal run: `python -m dev`. If the script runs without any problems you should see "\* Running on <_a-server_>". Command or Control click on the server to open the site in your browser.
- To view any changes you are making, navigate to the file you have changed and reload the page if you do not see your updates.

> Note: When making CSS changes a "hard refresh" will often be needed to view any differences. To do this hold shift while reloading your browser.

## Hotdev script

- An alternative to the normal dev script is `python -m hotdev`. You run this in the exact same directory as the normal script and it mostly works the same.
- The benefit of the `hotdev` script is it enables what is referred to as hot-reload or autoreload. When ever you make markdown or css changes, your browser will refresh on save of file instead of having to be manually reloaded.
- It is reccomended to use this script primarily when trying to finish up organizing and styling a page, or making many CSS changes.
