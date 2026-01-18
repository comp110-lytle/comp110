---
title: Writing Markdown for the Course site
date: 2021-02-25
author:
  - Ezri White
page: logistics
template: overview
site-branch: team
---

Most content on the course site is just written in markdown(md). This guide walks through the associated styles for different markdown. If you are not starting a new file from scratch and are instead contributing to a file, I would still reccomend viewing the example markdown in [this step](/course-site-markdown#setting-up-your-file) if it is your first time contributing.

## Preparing to work

Make sure you have the dev script running so that you are able to view your work! Run in the `site` directory:

`python -m dev`

or

`python -m hotdev`

The normal `dev` script will run a dev server where you will need to reload to see any changes. For small changes, mostly written work or editing scripts/ code this is the better dev script to use.

The `hotdev` script will run a dev server that will hot-reload a page when you edit the markdown or css files it is built from. This script is particulary useful for styling a page and making css changes.

## Creating a new file

Generally we want to keep the site organized so try to put your files in an appropriate place. For instance if your file will live under the resources tab, make sure to put it under resources.

- When creating your md file, name it something that makes sense for your work and then end the file name with .md so that the dev and prod scripts know how to parse it. If the file name has multiple words, we generally use the convention of separating them with dashes.

## Setting up your file

- Find the file `markdown-example.md` directly in the site directory and open it.
- In your local version of the course site (the one opened by the development script) add `/markdown-example.html` to the end of the URL. (There is nothing on the course site that links to this page, so you will have to manually navigate to it.)

This markdown sheet should give you a good reference point for how all different kinds of markdown will show up as you write it.

> You are absolutely welcome to edit this file for learning and experimentation BUT make sure to not commit or push any changes to it.

- Go ahead and copy the contents of this file into your new file.
- Once you have filled in your file with the starter content you should be able to view your file. The file paths of the course site are determined by which directories they reside in. If you placed your new file named `function-examples.md` inside the `practice` directory inside the `resources` directory, then you could navigate to this file by adding `/resources/practice/function-examples.html`.

## Last Steps

Once you have successfully navigated to your new file there are a few more things to take note of before you are ready to add your own content!

- Note that the title shown on your page corresponds with the `title` variable at the top of the md file. Edit this to change your page title.
- Make sure to add your own name under the `author` variable. If you are adding on to a page, you still deserve credit so make sure to add your name to `author`!

For more information on how to make use of the other `global variables` at the top of your page check out [this guide](/team/documentation/guides/course_site_features).
