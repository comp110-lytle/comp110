---
title: Troubleshooting
author:
- Claire Helms
page: resources
template: overview
---

Before you hop in the Office Hours queue, check out these common issues and their solutions!

## General Assingment Issues

### There's a bug in my code... I think?
A software 'bug' is an error or flaw in code that causes the program to behave in unintended ways. In office hours, we're available to help spot bugs, but there are also ways for you to debug yourself!

1. __Use environment diagrams!__ Environment diagrams are super effective for tracing code. You can write your own environment diagrams for your program to track what goes wrong. Here's a refresher on environment diagrams.
2. __Review applicable concepts.__ Are you working with the modulo (%) operator? Factorials? Functions? You may have forgot a characteristic of the concept, such as that 0! == 1 and function definitions require specific syntax. Brush up on concepts to be sure you understand them!
3. __Take it to paper.__ If you're really stuck, you might want to revisit reworking the steps of your program. One way programmers do this is by writing *pseudocode*, which is a simplified outline of a program that contains its necessary steps. Once you have written down pseudocode for the assignment, you can compare it with your code's implementation! This is also a great way to start writing a program. Check out this <a href="https://www.geeksforgeeks.org/how-to-write-a-pseudo-code/" target="_blank">GeeksforGeeks article</a> for more info on pseudocode.

## Issues with Git
Issues with Git can seem really scary; the reality is, though, you can solve them yourself! Here are some common Git issues and their solutions:

* __Problem: "Pull from upstram not working : can't integrate ...":__
    * Possible solution:
        1. Make sure you have committed and backed up everything before pulling. Any uncommitted changes could prevent you from pulling new material.
* __Problem: the *Source Control* panel in VSCode says "The folder open currently doesn't have a git respository...", and you can't push, pull, commit, etc.:__ 
    * This indicates that there is no valid git instillation, and this has been happening frequently to Mac users after their computer upates.
        * Solution: 
            1. In the terminal, run `xcode-select --install`
                a. In the popups, accept the request to start an installation
            2. Restart VSCode (don't just X out of it)
                a. Click "Code" at the top of the screen, next to the Apple symbol
                b. Click "Quit Visual Studio Code" at the bottom of the dropdown menu
        * The Source Control panel should now look normal, so go ahead and retry the operation you were trying to do originally!
* __Problem: You can't get characters to show up when you start typing in a file in VSCode/it takes a while for the keyboard to "start working":__
    * You have probably installed and enabled the *Vim extension* in VSCode accidentally (this happens frequently when VSCode recommends extensions).
        * Solution: 
            1. On the left side of VSCode, where we access the file explorer and the source control panel, click the button that looks like four squares with one square separated from the group.
            2. You should see a list of extensions under the title “Installed.” If you just see “Installed” without a list of items underneath it, click on the “Installed” line.
            3. Click on the “Vim” extension in this “Installed” list.
            4.  page about the Vim extension should open up to the right. Under the title of the page, you should see and click on the “Disable” button.
            5. Another button that says “Reload Required” should now appear in the same location. Click this button and wait for VSCode to quit and reopen.
        * Vim should now be disabled and should no longer have any effect over your experience typing in VSCode.
* __Problem: error message "invalid developer directory.":__
    * Solution:
        1. run `xcode-select --install` to verify you have xcode installed
        2. run `sudo xcode-select --switch \Library\Developer\CommandLineTools`


## Issues with Python/VSCode

### General
* __Issue: None of your Python commands are working:__
    Solution: trash all existing terminals and create a new one. Check it's inside your workspace folder.
* __Issue: Python only shows anaconda version "(base)":__
    Solution: run //conda deactivate
* __Issue: Timeout exception error when running `python -m pip install pip -r requirements.txt`:__
    Solution: in terminal, run `python -m pip install pip --default-timeout=100 -r requirements.txt`

### Mac
* __Issue: Password not working while running a command with `sudo`:__
    Solution: try running the command without `sudo`
* __Issue: git commands result in xcrun error:__
    Solution: in terminal, run `xcode-select --install`
* __Issue: Default shell is 'bash' instead of 'zsh':__
    Solution: Enter Command Palette (`Cmd+Shft+P`), select "Terminal: Select Default Shell", select `zsh`
* __Issue: VSCode still says it's running Python 2.7:__
    This is for when VSCode still says it's Python 2.7 even when running `python --version` or `python3 --version` in a terminal says 3.10.1
    Solution: run `sudo ln -s "$(which python3)" "$(dirname $(which python3))/python"`
    Trash the terminal and open a new one.
* __Issue: Need for split screen:__
    Hold down the green button in the top left of your screen and "Tile Window" to the left or right!
* __Issue: "No module 'tools'/'exercises'" on file export:__
    Solution: make sure your default shell is `zsh` (see issue above)
* __Issue: Command Palette lacking git commands:__
    Solution: Move VSCode from Downloads folder on your Mac into Applications folder (can drag and drop!)

### Windows
* __Issue: VSCode can't find Python:__
    Solution: reboot VSCode. If still a problem, uninstall and re-install Python being *very careful* to check the box on the first screen that asks if you want to add Python to PATH.
* __Issue: VSCode is not available as default text editor:__
    Solution: install VSCode before Git.
* __Issue: checking `Python --version` opens app store or displays an old version of Python:__
    Solution: Uninstall and reinstall python via Start > Add/Remove Programs and BE SURE “Add Python to PATH” is selected. Continue install. Try again from a new terminal session and, worst case, reboot if still an issue.
* __Issue: "git bash permission denied":__
    Solution: try using `py` instead of `python` So: `py –version` instead of `python –version`


Have a problem not covered? Join us in <a href="https://course.care" target="_blank">Office Hours</a>! Else, you can be a \~detective~ and research solutions yourself (StackOverflow has helped me troubleshoot many times). Just be sure to not make fatal changes. Happy solving!