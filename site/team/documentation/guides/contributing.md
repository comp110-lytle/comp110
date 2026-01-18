---
title: How to Edit this Site
date: 2021-01-21
author:
- Christine Mendoza
- Chiazo Agina
page: logistics
template: overview
site-branch: team
---

## Setting up the Repo Locally

Clone the repository (https://github.com/comp110/team110) to VSCode.

- **Any errors?** Try this:
  > If you can't open this link, you have not been added to the team org on Github. Send your github username to Kaki!

1. Run these 3 commands separately to enter the team site directory, install the site's packages and to see your live changes at **localhost:8000** (Note: Make sure that you have installed node.js):

   > `cd team.comp110.com` > `npm install` > `npm run start`

1. Make your changes! Within the `src` folder there exist 4 important folders:

   ![](/static/team/repo-instructions/step_4.png)

> `components` - this folder contains React/Gatsby components that will be shared across multiple pages or the entire site. A great example is `footer.js`; each page on the site shares the same footer! The most important file here is `layout.js`. It is wrapped around every page and imports in a `Header` and `Footer` component. If you make a new component, be sure to _import_ and _export_ it into `index.js`. This will be helpful later.

> `pages` - this folder contains two types of pages. The first are the markdown pages stored in `pages/markdown/`. This is where you'll add new guides or proposals. Make sure to add a `slug`, `title`, `date`, and `author` at the top of your markdown files. Feel free to make new folders in `pages/markdown`, everything will be rendered recursively. If you want to change the location of the markdown, be sure to update the path in `gatsby-config.js` in the `gatsby-source-filesystem` plugin. The second type of page here are those that contain components in React/Gatsby. An example would be `guides.js` which renders the preview of every markdown file as a div with a title. This is where you'd go to make new pages that aren't based in markdown. The name of the component will be the page on the website. For example `about.js` exports the `About` component and is found at the `/about` path of the website.

> `styles` - this folder contains all the CSS/SASS the site uses. As a matter of good practice, create a new file for each page you create beginning with an `_` and ending in `.scss` (for example: `_gallery.scss`). Then, import this new file into `styles.scss` using an `@` symbol (for example: `import @gallery`). SASS is super cool because you can use global variables and use math to expand the capabilities of CSS. Please try to define a new color variable in `styles.scss` and reference it using a `$` symbol in subsequent `scss` files. Try to avoid inline styling when possible so that we know the best place to easily change the look of the site. A couple colors to be aware of are: `$base-color`, `$highlight`, `$purple`.

> `templates` - this folder contains templates for specific types of Gatsby queries. Currently, it only has a template for `markdown` files. If you want to get rid of the date requirement for all `.md` files, you'd simply remove the line in this `markdown.js` file referencing `frontmatter.date`. It also contains some code to create the table of contents on each `markdown` page!

Create a branch by writing:

- `git checkout -b <branch-name>`
  > example: `git checkout -b christine-profile`

## Pushing to Github

Prepare the branch locally by running the following lines of code:

- `cd ..` (this moves you back to the team110 directory)
- `git add .` (this will prepare all your changes to be uploaded to github)
- `git commit -m "<commit message here>"` (a short statement describing what you did)
- `git push origin <branch-name>` (this uploads your draft to github)

Go to **Pull Requests** on the team repo and click the green button to make a Pull Request. On the side where it says **Reviewers** add someone to review your work (for now choose the documentation lead)!

> Contributors: Christine Mendoza, Chiazo Agina