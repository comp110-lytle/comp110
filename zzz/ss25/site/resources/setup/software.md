---
title: Software Setup
author:
- Kris Jordan
page: resource
template: overview
---

This guide will walk you through installing the software you'll need for the course. Before diving in it's worth understanding what you're about to do at a high level.

First, you should be sure your operating system is up-to-date. If you did not already move through the [Operating System Update](/resources/setup/os-update.html) steps, then go ahead and do that first.

Next, you'll install the software needed to _write your own programs_ in the course. We will be using a modern technology called Docker Containers and VSCode to ensure your development tools are exactly the same as everyone else's in the course, regardless of whether you are on Windows or Mac. We will talk more about each, but briefly Docker is what allows us to bundle the same required software for everyone and VSCode will be the program you write your programs in.

Follow the instructions for your operating system, either:

* [Windows 10 and 11](#windows-10-and-11-instructions)
* [macOS](#macos-instructions)

-----

# Windows 10 and 11 Instructions

Before beginning, be sure you are using the latest version of [Windows 10](/resources/setup/os-update.html#windows-10) or 11.

## 0. Before installing Docker, you will need to enable WSL (Windows Subsystem for Linux)

1. From your Start Menu, please search for PowerShell and open it as an Administrator (right-click and select "Run as Administrator")
2. **Be sure you opened PowerShell as an Administrator! In the previous step you should have right-clicked and selected "Run as Administrator"**.
3. Type in the command `wsl --install` and press enter. This will take a few minutes to complete. Note there are two dashes before the word `install`.

## 1. Install Docker Desktop

1. [Download Docker Desktop application by clicking this link](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe).
2. Open the installer you just downloaded and follow its instructions to install Docker Desktop.

You may need to reboot your computer in this process.

## 2. Install the git Source Code Management Software (SCM)

1. Open the git website in another tab: <https://git-scm.com>
1. Look for the button to “Download for Windows” (it is embedded in a monitor graphic to the right)
1. After the download begins open the installer
1. Allow the app to make changes and install
1. Press Next on the Information page
1. Press Next on the Destination Location page (default is fine)
1. Press Next on the Components page (defaults are fine)
1. Press Next on the Start Menu Folder page
1. Choose Visual Studio Code as Git’s default editor and press Next
1. Press Next/Install on the remaining pages and accept the defaults

## 3. Install the Visual Studio Code (VSCode) Text Editor

0. Open the **VSCode website** in another tab: 
<a href="https://code.visualstudio.com/" target="_blank">https://code.visualstudio.com/</a>
1. Select the large **Download for Windows** button (Stable Build)
2. Open the downloaded installer after its download completes
   0. Accept the licensing agreement
   1. You're asked _where_ to install VS Code. The suggested location is OK. Press Next.
   2. You're asked if you want to add VS Code to your start menu. That's OK, too. Press Next.
   3. **Important** Under additional tasks, **check all** of the options available.
      - These options make it easier for you to open files in VS Code.
   4. At Ready to Install, select Install.

## 4. Reboot your machine!

Reboot your computer now. Some settings of the applications you just installed will not take effect until you reboot. Attempting to continue on from this point without rebooting will lead to strange errors later.

Once you've completed this, you've got the necessary software installed! Great work!

## 5. Continue to Workspace Setup

Now that your software is installed, it's time to setup your personal workspace for the course. Continue on to [Workspace Setup](/resources/setup/workspace.html).

----

# macOS Instructions

Before beginning, be sure you are using the latest version of [macOS](/resources/setup/os-update.html#macos).

## 0. Check to see your mac Computer/Processor/CPU is made by Intel or Apple

0. Open Spotlight Search (the magnifying glass icon in the top-right corner), search for: _About this Mac_.
1. Look for the _"Processor"_ or _"Chip"_ line. If it says _Apple_, you have an Apple Silicon CPU. If it says _Intel_, you have an Intel CPU.

## 1. Download and Install Docker Desktop

0. [If your processor is **Intel**, please download this version of Docker.](https://desktop.docker.com/mac/main/amd64/Docker.dmg)
1. [Otherwise, if your processor is **Apple**, please download this version of Docker.](https://desktop.docker.com/mac/main/arm64/Docker.dmg)

## 2. Install the git Source Code Management Software (SCM)

1. Start a Terminal window: Open Spotlight Search (the magnifying glass icon in the top-right corner), search for: _Terminal_.
1. Type `git --version` and press Enter.
1. If you see text displayed such as “git version 2.39.3” then you already have git installed and can close the terminal and continue on to part 3 of Installing VSCode.
1. If git was not already installed, you should see a pop-up window asking you to install Git / Developer Tools. Accept this install request and follow its instructions through completion. After it completes, exit and continue to Step 0 to confirm the install succeeded.
1. Note: You may instead see a notice about accepting a license agreement and/or running a given command in your terminal. In that case, just follow the instructions and enter your password if needed.
1. Once complete, you can close the terminal.

## 3. Install the Visual Studio Code (VSCode) Text Editor

0. Open the VSCode website in a new browser tab: <a href="https://code.visualstudio.com/" target="_blank">https://code.visualstudio.com/</a>
1. Select the large Download for Mac button
2. When you open this Zip download, it creates an application file named Visual Studio Code in your **Downloads** folder and opens that folder in a new **Finder** window.
3. Confirm your **Finder** window sidebar is visible, it should be to the left of your files and you should see _Applications_ listed under _Favorites_. If you do not see the sidebar, go to the _View_ menu and select _Show Sidebar_. If you do not see _Applications_ listed under _Favorites_, open the _Finder_ menu, select _Preferences..._, and check _Applications_.
4. To install Visual Studio Code as an Application, drag the _Visual Studio Code_ icon into your _Applications_ directory which you should see in the left-hand sidebar of the Finder window under Favorites.
5. Open Spotlight Search again (`Command + Space` or the search icon by your clock) and search for "Code". You should see Visual Studio Code in the results. Open it and it will likely ask to confirm it's OK to open a file downloaded off the internet. Accept.
6. You should see Visual Studio Code open to a Welcome tab. If you do, you're all set and can close it for now and continue on.

## 4. Reboot your machine!

Reboot your computer now. Some settings of the applications you just installed will not take effect until you reboot. Attempting to continue on from this point without rebooting will lead to strange errors later.

Once you've completed this, you've got the necessary software installed! Great work!

## 5. Continue to Workspace Setup

Now that your software is installed, it's time to setup your personal workspace for the course. Continue on to [Workspace Setup](/resources/setup/workspace.html).