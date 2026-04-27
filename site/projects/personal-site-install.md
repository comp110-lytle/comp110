---
title: Setting Up a Personal Website
author:
  - Alyssa Lytle
layout: page
---

# Setting Up A Personal Website

Here are the instructions for setting up a personal site if you are looking for a little more control over the design and implementation of your site!

## Create a new Jekyll Project

we're going to set up a new Jekyll project. Jekyll is a static site generator. It helps you build a prettier site and has some really nice features!

0. First, make sure you have all of the prerequisites installed by going to [this link](https://jekyllrb.com/docs/installation/) and checking under the "Requirements" tab.

1. Open your terminal and use the `cd` command to navigate to wherever you want to have your site. For example, I'll want my site file to be stored in documents, so I'll type `cd Documents`.

2. Now run the following command to install Jekyll: `gem install jekyll bundler`

3. To create your first Jekyll project, run the following command: `jekyll new --skip-bundle <site-name>`, where `<site-name>` is whatever you want to call your site.

4. Now, you'll have a folder entitled `<site-name>`! Open Visual Studio and then open the directory site you just created! (If you installed it in your Documents folder, it'll be inside Documents > `<site-name>`).

5. You'll see a file called "Gemfile". Click to open that file. We are going to modify it!

6. In Gemfile, Add "#" to the beginning of the line that starts with `gem "jekyll"` to comment out this line.

7. Add the github-pages gem by editing the line starting with `# gem "github-pages"`. Change this line to:
`gem "github-pages", "~> 228", group: :jekyll_plugins`<br/>
then save and close the Gemfile!

8. In your terminal, run `bundle install`


## Continue With Instructions
Now, you can continue with the [original instructions](/projects/personal-site.html) starting at step 1. 


## More Resources


Now that you have Jekyll installed, you can change the Jekyll theme of your site to style it!
Here is a list of the currently supported themes: [https://pages.github.com/themes/](https://pages.github.com/themes/). Click on the Theme you want and it'll give you instructions on how to install it!

More info for running your site locally and general debugging can be found [here](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll?platform=mac)