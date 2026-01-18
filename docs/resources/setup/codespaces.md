---
title: CodeSpaces
author:
  - Kris Jordan
page: resource
template: overview
navbar: base
---

## CodeSpaces when Software Setup or Computers Fail

If Software Setup is failing on a laptop or a computer has failed, is off for replacement or repair, and you want to avoid a loss of continuity to work, it is possible to continue work thanks to GitHub Codespaces, a closely related feature to VSCode DevContainers.

## Setting up a Codespace

Your workspace must be setup and at least one successful "backup push" to GitHub is made. Please be sure you have completed the software installation and workspace installation up to the point of steps 1 through 5 in [Workspace Repository Setup](/resources/setup/workspace.html).

## Open your GitHub Repository

In GitHub, navigate to your personal repository for backing up your workspace. It should have a URL that is of the format:

`https://github.com/26s-comp110/comp-110-workspace-KrisJordan` or `https://github.com/comp110-26s/comp-110-workspace-KrisJordan` (except instead of `KrisJordan` you will see your GitHub username)

## Create a Codespace

1. Click the Green 'Code' Button. Click "Create Codespace on Main".
2. This will open up a Github Codespace that is very similar to a VSCode Dev Container. It will take about a minute to start up. Please wait for any "working" badges in the sidebar and bottom status bar to complete before continuing.
3. After it has started up successfully, you should be able to start Trailhead in the manner shown in class / exercises, however, there will be a difference in how you access it. You will need to switch to the "Ports" tab at the bottom (or use command palette to View Ports) and find port 1110 listed (it will take a second to complete setup the first time, wait until the "No forwarded ports." message disappears). Hover over the "Forwarded Address" for this row and click the globe icon. This will open up a tab to the location you can use to access Trailhead (this is the key difference versus a DevContainer). *The tab will open an "error" page. That's ok! When you start up your trailhead, you can go back and refresh this page!*
4. Go back to the Codespace tab in your browser (the tab that looks like VS Code)  and start your trailhead! Press the debug button on the left (the little play button with a bug on it), then a little play button should appear in the top left that has “start trailhead” next to it. Click that play button. Give it a few seconds, then go back to the error page you were seeing and refresh. Your trailhead should appear! 
5. You can now use the CodeSpace just the same as VSCode with two important, additional differences: saving/backing up your work and stopping a working session. Please continue to learn how these work.

## Backing Up Your Work

Because a CodeSpace is stored in the GitHub Cloud, your changes are not stored on your computer. You should frequently back up your work, just like we show in exercises: after changes you'd like to save are made, go to the Source Code View (sidebar icon with three circles connected by lines), hover over the files you'd like to back up, enter a message in the message box, then click the Commit Button. Finally, click the elipses button at the top of the sidebar, select "Push" to back your work up.

## Stopping Work

When your Codespace is active, you are making use of a computer in the cloud that is running to keep your workspace available. When you are done, please Stop the Codespace by clicking in the lower left hand corner of the screen and selecting "Stop Codespace" (also possible via the command palette).

## Coming Back to a Codespace

When you are ready to resume work, navigate back to your GitHub backup repository (above). Click the Green code button, under the Codespaces tab you will see the random name given to your prior code space under "on current branch". Click this link and your Codespace will reopen (you may need to click the button "Restart Codespace".) Reopening a code space is faster than setting one up for the first time.

## Creating a Submission for Autograding

You can follow an exercises' instructions for autograding purposes. After you generate a submission file, though, you will need to download it from your Codespace. This is one extra step versus a standard Dev Container. Once you have generated a submission, go back to your File Explorer tab in your Codespace. Find the zip file generated. Right click on it and select "Download..." and you will now have a zip file in your Downloads directory that can be uploaded to Gradescope for autograding.

## Final Notes

We strongly encourage continuing to try and get Docker + Dev Containers successfully running on your laptop. Continue working with the UTAs and Kris to make it happen. In the interim, GitHub Codespaces will allow you to stay on track for the course using 99.9% the same tools in Dev Containers, with a few minor differences and extra steps for various tasks.