---
title: Setting Up a Personal Website
author:
  - Alyssa Lytle
page: resources
template: overview
navbar: base
---


# Create a new Jekyll Project

we're going to set up a new Jekyll project. Jekyll is a static site generator. It helps you build a prettier site and has some really nice features!

0. First, make sure you have all of the prerequisites installed by going to [this link](https://jekyllrb.com/docs/installation/) and checking under the "Requirements" tab.

1. Open your terminal and use the `cd` command to navigate to wherever you want to have your site. For example, I'll want my site file to be stored in documents, so I'll type `cd Documents`.

2. Now run the following command to install Jekyll: `gem install jekyll bundler`

3. To create your first Jekyll project, run the following command: `jekyll new --skip-bundle <site-name>`, where `<site-name>` is whatever you want to call your site.

4. Now, you'll have a folder entitled `<site-name>`! Open Visual Studio and then open the directory site you just created! (If you installed it in your Documents folder, it'll be inside Documents > `<site-name>`).

5. You'll see a file called "Gemfile". Click to open that file. We are going to modify it!

6. In Gemfile, Add "#" to the beginning of the line that starts with `gem "jekyll"` to comment out this line.

7. Add the github-pages gem by editing the line starting with `# gem "github-pages"`. Change this line to:

`gem "github-pages", "~> 228", group: :jekyll_plugins`

Then save and close the Gemfile!

8. In your terminal, run `bundle install`

# Creating a Github repository for your site named `<github-username>.github.io`
Now you need to connect this directory to Github!

1. Navigate to [https://github.com/](https://github.com/) and click on the "New" button to create a new repository.

2. Name your repository `<github-username>.github.io` where `<github-username>` is your github username and choose whether or not your repo will be Public or Private. (This will not impact who can see your site. It'll just impact who can see the *repository* for your site.) It's probably best to set your visibility to Private. This will give you some permission limitations when pulling/pushing to github though, so you'll have to [set up an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account) and use it to connect your Github account with your computer.

3. Click "Create Repository"


# Linking Your Site to Github

Now we want to link the site you just made on your computer with Github!

1. Open Visual Studio and then open the directory site you just created! (If you installed it in your Documents folder, it'll be inside Documents > `<site-name>`).

2. Open the command palette, and type `Git: Initialize Repository` you can select `<site-name>` as your workspace folder.

3. Open the command palette again and type `Git: Add Remote` and input the link to your git repo (`https://github.com/<github-username>/<github-username>.github.io.git`). When prompted, you can name your remote "origin".

4. Commit your changes and push to origin!


# Configure a publishing source for your GitHub Pages site

*(It is possible that this step will be automated for you! You can check by going to your site URL: `<github-username>.github.io` and seeing if anything shows up!)*


Follow steps 1-8 [here](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-from-a-branch). For step 1, you can choose your "main" branch.



<img class="img-fluid" src="/static/assets/f23/pages-branch.png" alt="Image of Github Pages settings page under the 'branch' header. 'main' is selected as the branch. "  />

After you do this, your site should be live at `https://<github-username>.github.io`


# Add Content + Make it Pretty
You'll want to start by modifying the `_config.yml` file to add some info about yourself!

You can also change the Jekyll theme of your site to style it!
Here is a list of the currently supported themes: [https://pages.github.com/themes/](https://pages.github.com/themes/). Click on the Theme you want and it'll give you instructions on how to install it!

*(I'll add more here later.)*

# More Info
More info for general debugging can be found [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=mac)