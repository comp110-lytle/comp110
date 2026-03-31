---
title: Workspace Setup Without Docker
author:
  - Alyssa Lytle
page: resource
template: overview
navbar: base
---

# Part 0. Checking for Python Install

To get your workspace working without using the Docker Dev Container, you first want to see if python is installed on your computer.

0. Open your terminal and type `python --version`. If you see something like `Python 3.11.1` (or greater), congratulations! You already have Python installed. You can skip the rest of these steps and continue to [Part 2](#part-2-install-requirements).

1. If you get an error, try typing `python3 --version`. 

If you get an error message, skip the rest of this step and continue to [Part 1](#part-1-installing-python).

*If* you see something like `Python 3.11.1` (or greater), then you have the correct version installed and just need to update your terminal command so that the `python` command works! Type the following command in your terminal exactly:

```
sudo ln -s "$(which python3)" "$(dirname $(which python3))/python"
```

It may prompt you for your computer password. This change will only take place in a new shell session. Type the exit command, press enter, close your terminal. Retry the command `python --version` to check it is successfully linked to Python 3.11.1 or greater. You can now skip Part 1 and continue to [Part 2](#part-2-install-requirements)!

# Part 1. Installing Python

## Windows 10 and 11 Instructions

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

## macOS Instructions

Before beginning, be sure you are using the latest version of [macOS](/resources/setup/os-update.html#macos).

### 0. Update Your Default Shell in the Terminal

There are two pieces of _jargon_ in the title of this section. A "shell" is a program that serves as a concierge to your computer: you give it commands, such as asking it to run a program you're working on, and the shell does the work of carrying out your command. A "terminal" is the program you will use to interact with your shell. Apple recently updated its recommended shell software to Z-shell, or `zsh`, so let's be sure yours is configured to use it.

0. Using Mac's Spotlight Search, accessed by pressing `Command + Spacebar` or clicking the search icon near your clock, type `Terminal` and press enter. This starts the Terminal app, which may look like what hackers use in the movies, _because it is_.
1. Let's learn what shell program your terminal is using by default by typing the following (cryptic, based on what we know now) command and pressing enter: `echo $SHELL`  (yes, that's the word `echo`, followed by a space, and then a dollar sign followed immediately by the word SHELL in all capital letters, `$SHELL`)
2. If you see `/bin/bash` in the text "printed" below your command, continue to next step to update your default. If, instead, you see `/bin/zsh`, you are all set and can jump to step 6.
3. Since you saw `bash` instead of `zsh`, let's `ch`ange your default `sh`ell using the `chsh` program to be the location, or path, of the `zsh` shell program on your computer which is `/bin/zsh`. Type the following command, check that yours matches exactly, in both spaces and capitalization, and press enter: `chsh -s /bin/zsh`
4. You will likely be asked for your computer's password. When you type in your password you will not see any text appear on your screen, not even dots, but the keys you type are being received. Press enter once you've entered your password. If you see "Credentials could not be verified, username or password is invalid." try running the command again and entering your laptop's password again.
5. This change will be applied to your next shell session, so type `exit`, close your `Terminal` again. Go back up to step 0, and continue from there, to confirm it was successful. 
6. Great! You can quit your shell session by typing `exit`, pressing enter, and then closing your `Terminal` window.

### 1. Install (or Update) the Python Programming Language Toolkit (3.11.1 or greater)

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

### 2. Configure your Shell to use the Latest Python

0. Open a new Terminal window. If you still have one open from section 0, close it out and start a new one, because changes made during the installation of Python will not take effect until a new shell session begins.
1. Give the command `python3 --version`, notice the `3` after the word `python` and two dashes at the front of `--version`, and press enter. You should see `Python 3.11.1` (or greater) which indicates your install was successful. If not, try the steps above one more time and restart your computer before trying these. Otherwise, come work with us in office hours!
2. Now try giving the command `python --version`, without the `3` from above. If you see `Python 2.X.YY`, where `X` and `YY` are irrelevant numbers, continue to the next step because Mac also includes a much older version of Python. This is confusing when you're trying to learn modern Python! If you see `Python 3.X.YY`, but not `Python 3.11.1` or greater, this means you previously installed an older version of Python3, and you should also continue to step 3. If you see the result `Python 3.11.x` then you are all set and can continue to the next section on installing VSCode.
3. Let's simplify life by making `python` refer to the latest version you just installed, not the old one. What the following command is doing is making a link between the name `python` and the version you just installed. The command is more advanced than where we are at, so do not worry yourself on its details. You should copy and paste the following command into your Terminal, and press enter, because the punctuation symbols need to match precisely.

`sudo ln -s "$(which python3)" "$(dirname $(which python3))/python"`

 If you are prompted for a password, enter your computer's password. You will not see any indication of your keystrokes show up as you type in your password, but they are being recorded. Press enter after typing your password invisibly. 
4.
4. This change will only take place in a new shell session. Type the `exit` command, press enter, close your terminal. **Go back to Step 0** and continue on until confirming `python --version` is successfully linked to `Python 3.11.1` or greater.


# Part 2. Install requirements.

First, you're going to want to *pull* the latest version of the course workspace from github. 

## "Pulling" course materials down from Upstream. 

**MAKE SURE YOU PUSH YOUR LOCAL CHANGES BEFORE DOING THIS!!!**s

0. Open the View menu and select Command Palette
    
    * The shortcut for this menu is:
    * Windows: Control+Shift+P
    * Mac: Command+Shift+P

1. Begin typing in Git: Pull From... and press Enter once it is the first option.
2. Begin typing in `origin` and press Enter once it is the first option.
3. Press enter with `origin/main` as the first option.
4. This downloads the latest course materials! It will succeed silently, so if nothing appears to happen, check to confirm that the "requirements.txt" file showed up in your workspace files. If there was an error, you would see an error message pop up. 

### Common errors/solutions: 

* Make sure you PUSHED all of your changes to backup first!!!
* In your terminal, type git config pull.rebase false
* In your Visual Studio command center, select Pull From... -> Upstream -> Upstream/Head. (If not an option, do Origin -> Main.)

If you’re still having issues, come to office hours!



## Install requirements

You can install the workspace requirements using the following command in your terminal: 

```
python -m pip install -r requirements.txt
```

Congratulations! You should be good to go!