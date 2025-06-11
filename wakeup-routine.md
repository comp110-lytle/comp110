---
title: Bedtime Routine
author:
- Kris Jordan
- Alyssa Lytle
---


# To do 


## Bedtime

* Put the previous semester to bed via `bedtime-routine.md`




## On-ramp New Team Members
  * Acceptance Message
  * Invite to Slack
  * Add new members to Team 110 Airtable
  * Send info on registration for ShiftOverflow/Homebase
  * I-9 information to HR
  * Plan orientation meeting before all-hands (slides in last semester's Drive folder)
* Add to CSXL course

## Ramp-up Team 110
* Start of semester survey
  * Get availability for open house and all hands
* Schedule first all-hands
* Bring members into Canvas site as TAs
* Bring members into Gradescope site as TAs
* Update team site
  * Update shift lead form link on shift_leads.md
  

## Update Website

### Getting Started Instructions
  * Update version requirements and OS versions / instructions
  * Setup Hello World exercise

### Support Page

* Update Course.Care info with new code (deprecated?)

### Calendar

### Syllabus
  * Quiz Dates
  * Meeting Days/Times
  * Weights of grade components
  * Difference between sync/async sections
  * Update links to forms (and duplicate forms)
    * Quiz Absence Request form
    * Feedback and Grievance forms
    * Final Exam Absence form
  * Post to OSM


## Setup course sites
  * Canvas site
    * Make announcement on where to find course site (once live)
  * Link with Gradescope to create Gradecope course

  * In Gradescope
    * When ready for students import from Canvas
  * Course.Care
    
  * GitHub
    * Create a new org: comp110-YYt eg comp110-20f
    * Upgrade the org here: https://education.github.com/toolbox/offers/github-org-upgrades
    * Create a PUBLIC github org site repo: comp110-YYt.github.io (make sure it belongs to the organization)
    * Touch one file in this repo so that it's not a bare/empty repo
    * Update the args in `.github/actions/deploy-site/action.yml` for building site via Github Actions
    * Setup DNS to point to the correct new site
      * CNAME that points to comp110-YYt.github.io for 1 day
    * Enable GitHub Pages in the new repo
      * Pages -> Source -> main (root)
      * Custom Domain: YYt.comp110.com
      * Enforce HTTPS
    * Setup course workspace repo in the org:
      * Checkout repo at this commit, add remote to new workspace repo, push main from this commit (unless there are changes needed)
    * Setup a classroom for the org: classroom.github.com
      * Create a new assignment (this will be the students' workspace for the semester)
      * Title: COMP110 Workspace
      * Prefix: comp110-workspace
      * Leave the repo template starter code blank
      * Copy workspace starter URL and update documentation (and README in workspace)
      

## Scheduling
  * Schedule tutoring room
  * Schedule all-hands meeting room
  * Schedule final exam makeup room
  * Ask help@cs.unc.edu to unlock doors if the final exam makeup takes place on a Sunday and the doors aren't already [scheduled to be unlocked](https://calendar.google.com/calendar/u/0/embed?src=cs.unc.edu_k2nl1c88kc5uu8ivhv1vr5ruso@group.calendar.google.com&ctz=America/New_York)