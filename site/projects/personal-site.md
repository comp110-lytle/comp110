---
title: Setting Up a Personal Website
author:
  - Alyssa Lytle
page: exercises
template: overview
---

# Instructions

## 1. Clone the Repo

Open a new Visual Studio window and clone the following repo: [https://github.com/AlyssaLytle/personal-site.github.io.git](https://github.com/AlyssaLytle/personal-site.github.io.git)

## 2. Create a Github repository for your site 
 <!-- named `<github-username>.github.io` -->
Now you need to connect this directory to Github!

1. Navigate to [https://github.com/](https://github.com/) and click on the "New" button to create a new repository.

2. Name your repository `<github-username>.github.io` where `<github-username>` is your github username and choose whether or not your repo will be Public or Private. (This will not impact who can see your site. It'll just impact who can see the *repository* for your site.) It's probably best to set your visibility to Private. This will give you some permission limitations when pulling/pushing to github though, so you'll have to [set up an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) and use it to connect your Github account with your computer.

3. Click "Create Repository"


## 3. Link Your Site to Github

Now we want to link the site you just cloned to visual studio to Github!

1. Open Visual Studio and then open the directory that you just cloned.

2. Open the command palette, and type `Git: Initialize Repository` you can select `<site-name>` as your workspace folder.

3. Open the command palette again and type `Git: Add Remote` and input the link to your git repo (`https://github.com/<github-username>/<github-username>.github.io.git`). When prompted, you can name your remote "origin".

4. Commit your changes and push to origin!


## 4. Configure a publishing source for your GitHub Pages site

*(It is possible that this step will be automated for you! You can check by going to your site URL: `<github-username>.github.io` and seeing if anything shows up!)*


Follow steps 1-8 [here](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-from-a-branch). For step 1, you can choose your "main" branch.

<!-- 

<img class="img-fluid" src="/static/assets/f23/pages-branch.png" alt="Image of Github Pages settings page under the 'branch' header. 'main' is selected as the branch. "  /> -->

After you do this, your site should be live at `https://<github-username>.github.io`


## 5. Add Content + Make it Pretty
You'll want to start by modifying the `_config.yml` file to add some info about yourself!

You can also change the Jekyll theme of your site to style it!
Here is a list of the currently supported themes: [https://pages.github.com/themes/](https://pages.github.com/themes/). Click on the Theme you want and it'll give you instructions on how to install it!

*(I'll add more here later.)*

# More Info
More info for general debugging can be found [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=mac)