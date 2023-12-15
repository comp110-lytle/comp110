---
title: Common Python Setup Issues
date: 2021-02-25
author:
  - Ezri White
page: logistics
template: overview
site-branch: team
---

# General

### Installing requirements leads to version error

Detailed Issue: Installing pip requirements.txt leads to “Could not find a version that satisfies the requirement pytest." (Or another package)

**Solution**: This seems to be an SSL error and some indication the user is behind a proxy / strong antivirus firewall or has malicious software running on their machine. The workaround is:

`python -m pip install --trusted-host=pypi.python.org --trusted-host=pypi.org --trusted-host=files.pythonhosted.org -r requirements.txt`

**Note**: Before trying this command, make sure to confirm that just `python -m pip install pip -r requirements.txt` does not work.

### None of their python commands are working

**Solution**: Make sure terminal is opened inside of the workspace folder

**Note**: There could be other causes for this so if that does not fix look at some of the other issues on here.

### Python only shows anaconda version "(base)"

Detailed Issue: Python version and path only showing the version of python installed with anaconda and before the prompt string in the terminal you see something like “(base)” or the name of some other environment. This means they have a conda session activated.

**Solution**: run `conda deactivate`

### Timeout exception error when installing requirements

Detailed Issue: Timeout exception error when running `python -m pip install pip -r requirements.txt`

**Solution**: increase timeout default by running `python -m pip install pip --default-timeout=100 -r requirements.txt`

# Mac

### Password not working with sudo (step 2)

Detailed Issue: Password not working when using sudo for step 2

**Solution**: Try running the command without `sudo`

### git _anything_ results in xcrun error

Detailed Issue: git _anything_ results in xcrun: error: invalid active developer path (/Library/Developer/CommandLineTools

**Solution**: run `xcode-select --install`

### Default shell is ‘bash’ instead of ‘zsh’

**Solution**: Cmd+Sht+P “Terminal: Select Default Shell”

### VSCode still says its running Python 2.7

Detailed Issue: VSCode still says that it’s python version 2.7 even though running python --version or python3 --version in a terminal window says 3.10.1

**Solution**: Following these steps in your terminal:

1. `sudo ln -s "$(which python3)" "$(dirname $(which python3))/python"`
1. trash the terminal, open a new one and it should work

### Need for Split screen

Detailed Issue: Student is struggling to code and simultaneously view instructions

**Solution**: Hold down the green button at the top of their window to go into split screen mode

### git broken with invalid developer directory

Detailed Issue: user unable to find git, the error message looks like: invalid developer directory

**Solution**:

- `xcode-select --install` ; verify you have xcode installed
- `sudo xcode-select --switch \Library\Developer\CommandLineTools`

### “No module ‘tools’” on file export / No module named exercises

Detailed Issue: Error message “No module ‘tools’” when trying to export file from VSCode on Mac

**Solution**: Make sure the student’s default shell is `zsh`

**Solution**: Make sure the terminal is running from the top workspace directory (a.k.a cd into the outermost folder)

### Command Palette lacking git commands

Detailed Issue: VSCode is not listing any of the git commands in the command palette

**Solution**: Move VSCode from Downloads folder into Applications folder

# Windows

### VSCode can’t find Python

**Solution**: Likely a PATH problem. If a student has not yet rebooted, they should do that now. If still fails, uninstall Python and reinstall being very careful to check the box on the first screen that asks if you want to add Python to PATH.

### VSCode is not available as default text editor

Detailed Issue: VSCode is not an option to use as default text editor after installing git.

**Solution**: Install VSCode first. The website instructions now recommend this route.

### Checking python version opens app store

Detailed Issue: Running `python --version` pops open windows app store or displays an old version.

**Solution**: Uninstall and reinstall python via Start > Add/Remove Programs and BE SURE “Add Python to PATH” is selected. Continue install. Try again from a _new terminal session_ and, worst case, reboot if still an issue.

### git bash permission denied

**Solution**: try using py instead of python
So: py --version instead of python --version
