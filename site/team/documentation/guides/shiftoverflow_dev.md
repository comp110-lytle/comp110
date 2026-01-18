---
title: ShiftOverflow Dev
date: 2021-03-24
author:
  - Madison Huber
page: logistics
template: overview
site-branch: team
---

## Getting Started

[This video](https://youtu.be/vOWy25FGr7I) provides an overview of how ShiftOverflow development works and the steps to get started on the project.

To work on ShiftOverflow you will need to be granted access to the repository by someone who currently has access to it (it is a private repository, separate from the team repository). You will also need to get the `credentials.json` file from someone who is currently working on or has in the past worked on ShiftOverflow. For secutiry purposes, we do not store certain credentials on GitHub, so once you have this file put it in the `server` directory within the overall `shiftoverflow.com` directory from when you cloned the repository.

Once you have access to the repository, following the steps in `README` will take you through the process to set up and run the project locally.

## Working on Features or Issues

1. When contributing to the codebase, make all your changes on a new git branch specific to the feature you are currently working on.
1. Once you feel your changes are done, make a pull request describing what your changes were and why you made them.

> - mentioning how you tested your changes (ex. what browsers and viewports you tested on)
> - including screenshots of what your changes look like in desktop and mobile views if they were changes to the UI

1. Before merging and deploying your code, your pull request must be reviewed and approved by at least one other person.

## Deployment Process

After your code has been approved, it is ready for deployment. The steps to deploy are described in the following subsections.

### Merging to Master

Once your pull request has an approving review, squash and merge it to master which can be nicely done using the pull request UI on GitHub.

After merging to master:

1. go back to your local ShiftOverflow development directory & open a terminal
1. run `git checkout master` then `git pull` to get the changes you just merged with the most recent code on the master branch
1. Run `npm run dev-local` and re-test all features of your changes to make sure they still work with the code from master (if you were not already working off the latest changes in the master branch)

### Preparation on the Server

If all is well after re-testing, `ssh` into the ShiftOverflow AWS server to get it ready for deployment. If you don't have this set up, check out the [guide for scheduling](/scheduling) for more information, or talk to Kris for help getting set up.

When deploying any code anywhere, there is a chance things will fail for whatever reason or unforeseen issues may arise. To avoid disaster and panic if this happens, make a backup of the app files and the database on the server before deploying.

1. From within the server, copying the app files can be done with `cp -r /var/apps/shiftoverflow/build/ ~/sobuildbu`. This copies the contents of the `build` directory to the directory `sobuildbu`. If your changes affect other directories or files, copy those too before bringing in your new changes.

1. Copying the database can be done with a dump also from within the server:
   `sudo mysqldump -h comp110.clq5qdd6e8wc.us-east-1.rds.amazonaws.com -u shiftoverflow -p shiftoverflow > bu02_01_21.sql`

The part after the `>` is the name of the file you want to save this to. It is helpful to label with the date for quick future reference.

### Transferring Files to the Server

After testing and backing things up, it's time to transfer your changes to the server. To avoid the site going down during office hours, try to deploy during times office hours are not open.

1. First, run `npm run build` in your local ShiftOverflow development environment. The `build` directory and process of running or copying `build` handles all client-side code and changes.
1. Next, still in your local ShiftOverflow development environment copy the contents of `build` to the server with `npm run copy-build`.

If all your changes were client-side, this should be all you need to do and you should be able to see your changes on shiftoverflow.com.

If you made server-side changes too, you will want to copy those other changed files over as well with the following command, run from your local ShiftOverflow development environment: `rsync -r server git@shiftoverflow.com:/var/apps/shiftoverflow`. The next thing to do is run `sudo reboot` from the server which you previously ssh'ed into. This will stop and start the service because syncing the server while it's running isn't always reliable and quick. This may take a few moments, and if you refresh or load shiftoverflow.com while it's rebooting you may see a `502 bad gateway nginx error`. However, waiting anywhere from a few seconds to 5 minutes before reloading the page should display your changes.

If you made changes in the `shared` directory, you'll want to copy that directory over as well using the same `rsync` command from above like so: `rsync -r shared git@shiftoverflow.com:/var/apps/shiftoverflow`.

### Verification of Success and Production Testing

Once you are at this point, test your changes in production on shiftoverflow.com to make sure they work as expected when run on the server and not in your local environment. If something is not right, you can investigate and if necessary go back to the previously working version of ShiftOverflow by either:

1. reverting via git and repeating the deployment steps
1. utilizing the backups you made earlier on in this process

## Troubleshooting

If you see messages on the AWS server about having run out of space, a good place to start freeing some up is in `/var/log/journal`. You can get some context around that by doing `sudo du -sh /var/log/* | sort -h` on the server (the rest of the commands in this section are also to be done on the server).

1. To free up that space, run `cd /var/log/journal` to change into the `/var/log/journal` directory.
1. run `ls` to see the contents of this directory, which should output a hash-looking thing (ex. `198a6518d83c4c89b805fb52c91f0316`)
1. Next, change into that directory by doing `cd 198a6518d83c4c89b805fb52c91f0316` (or whatever output you had)
1. Here, run `sudo journalctl --disk-usage` to see usage information
1. Then (being sure you are in this same directory) run `sudo rm *` to remove that log information and free up space.

If you make server-side changes and restart the service but still see 502 bad gateway errors even after waiting several moments, you can try manually running `npm run start-server` from the `/var/apps/shiftoverflow` directory (`cd` there if needed) to go through the server starting process in a way that will display any errors that occur. If errors appear here, it may have to do with your code, so look closely and double check that everything that you have locally was copied over and is located on the server (if it is being referenced).
