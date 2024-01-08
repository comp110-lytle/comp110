---
title: Workspace Repository Setup
author:
  - Kris Jordan
  - Alyssa Byrnes
page: resource
template: overview
---

Before beginning these instructions you should have first [updated your operating system](/resources/setup/os-update.html) and then [installed the required software (Python 3.11, Visual Studio Code, and git)](/resources/setup/software.html).

## 0. Find Your Canvas UNC E-mail Address

_**Canvas UNC e-mail addresses typically end in @live.unc.edu or @email.unc.edu**!_

Find your Canvas e-mail address by logging into Canvas, clicking on "Account" in the top right corner, selecting "Settings", and looking under the Email field on the right.

Use your Canvas e-mail address when you login to Gradescope and register for GitHub.

## 1. Register for GitHub

GitHub is for backing up your course Workspace Repository and for downloading course materials.

You can think of GitHub as a social network where people and organizations share and collaborate on code with one another. Organizations like NASA, NOAA, Peace Corps, Washington Post, New York Times, and so on, host projects publicly (and privately) on GitHub. It's a valuable service for data scientists, software engineers, research teams, and more.

Your coursework will have its own private "git repository". The technology we use for backing up versions of our projects and transmitting them to or from the internet, hosted on GitHub, is called _git_. Visual Studio Code has git support built into it. Git is a professional _version control_ tool we use in limited ways in COMP110, but if you continue on in a field that involves programming and data you'll likely encounter it again.

1. Register for a GitHub account with your primary UNC address: <a href="https://github.com/" target="_blank">https://github.com/</a>
   - You are encouraged to choose your ONYEN as your username, if it is available (not required)
2. After registering, edit your profile from this page: <a href="https://github.com/settings/profile" target="_blank">https://github.com/settings/profile</a>
   - Be sure your name and email match what you used on Course.Care
   - Fill out the rest of your GitHub profile with a high quality photo of yourself, a brief bio, UNC Chapel Hill as your "company", and Chapel Hill (or home) as your location if you are going to continue in a field that involves programming (computer science, data science, information science, and so on). Think of this as a secondary LinkedIn when it comes to future opportunities, because that's often how employers and graduate schools look at it.

## 2. Setup your Workspace in Visual Studio Code

1. Open Visual Studio Code
2. Open the _View_ menu and select _Command Palette_
   - You'll use the Command Palette a lot so it's worth trying to remember its shortcut!
   - Windows: `Control+Shift+P`
   - Mac: `Command+Shift+P`
3. Type in "Git: Clone" (without the quotes) and press `Enter`.
   - If you do not see this option after installing course software previously, try rebooting your computer.
4. Copy the following URL: `https://github.com/comp110-24s/comp110-24s-workspace.git`
   - Right Click and Paste the copied URL into the text box that appeared in VS Code after the previous step.
   - Or use the Paste keyboard shortcut: `Control+V` Windows / `Command+V` Mac
5. Press Enter and you will be asked where you want your course workspace repository to be saved on your computer. Just accepting the default suggestion is OK.
6. Visual Studio Code may ask you to enter your GitHub username and password in the same place you just entered your Workspace Repository URL. If you don't see this prompt you can proceed to step 7.
   - If it asks for your GitHub username, type it in and press enter. Your username can be found in the top left of your GitHub profile at <a href="https://github.com/settings/profile" target="_blank">https://github.com/settings/profile</a>.
   - If it asks for your GitHub password, type it in and press enter. Your password will show up as dots as you type.
7. Press OK when asked if you would like to Open the repository after it downloads.

## 3. Installing VSCode Extensions

VSCode can be customized with extensions specific to the types of work you use it for. We will install extensions that help us this this course. We recommend limiting the number of additional extensions you install, you shouldn't need any more for our course, because they can slow down VSCode and not cooperate with one another nicely in some configurations.

1. If you see a popup notifying you "This workspace has extension recommendations." then click "Install All"
   - VSCode will ask you to restart for the Pylance extension. Allow it to.
   - Press ignore for any additional prompts to install additional plugins such as `pytest` or `flake8`. For these you can click the gear icon and ask VSCode to stop recommending them.
2. Confirm you have the correct VS Code extensions installed by clicking the `View` menu and selecting `Extensions`. If you do not see the following listed under "Installed", find them under Recommended, click on each, and click install.
   1. Python
   2. Pylance
   3. Jupyter
   4. Edit csv
3. Restart VSCode by going to File > Exit and then opening VSCode.

## 4. Installing Python Libraries

We will use some popular 3rd party libraries this semester in COMP110. These are freely available, open source packages that other software developers made and shared. The packages installed will help us with some data science concerns when we reach that segment of the course.

1. Open the _File_ menu, followed by _Open Recent_ and you should see the top entry listed as something like "comp110-24s-workspace"
   - If you do not, try closing and reopening VSCode.
