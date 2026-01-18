---
title: Markdown Example
author: 
- Ezri White
page: resource
template: overview
---

# Heading 1
These are the different heading sizes available.

## Heading 2
When the overview template is used, they also can appear in a table of contents like you see on the right.

### Heading 3
Notice that headings sizes are nested based on which size they are.

#### Heading 4
Keep in mind that heading 4 will not show up in the table of contents.

# General Styling

>To highlight blocks of text follow this format.

**To bold text follow this format**

_To italicize text follow this format_

# Bullets and Numbering

You can create lists with the following formats: 

* Exercises
* Projects
* Conceptual Questions
* Lecture Review

1. Exercises
2. Projects
3. Conceptual Questions
4. Lecture Review

# Images and Links

## Links
Sometimes we want links to reuse the same tab when redirecting the browser, but sometimes we want them to open a new tab and leave the course site up.

### Linking Internally
 
When linking to another page on the course site, follow this format:

[Style, Linting and Reading the Autograder](/resources/style-guide.html)

### Linking Externally

When linking to a page off the course site, follow this format:

<a href="https://www.alexandrato.com/papers/Critical_Race_Theory_for_HCI.pdf" target="_blank" rel="noopener noreferrer">Critical Race Theory for Human-Computer Interaction</a>

Note that in this case we can just use html to achieve our needs. This is a pattern you can make use of! While we want to avoid it, if you can not achieve your desired effect with simple markdown, you are able to also put html into the markdown files and our dev and prod scripts can parse it fine!

## Image

![](/static/assets/support/officehours.png)

# Code Blocks

Keep in mind that code blocks show up slightly off when viewing on the dev server. To see what code blocks will look like once they are published to the course site visit this page on the published site -> https://21s.comp110.com/markdown-example.html

For shorter code blocks, line numbers are not that helpful so use this formatting.

~~~ {.python }
if <conditional statement>:      
   # code to execute
~~~

For longer code blocks, line numbers are helpful for describing specific lines to students. Use the formatting below.

~~~ {.python .numberLines startFrom="1"}
if <conditional statement>:    
    # code to execute
else:
    # code that executes when conditional statement is false
~~~





