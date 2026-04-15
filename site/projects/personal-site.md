---
title: Setting Up a Personal Website
author:
  - Alyssa Lytle
page: exercises
template: overview
---

# Instructions

## 1. Clone the Repo

You are going to create a new repository *outside* of your Comp110 workspace. 

1. Open a new Visual Studio window by clicking the _File_ menu in the top bar and selecting _New Window_. 


2. Under the _Start_ menu, click _Clone Git Repository..._

3. The command pallette should open at the top prompting you for a URL. Copy/Paste the following URL:

[https://github.com/AlyssaLytle/personal-site.github.io.git](https://github.com/AlyssaLytle/personal-site.github.io.git)

4. Select a destination to save the new repository and open the repository when prompted.

## 2. Create a Home Github repository for your site 
 <!-- named `<github-username>.github.io` -->


1. Navigate to [https://github.com/](https://github.com/) and click on the "New" button to create a new repository.

2. Name your repository `<github-username>.github.io` where `<github-username>` is your github username and choose whether or not to set your repo to be Public or Private--it's your choice!

(This will not impact who can see your site. It'll just impact who can see the *repository* for your site.) It's probably best to set your visibility to Private.)

3. Click "Create Repository"

## 3. Great a Second Github Repository for your Project

Now you want to create a separate repository for your course project. You will have a special url like: `<github-username>.github.io/<custom-path>`. You get to pick the `<custom-path>` for your site!

1. Navigate to [https://github.com/](https://github.com/) and click on the "New" button to create a new repository.

2. Name your repository `<custom-path>` where `<custom-path>` is whatever you choose! Set the repository visibility to Public. 



## 4. Publish Your Site to Github

Now we want to link the site you just cloned to visual studio to Github!

Open Visual Studio and then open the directory that you just cloned.

### 4.1 Update Your Site Configuration

1. Open the file `_config.yml`

2. Modify the line `baseurl: ""` to be `baseurl: "/<custom-path>"` where `<custom-path>` is the path you chose before.

3. Modify the line `url: ""` to be `<github-username>.github.io` where `<github-username>` is your github username.


### 4.2 Link to Github

1. Open the command palette, and type `Git: Initialize Repository` you can select `personal-site.github.io` as your workspace folder.

2. Open the command palette again and type `Git: Add Remote` and input the link to your git repo (`https://github.com/<github-username>/<custom-path>`). When prompted, you can name your remote "main".

3. Commit your changes and push to origin!


## 5. Configure a publishing source for your GitHub Pages site

*(It is possible that this step will be automated for you! You can check by going to your site URL: `<github-username>.github.io/<custom-path>` and seeing if anything shows up! It may take a few minutes.)*


Follow steps 1-8 [here](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-from-a-branch). For step 1, you can choose your "main" branch.

<!-- 

<img class="img-fluid" src="/static/assets/f23/pages-branch.png" alt="Image of Github Pages settings page under the 'branch' header. 'main' is selected as the branch. "  /> -->

After you do this, your site should be live at `https://<github-username>.github.io`


## 6. Add Content + Make it Pretty

You'll want to start by further modifying the `_config.yml` file to add some info about yourself!

For your actual assignment webpage, you'll want to edit the `index.md` file. The language you will be using to write this is called markdown--the same language you used in your Jupyter notebook text cells! There's some guidance in the file for basic syntax.


### Optional Styling
You can also change the Jekyll theme of your site to style it!
Here is a list of the currently supported themes: [https://pages.github.com/themes/](https://pages.github.com/themes/). Click on the Theme you want and it'll give you instructions on how to install it!


# More Info
More info for general debugging can be found [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=mac)

For this assignment, you created an empty repository named `<github-username>.github.io`. If you want to actually populate that repository and host a personal/professional website on Github, you can find instructions to do so [here](https://alyssalytle.github.io/resources/personal-site.html).