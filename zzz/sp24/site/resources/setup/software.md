---
title: Software Setup
author:
- Kris Jordan
- Alyssa Byrnes
page: resource
template: overview
---

This guide will walk you through installing the software you'll need for the course. Before diving in it's worth understanding what you're about to do at a high level.

First, you should be sure your operating system is up-to-date. If you did not already move through the [Operating System Update](/resources/setup/os-update.html) steps, then go ahead and do that.

Next, you'll install the software needed to _write your own programs_ in the course. In general, to write your own programs you need two kinds of software installed: a **programming language toolkit** and a **text editor designed for programming**. For this course we'll explore programming with the Python programming language using the Visual Studio Code text editor. These are two of the most widely used tools of their kind in 2021 and are highly applicable beyond the scope of this course.

Finally, you'll install the Zoom Web Conferencing software. Installing this app on your computer, rather than using the web version, will improve your experience and make it easier for you to share your screen with our course staff as needed. If you already have the app installed, be sure to check for updates as Zoom improved over the break.

Follow the instructions for your operating system, either [Windows 10 and 11](/resources/setup/os-update.html#windows-10-instructions) or [macOS](/resources/setup/os-update.html#macos-instructions).

-----

# Windows 10 and 11 Instructions

Before beginning, be sure you are using the latest version of [Windows 10](/resources/setup/os-update.html#windows-10).

## 0. Install the Latest (Release Candidate) Python Programming Language Toolkit (3.11.1 or greater)

For these steps, be sure your web browser Window is maximized and be sure to follow step 4.0 closely that **checks** the option "Add Python 3.11.1 to Path" during install. 

0. Open the **Python Website** in another tab: <a href="https://www.python.org" target="_blank">https://www.python.org</a>
1. Press the **Downloads** button in navigation.
2. In the headline, you should see **"Download the latest version for Windows"**.
   * If, instead, you see "Download the latest version of Python" be sure your browser Window is maximized and refresh the web page.
3. Press the **Download Python 3.11.4** button. The download should begin.
   * If you are taken to another page without a download beginning, scroll down to the **Files** heading and select the file named `Windows x86 executable installer`.**
4. Open the download once it completes and **carefully** follow the instructions below, _especially the first one_:
   0. **IMPORTANT: Check the box on the first screen labelled "Add Python 3.11.4 to PATH"**
      - If you do not see this option, you likely have an older version of Python already installed. Go ahead and uninstall the old version and then retry installing the new version.
      - Knowing exactly what this does is beyond your concern, but the gist is it makes it easier for other programs on your system to make use of Python.
   1. After checking the box of Step 0, click Install Now.
   2. Allow the installer to make changes if further prompted.
   3. Accept other defaults on following screens.
   4. Click the Close button to complete the Install.

## 1. Install the Visual Studio Code (VSCode) Text Editor

0. Open the **VSCode website** in another tab: 
<a href="https://code.visualstudio.com/" target="_blank">https://code.visualstudio.com/</a>
1. Select the large **Download for Windows** button
2. Open the downloaded installer after its download completes
   0. Accept the licensing agreement
   1. You're asked _where_ to install VS Code. The suggested location is OK. Press Next.
   2. You're asked if you want to add VS Code to your start menu. That's OK, too. Press Next.
   3. **Important** Under additional tasks, **check all** of the options available.
      - These options make it easier for you to open files in VS Code.
   4. At Ready to Install, select Install.

## 2. Install the `git` Source Code Management Software (SCM)

0. Open the `git` website in another tab: <a href="https://git-scm.com" target="_blank">https://git-scm.com</a>
1. Look for the button to "Download for Windows" (it is embedded in a monitor graphic to the right)
2. After the download begins open the installer
3. Allow the app to make changes and install
4. Press Next on the Information page
5. Press Next on the Destination Location page (default is fine)
6. Press Next on the Components page (defaults are fine)
7. Press Next on the Start Menu Folder page
8. Choose Visual Studio Code as Git's default editor and press Next
9. Press Next/Install on the remaining pages and accept the defaults

## 3. Reboot your machine!

Reboot your computer now. Some settings of the applications you just installed will not take effect until you reboot. Attempting to continue on from this point without rebooting will lead to strange errors later.

Once you've completed this, you've got the necessary software installed! Great work!

----

# macOS Instructions

Before beginning, be sure you are using the latest version of [macOS](/resources/setup/os-update.html#macos).

## 0. Update Your Default Shell in the Terminal

There are two pieces of _jargon_ in the title of this section. A "shell" is a program that serves as a concierge to your computer: you give it commands, such as asking it to run a program you're working on, and the shell does the work of carrying out your command. A "terminal" is the program you will use to interact with your shell. Apple recently updated its recommended shell software to Z-shell, or `zsh`, so let's be sure yours is configured to use it.

0. Using Mac's Spotlight Search, accessed by pressing `Command + Spacebar` or clicking the search icon near your clock, type `Terminal` and press enter. This starts the Terminal app, which may look like what hackers use in the movies, _because it is_.
1. Let's learn what shell program your terminal is using by default by typing the following (cryptic, based on what we know now) command and pressing enter: `echo $SHELL`  (yes, that's the word `echo`, followed by a space, and then a dollar sign followed immediately by the word SHELL in all capital letters, `$SHELL`)
2. If you see `/bin/bash` in the text "printed" below your command, continue to next step to update your default. If, instead, you see `/bin/zsh`, you are all set and can jump to step 6.
3. Since you saw `bash` instead of `zsh`, let's `ch`ange your default `sh`ell using the `chsh` program to be the location, or path, of the `zsh` shell program on your computer which is `/bin/zsh`. Type the following command, check that yours matches exactly, in both spaces and capitalization, and press enter: `chsh -s /bin/zsh`
4. You will likely be asked for your computer's password. When you type in your password you will not see any text appear on your screen, not even dots, but the keys you type are being received. Press enter once you've entered your password. If you see "Credentials could not be verified, username or password is invalid." try running the command again and entering your laptop's password again.
5. This change will be applied to your next shell session, so type `exit`, close your `Terminal` again. Go back up to step 0, and continue from there, to confirm it was successful. 
6. Great! You can quit your shell session by typing `exit`, pressing enter, and then closing your `Terminal` window.

## 1. Install (or Update) the Python Programming Language Toolkit (3.11.1 or greater)

For these steps, be sure your Web Browser window is maximized. 

0. Open the **Python Website** in a new tab: <a href="https://www.python.org" target="_blank">https://www.python.org</a>
1. Select the **Downloads** button in the navigation
2. Look for the **"Download latest version for Mac OS X"**
   * If you instead see, "Download the latest version of Python", make sure your browser is full screen and refresh the page.
3. Click the **Download Python 3.11.4** button. Your download should begin.
   * If you are brought to another page, scroll down to the Files section and select the `macOS 64-bit universal2 installer`.
4. Open the downloaded package to begin the installer
   0. At Introduction screen: Continue
   1. At the Read Me screen: Continue
   2. At the License: Continue (Agree)
   3. At Installation Type: Install
   4. After Install completes, select Close and close any windows it popped up. 
   5. If asked, move the installer to Trash

## 2. Configure your Shell to use the Latest Python

0. Open a new Terminal window. If you still have one open from section 0, close it out and start a new one, because changes made during the installation of Python will not take effect until a new shell session begins.
1. Give the command `python3 --version`, notice the `3` after the word `python` and two dashes at the front of `--version`, and press enter. You should see `Python 3.11.1` (or greater) which indicates your install was successful. If not, try the steps above one more time and restart your computer before trying these. Otherwise, come work with us in office hours!
2. Now try giving the command `python --version`, without the `3` from above. If you see `Python 2.X.YY`, where `X` and `YY` are irrelevant numbers, continue to the next step because Mac also includes a much older version of Python. This is confusing when you're trying to learn modern Python! If you see `Python 3.X.YY`, but not `Python 3.11.1` or greater, this means you previously installed an older version of Python3, and you should also continue to step 3. If you see the result `Python 3.11.x` then you are all set and can continue to the next section on installing VSCode.
3. Let's simplify life by making `python` refer to the latest version you just installed, not the old one. What the following command is doing is making a link between the name `python` and the version you just installed. The command is more advanced than where we are at, so do not worry yourself on its details. You should copy and paste the following command into your Terminal, and press enter, because the punctuation symbols need to match precisely.

`sudo ln -s "$(which python3)" "$(dirname $(which python3))/python"`

 If you are prompted for a password, enter your computer's password. You will not see any indication of your keystrokes show up as you type in your password, but they are being recorded. Press enter after typing your password invisibly. 
4.
4. This change will only take place in a new shell session. Type the `exit` command, press enter, close your terminal. **Go back to Step 0** and continue on until confirming `python --version` is successfully linked to `Python 3.11.1` or greater.

## 3. Install the Visual Studio Code (VSCode) Text Editor

0. Open the VSCode website in a new browser tab: <a href="https://code.visualstudio.com/" target="_blank">https://code.visualstudio.com/</a>
1. Select the large Download for Mac button
2. When you open this Zip download, it creates an application file named Visual Studio Code in your **Downloads** folder and opens that folder in a new **Finder** window.
3. Confirm your **Finder** window sidebar is visible, it should be to the left of your files and you should see _Applications_ listed under _Favorites_. If you do not see the sidebar, go to the _View_ menu and select _Show Sidebar_. If you do not see _Applications_ listed under _Favorites_, open the _Finder_ menu, select _Preferences..._, and check _Applications_.
4. To install Visual Studio Code as an Application, drag the _Visual Studio Code_ icon into your _Applications_ directory which you should see in the left-hand sidebar of the Finder window under Favorites.
5. Open Spotlight Search again (`Command + Space` or the search icon by your clock) and search for "Code". You should see Visual Studio Code in the results. Open it and it will likely ask to confirm it's OK to open a file downloaded off the internet. Accept.
5. You should see Visual Studio Code open to a Welcome tab. If you do, you're all set and can close it for now and continue on.

## 4. Install the `git` Source Code Management Software (SCM)

0. If you do not have a running shell session in Terminal, start one as you did above. 
1. Type `git --version` and press Enter.
2. If you see text displayed such as "git version 2.21.0)" then you already have `git` installed and can close the terminal and continue on
3. If `git` was not already installed, you should see a pop-up window asking you to install **Git / Developer Tools**. Accept this install request and follow its instructions through completion. After it completes, `exit` and continue to Step 0 to confirm the install succeeded.
   * Note: You may instead see a notice about accepting a license agreement and/or running a given command in your terminal. In that case, just follow the instructions and enter your password if needed.

Once you've completed this, you've got the necessary software installed! Great work!


----

# Basic Troubleshooting

If you are having trouble linking to your newest version of python, try these things...

Remember that you can always check which version of python is being run by typing `python --version` in your terminal.

## Deactivate Conda

Many people seem to have issues because they have previously installed Conda. Therefore the `python` and/or `python3` commands could be calling this version. If this is your case, open your terminal and type:

`conda deactivate`

Don't worry! You will be able to reactivate it again if you need it!

## Unalias python
It might be the case that there is an existing Python alias on your computer. Open your terminal and type:

`unalias python`

If nothing is output, that means that an old alias existed and you just deleted it. If you get an error code, then this was not the issue.

## Restart your Terminal
It could just be an issue of closing out of your terminal and opening it back up! 