2. In the future, if you open VS Code and need to get back to your COMP110 Workspace, the easiest way is to repeat step 1 above.
3. In the bottom "status bar" of VSCode, to the right of "main" and a refresh icon, you should now see Python followed by a version number. If the version number is not there or is not 3.10 or greater, follow the next bullet:
   - Open the _View_ menu and _Command Palette_. Type "Python: Select Interpreter" (without the quotes) and press Enter. From the list that pops up choose Python 3.10 or greater.
4. Open the _View_ menu and select _Terminal_ to bring up the built-in terminal.

### Everyone follow these steps 5-6:

5. In the _Terminal_ type the following command, being careful to match it _exactly_.

```{.bash}
    python -m pip install pip -r requirements.txt --user
```

6. Press `Enter` to run the command. This command installs additional Python libraries, which give you functionalities we'll use later in the course.

## 5. Setup your Backup Workspace on GitHub

1. Navigate a web browser to <a href="https://classroom.github.com/classrooms/153874831-comp110-24s-classroom-a7fa2a" target="_blank">Github classroom</a>
2. Click "Skip to the next step" when prompted to select your user / identification
3. Click "Accept this Assignment"
4. When the workspace is getting setup you may need to refresh until it tells you you're ready to go!
5. Click the link to your personal backup repository that looks something like this `https://github.com/comp110-24s/comp110-workspace-KrisJordan` (except instead of `KrisJordan` you will see your GitHub username).
6. Toward the top of the page there will be a green button that says `Code`. Click this and you will see two options: HTTPS and SSH. Click HTTPS.
7. Copy the text in the box to the right of the HTTPS/SSH buttons (or click the clipboard icon). This is the URL to your backup repository.
8. In VSCode, ppen the _View_ menu and select _Command Palette_, the shortcut for this menu is:
   - Windows: `Control+Shift+P`
   - Mac: `Command+Shift+P`
9. In VSCode, type in _Git: Add Remote_ and press enter with the option selected.
10. In the blank text box that appears, paste in the URL to your backup repository that you just copied. Press enter.
11. When asked for "Remote name" type in: `backup`
12. Open up the _Command Palette_ once more, just as in step 8.
13. Begin typing in: `Git: Push to...` and press `Enter` once it is the first option.
14. Select the `backup` remote that is your personal workspace on GitHub.
    - You may see a spinning "refresh" icon in your status bar at the bottom of VSCode. Unless an error backing up occurs, you will not see any confirmation. It succeeds silently.
    - If you want to see your backed up work on Github, back in your web browser, refresh the page you had open and you should see files in it now.
15. If steps 13 and 14 do not work, do the following:
    - If your _Terminal_ window from above is still open from section 3, great! If not, open a new _Terminal_ pane in VS Code.
    - At the prompt, type the following command and press enter:
      `git push --force backup main`

## 6. Configure your `git` Name and E-mail

1. If your _Terminal_ window from above is still open from section 3, great! If not, open a new _Terminal_ pane in VS Code.
2. At the prompt, type the following command and press enter with your primary e-mail address inside the double quotes:

```{.bash}
git config --global user.email "your@primary.email"
```

3. Then, type tye following command and press enter with your first and last name inside the double quotes:

```{.bash}
git config --global user.name "Your Name"
```

After doing this, when you make backup commits in `git` (which you'll do shortly!) they'll be correctly attributed to you.

## 7. Operating System Specific Configuration

### Windows

If your laptop is running Windows, you should change the default shell in VSCode to be Git Bash.

1. Open the _View_ menu and select _Command Palette_ (or press Control + Shift + P)
2. Type: Select Default Profile
3. Press Enter
4. From the dropdown list, you should see Git Bash. Select it.

### macOS

If your laptop is running macOS, you should confirm the default shell in VSCode is `zsh`. This should already be the case, but to be sure, run these steps:

1. Open the _View_ menu and select _Command Palette_ (or press Command + Shift + P)
2. Type: Select Default Profile
3. Press Enter
4. From the dropdown list, you should see `zsh` in one of the options. Select it.

It is handy to be able to open Visual Studio Code from your Terminal using the `code` command in the future. To register this:

1. Open the _View_ menu and select _Command Palette_ (or press Command + Shift + P)
2. Type: Install code command
3. Press Enter

---

## 8. Confirm Everything is Good to Go

From the View Menu, select Explorer. You should see a left-hand sidebar with comp110-WORKSPACE at the top and if you expand it you should see `exercises`,  `README.md`, etc. These are folders, which we refer to more technically as directories, and files in your workspace.

Let's be sure you are able to exit out of VSCode and find your work again. Go ahead and close VSCode. Then open new window. If you see the same files in the left-hand sidebar: great! Keep reading, though, so you know what to do in the future if you do not see your workspace.

If you do not see your workspace files in the Explorer sidebar, go to File, select Open Recent, and look for the topmost entry that is `comp110-24s-workspace` and select it. This is how you can get back to your workspace most easily in the future.

Great work! Your software setup is now ready for COMP110!
