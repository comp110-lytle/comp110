---
title: Common Issues with Software
author:
  - Kris Jordan
page: resource
template: overview
navbar: base
---

## Common Symptoms

### VSCode: Docker returned an error. Make sure the Docker daemon is running...

If you open up VSCode and see this error message, it means that your Docker Desktop program is not running. Start Docker Desktop, give it a minute to begin after starting it, then retry opening the Dev Container in VSCode.

### VSCode: An error occurred setting up the container

To fix this issue, follow the instructions of [Common Fix: Resetting the Container](#resetting-the-container).

### Trailhead: Error in loading `welcome.py`

If you load the `welcome` module in Trailhead and see an error, the first step is to make sure your VSCode is up-to-date and reloaded. With VSCode open, open the command palette and search for "Code: Check for Updates". If updates are available, install them. After they are installed. Fully close and exit VSCode, then reopen it. Try again.

If the error continues, look in the bottom-right corner of the VSCode window with `welcome.py` open and look for "Python 3.12.1". If you see an earlier version of Python listed, like 3.9 or 3.10, click on the version and a list of versions should pop-up. From here, select the recommended 3.12.1 version.

If the error continues, finally try the [Common Fix: Resetting the Container](#resetting-the-container).

### VSCode: Remote Extension Host terminated unexpectedly (macOS)

If you are on a Mac, especially an Intel-based Mac, you may be experiencing crashes to internal components of VSCode due to a new Apple framework breaking compatibility with Intel-based Macs. The good news is, the fix is pretty straightforward, please follow the steps in the fix [macOS Intel - Disable VirtioFS and Virtualization Framework](#macos-intel---disable-virtiofs-and-virtualization-framework).

## Common Fixes

### Resetting the Container

Many issues involve resetting your DevContainer. This does not risk losing any of your work, it simply gets you back to a clean slate in the DevContainer setup.

To fully reset your Dev Container, exit VSCode. Open the Docker Desktop Dashboard. Select "Containers" in the sidebar. Check the box next to `comp110-24s-003` and delete the container.

Now try reopening the Dev Container for your COMP110 workspace in VSCode. Open VSCode, go to File > Open Recent and select the [Dev Container] entry for COMP110. Give it some time to start up. You will see lots of lines of obscure output being printed to a terminal. Give it a minute to start and load extensions, you should not see any spinning circles or loading icons in the bottom status bar of VSCode. 

If prompted to "Reload Window" for Pylance/Python extension, do so. If not prompted, you should _Reload Window_ anyway through the command palette search for "Developer: Reload Window" and select it. This will cause the VSCode window to reload.

At this point, you have fully reset your Dev Container.

## macOS Intel - Disable VirtioFS and Virtualization Framework

If you are on an Intel-based mac and seeing issues in VSCode, changing the following two settings tends to resolve it:

1. Open Docker Desktop Settings and under 'file sharing' select `osxfs (Legacy)`
2. Uncheck the box "Use Virtualization Framework"

Click the "Apply and Restart" button to make the changes in Docker save and restart Docker. After doing so, reopen VSCode and try again. If this still does not resolve the issue, it is worth trying the [Common Fix: Resetting the Container](#resetting-the-container)

