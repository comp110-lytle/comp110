---
title: Set Up Your TA Profile
date: 2020-09-27
author:
  - Ezri White
  - Kaki Ryan
  - Meghan Sun
page: logistics
template: overview
site-branch: team
---

**These instructions will walk you through setting up a profile visible on the 110 site!**

## Setup

<p style="color:orange">Send your `github` username through `slack` to the [website lead](/team/documentation/leads/website.html) so they can add you to the 110 team on `github`! Make sure to check your email for an invite and accept it before it expires.</p>

If you have not set up the team110 repository yet navigate to [this doc](/team/documentation/guides/course_site_setup.html) and follow the instructions for cloning and installing various packages.

If you have the team repo and can successfuly run either `python -m dev` or `python -m hotdev` you are good to go!

## Creating a Profile

1. Make sure you're on the main branch (`git checkout main`) and run the command `git pull origin main` to get the latest updates.
2. Checkout a new `git` branch. In your terminal run the following command, replacing ONYEN with your onyen:
   `git checkout -b ONYEN-profile`
3. In the `site/static/profile-photos/` directory insert the photo of yourself you want on your profile. Resize this image to be exactly than **300x300** and name it `ONYEN`.png/jpg
4. In the `site/resources/profiles` directory create a new markdown file named `ONYEN.md` (replacing ONYEN with your onyen). Feel free to just paste the contents of someone else's profile into yours and fill in the relevant information. You'll want to make sure the relative path to your profile picture is correct. Note: Make sure the file extension of your photo in the `static` directory and the extension in this path match -- it is case sensitive! Doesn't matter if you have PNG or png, just be consistent.

## Styling your Profile

1. Navigate to your profile on the dev server by adding /resources/profiles/`your-ONYEN`.html
2. Here you can make sure everything looks ok and add any extra styling or visual elements like emojis! For instance some TAs have their star signs with emojis or so on.
3. Please take a minute to check out the [Site Markdown](/team/documentation/guides/course_site_markdown.html) and [Site Features](/team/documentation/guides/course_site_features.html) docs to see if there is anything you can learn from these that you may want to add to your profile! For instance, TAs have made use of the `columns` template for their profiles in the past.

##### Examples of Profile Markdown Styles:

**Single Column**

```

  title: Meghan Sun
  author:
    - Meghan Sun
  page: profile
  ---

  ![profile-photo](../../../static/profile-photos/meghansun.png)

  ## Pronouns

  she/her/hers

  ## Hometown

  Chapel Hill, NC


```

**Multiple Columns**

```

  title: Meghan Sun
  author:
    - Meghan Sun
  page: profile
  template: columns <- ADD TEMPLATE SECTION IF YOU WANT COLUMNS!
  ---

  ![profile-photo](../../../static/profile-photos/meghansun.png)

  ## Pronouns

  she/her/hers
  //split// <- EACH SPLIT CREATES A NEW COLUMN (what's above is a column, what's below is another - recommend using 2 splits)

  ## Hometown

  Chapel Hill, NC


```

## Linking to your Profile

1. Open the file `resources/team.md`. This file uses the grid layout which is described in the Site Features document!
2. Find where your name would list alphabetically and add in your profile link by copying and pasting the following code and filling in your info:

```

  <figure class="profile col-xs-12 col-sm-6 col-md-3">
    <a href="/resources/profiles/meghansun.html"><img src="/static/profile-photos/meghansun.png" class="profile-image"> </a>
    <figcaption>Meghan Sun</figcaption>
  </figure>


```

3. Make sure to switch the link to your profile, the link to your image (watch out for .png or .jpg here), and the caption to your name!
4. Navigate to the meet the team page on the dev server by adding `/resources/team.html` to the URL and make sure the page looks ok, your picture is there and when you click on it you are navigated to your profile!

## Creating a Pull Request

1. If you haven't been committing progress on your profile to the branch you setup for it... commit it!
   To do this, first add the files you've changed to the staging area:
   `git add <../site/static/profile-photos/ONYEN.png> <../site/students/profiles/ONYEN.md> <../site/students/resources/team.md>` or you could simply run `git add .` to add every single change file at once.
   Then commit your changes:
   `git commit -m "your_name Profile Page."`
1. Push your work to your training branch on the staff repo (`git push origin [your-branch-name]`). Check your branch with `git branch`.
1. Open GitHub Pull Requests on the `comp110` repo: https://github.com/comp110-lytle/comp110/pulls
1. You might/should see a yellow notification box: "Your recently pushed branches...". If so select "Compare & Pull Request". If not, select "New Pull Request", and in the Compare branch drop-down select your branch.
1. Scroll through the differences and confirm your latest changes were successfully pushed. If you don't see them, check that you committed everything you expected and pushed to your branch. Select "Create Pull Request".
1. In the description box, briefly describe your branch -- "<Name> Profile Page" is just fine.
1. On the right-hand sidebar, select Alyssa or a Web Lead as a reviewer.
1. Create pull request!

From here, a brief pass (and potentially some some revisions) will be taken by the reviewer and then merged in.
