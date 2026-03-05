---
title: Styling and Features Documentation
date: 2021-02-25
author:
  - Ezri White
page: logistics
template: overview
site-branch: team
---

> Detailed below are some extra styling and layout features you can use, outside of what is possible with markdown.

# Page Layouts

There are currently 3 different layouts you can use. To switch page layouts, change the `template` variable at the top of your md file.

- The most basic layout is called `generic` and will result in a full width page.
- The second layout is `overview` which will add an overview/ table of contents side bar to your page.
- The third is `columns`. To use the columns layout, in each place where you would like your markdown content to split into a new column add the text `//split//`. You can add many columns this way but it will start to look bad so make sure to view your page before commiting.
- The fourth is `rows`. To use the rows layout, in each place where you would like your markdown content to split into a new row add the text `//split//`. You can add as many rows as you like but make sure to view your page before commiting.
- The last is `grid`. To use the grid layout, in each place where you would like your markdown content to split into a new section add the text `//split//`. You can add as many sections as you like. You will also need to add a global variable called `row-length` and assign it an `int`. This will determine how many sections get put into each row of the grid. Make sure to view your page before commiting. (Check out `site/resources/team.md` for an example)

> Note: When using `//split//` make sure to have no space below it. Pandoc and jinja do not parse this well.

# Page Specific Styling

There are some cases in which you may need to add css styling that only applies to your page. This is a feature that is not yet widely used but can come in handy!

- To use this feature, in the 'global variables' at the top of your md add a `page` variable and set it to a string value without spaces that describes your page. Keep in mind, you can reuse the same specific styles with the same name on other pages.
- This essentially wraps your content in an ID called `your-string-value-page`. (Note the `-page` gets added on by the parser.)
- Then in the css file (site/static/style.css), find the section labeled PAGE SPECIFIC STYLING and place your css rules here.
