---
title: Diagnostic Code Library
author:
- Ezri White
page: resource
---

# Diagnostic Codes


## S1 - Python Errors

### S101 - Python is not installed
#### Windows
   1. Open the Python Website: https://www.python.org
   2. Select Downloads
   3. Look for "Download the latest version for Windows"
   4. Select the button that is "Download Python 3.10" (make sure they are updated if they had python previously)
   5. Open the download once it completes and carefully follow the instructions below
      1. **IMPORTANT** Check the box on the first screen labelled "Add Python 3.10 to PATH"
         - Knowing _exactly_ what this does is beyond your concern, but the short story is it makes it easier for other programs (such as your text editor Visual Studio Code) to make use of Python.
      2. **AFTER** ensuring the box of step #1 is checked, click Install Now
      3. Allow the installer to make changes if further prompted
      4. **IMPORTANT** On the "Setup was Successful" screen, click on "Disable path length limit". Allow this change when prompted.
         - This is also outside your concern, but it removes a silly, old limitation on how long your project's directory names and file names could be.
      5. Click the Close button to complete the Install.

#### macOS
   1. Open the Python Website: https://www.python.org
   2. Select Downloads
   3. Look for the "Download latest version for Mac OS X"
   4. Select the button that is "Download Python 3.10" (make sure they are updated if they had python previously)
   5. Open the downloaded package to begin the installer
      1. At Introduction screen: Continue
      2. At the Read Me screen: Continue
      3. At the License: Continue (Agree)
      4. At Installation Type: Install
      5. After Install completes, select Close 
      6. If asked, move the installer to Trash

Alias the `python` command to refer to the version of Python you just installed:

1. Use _Finder_'s Spotlight Search feature (`Command+Space`) to open the _Terminal_ application
2. Try typing `python3 --version` and pressing `Enter` to complete the line. You should see `Python 3.10.x` printed out. If you don't after installing Python as above, try rebooting your machine.
3. Next you'll _alias_ the command `python` to mean the same as `python3`. By default on a Mac the command `python` means version 2 rather than 3. For professional programmers supporting old applications it can be useful to have both version 2 and 3 available. For your purposes, though, you can avoid a lot of frustration by ensuring you're always working with the latest version which is what the next steps will achieve.
   1. Look in the title bar of your Terminal window, you should see your computer user name followed by an emdash and then either `-zsh` or `-bash`
      1. If you see `-zsh` write the following command in Terminal, being careful to match punctuation _exactly_:
      - `echo "alias python=python3" >> ~/.zprofile`
      - After pressing enter this command adds an alias to your `.zprofile` file which contains settings for how your terminal works. The details of this command are outside the scope of our concerns for the time being.
      2. If you see `-bash` write the following command in Terminal, being careful to match punctuation _exactly_:
      - `echo "alias python=python3" >> ~/.bash_profile`
      - After pressing enter this command adds an alias to your `.bash_profile` file which contains settings for how your terminal works. The details of this command are outside the scope of our concerns for the time being.
   2. Close your Terminal window and open a new one for this change to take effect and then try typing:
      - `python --version`
      - You _should_ see `Python 3.10.x` print and _not_ `Python 2.7.x`. If you are still seeing version 2.0, try the first instruction again and restart your terminal once more.
      - Once this is working, you can close the Terminal.

### S102 - `python` command runs a version less than 3.10 
#### Windows
   1. Open the Python Website: https://www.python.org
   2. Select Downloads
   3. Look for "Download the latest version for Windows"
   4. Select the button that is "Download Python 3.10" (make sure they are updated if they had python previously)
   5. Open the download once it completes and carefully follow the instructions below
      1. **IMPORTANT** Check the box on the first screen labelled "Add Python 9 to PATH"
         - Knowing _exactly_ what this does is beyond your concern, but the short story is it makes it easier for other programs (such as your text editor Visual Studio Code) to make use of Python.
      2. **AFTER** ensuring the box of step #1 is checked, click Install Now
      3. Allow the installer to make changes if further prompted
      4. **IMPORTANT** On the "Setup was Successful" screen, click on "Disable path length limit". Allow this change when prompted.
         - This is also outside your concern, but it removes a silly, old limitation on how long your project's directory names and file names could be.
      5. Click the Close button to complete the Install.

#### macOS
- Navigate to https://www.python.org
- Follow the set up instructions here: [/resources/setup/software.html] to make sure Python greater than or equal to 3.10 is installed.

### S103 - Python version being run in vscode is lower than 3.10
- Open the _View_ menu and _Command Palette_. Type "Python: Select Interpreter" (without the quotes) and press Enter. From the list that pops up choose Python 3.10.1 or greater.
- If you do not see Python 3.10 as an option follow the steps in **S103** 


## S2 - Git Errors

### S201 - Git is not installed.
#### Windows
   1. Open the Git website: https://git-scm.com
   2. Look for the button to "Download for Windows" (it is embedded in a monitor graphic)
   3. After the download begins open the installer
   4. Allow the app to make changes and install
   5. Press Next on the Information page
   6. Press Next on the Destination Location page (default is fine)
   7. Press Next on the Components page (defaults are fine)
   8. Press Next on the Start Menu Folder page
   9. Choose Visual Studio Code as Git's default editor and press Next
   10. Press Next/Install on the remaining pages and accept the defaults
   11. Follow instructions in **S202** and **S203** to finish configuring git.

#### macOS
   1. Open Finder's Spotlight Search (the magnifying glass in your menu bar or press Command+Space)
   2. Search for _Terminal_ and open it
   3. Type `git --version` and press Enter.
   4. If you see text displayed such as "git version 2.21.0)" then you already have `git` installed and can close the terminal and continue on
   5. If `git` was not already installed, you should see a pop-up window asking you to install Git / Developer Tools. Accept that install and follow its instructions through completion.
   6. Follow instructions in **S202** and **S203** to finish configuring git.

### S202 - Git email and username are not configured
1. Open up a new terminal in vscode
2. Type `git config --global user.email "onyen@live.unc.edu"`, using your onyen and email.
3. Type `git config --global user.name "Your Name"`, replacing "Your Name" with your first and last name. 

### S203 - No upstream exists
1. Open the _View_ menu and select _Command Palette_
2. Type in _Git: Add Remote_ and press enter with the option selected.
3. Copy and paste the URL below into the text box that says "Provide repository URL" and press enter: 
   - https://github.com/comp110-20f/course-material.git
4. When asked for "Remote name" type in:
   - upstream
5. Press enter.
6. Open the _View_ menu and select _Command Palette_ once more
7. Type in _Git: Fetch From All Remotes_ and press enter
8. The _upstream_ remote repository is now registered! In an upcoming lesson you will learn how to download new material from this repository.

### S204 - Upstream does not match course upstream
1. Open up a new terminal in vscode
2. Type `git remote rm upstream` and press enter.
3. Follow instructions in **S203** to configure the correct remote.



## S3 - Package Errors

### S301 - Missing VScode Packages
1. Open up the course workspace
2. Open up a new terminal
3.  Type `python -m pip install pip -r requirements.txt` and hit enter.
