# Autograder

For a more detailed guide, check out [Vrinda's Documentation](https://docs.google.com/document/d/1PCSGjEBVsBgT2_Ze_Jf_MBTSi5Fyx5-ElopUY3Vijsc/edit?usp=sharing).

## Setting Up in VS Code

Check if your version of python is >= 3.8 by running the shell commands `python --version` or `python3 --version`.

Make the `team11/code/autograder` directory your current working directory. 

Update PIP and install the library packages with the commands

```
python -m pip install -U pip
```
```
python -m pip install -r requirements.txt
```

Then use the command 

Required packages include:
- `pytest` for unit testing
- `mypy` for static type checking
- `flake8` for linting
- `jinja2` for template generation

## Testing Graders

### Passing Example
Once you’re in the correct directory, run the command

```
python -m setup.hello_world
``` 

The solution script found in setup/hello_world.py will be executed to print out “Hello world.” 

Then run command 

```
python -m grading.test graders.setup.hello_world
``` 

which runs the autograder found in the `graders.setup.hello_world` module. The grader should return a report with a 100% score and tests passing.

### Failing Example
Run the command 
```
python -m grading.test graders.setup.failing
``` 
all three tests should fail. 

## Grader Breakdown
There are a few working parts that make the autograder run. Note that the exercises directory includes all reference solutions, the graders directory includes your actual tests, and the grading directory includes the modules that help coordinate output and building. See this for yourself by checking out each of these directories.
The Solution: Everytime you set out to create a grader, you will also need to create a reference implementation of the project you will be evaluating. This will typically go in the exercises folder, however, for the sake of the following practice example, you will utilize the training folder.

- The `__main__.py` File:  This file serves as the autograding package runner—note that while the file is placed inside a directory, it makes the entire directory runnable. 
- The Pytest File: You will put your tests into the pytest files that all end with _test.py . These files exist in the same directory as the `__main__.py` file.
- Other Things: Evidently, there are many other files involved including the entire grading directory. Visit the Helpers and Modules section to better understand what is going on.

## Make Your First Grader
Now that you’re sure all components are working, let’s practice making a grader. 

### 1. Create a New Branch

Before you make any changes in the directory, create a new branch by running the command 
```
git switch --create grader-training-ONYEN 
```
in the terminal. The reason for creating a new branch is so you can experiment in the Team Repo without making any fatal changes. To check what branch you are in, run the command `git branch`.  If you are not interested in keeping your final changes, run the command `git switch master` to return to the master branch. Otherwise, to keep your changes, run the commands listed in the Saving Your Changes section. 

### 2. Check Your Working Directory
Make sure you are in the correct working directory which reflects the current semesters files: `/team110/code/autograder`. 

### 3. Reference Implementation
Begin with your exercise implementation which can be an arbitrary piece of code. Name the file `[yourONYEN].py` and place it in the training directory (`team110/code/autograder/training`). 

The topic and theme of this “assignment” is completely up to you. This is the piece of code that you will run your unit tests on. The implementation should follow the conventions of any 110 assignment including an `__author__` var, docstrings, and so on. Make sure you are able to run the program with the command `python -m training.[yourONYEN]`.

### 4. Create the Grader’s Directory
Within the graders/training directory, create a folder that will hold the files necessary for your grader, name it after your ONYEN. 

### 5. Main Module
Within the folder you just created above, create a file named `__main__.py`. You can use previous examples as a template.

You can run this grader package directly with the command 
```
python -m graders.training.ONYEN
```

However, you will see that the JSON printed is in the results.json that Gradescope expects! Instead, for a much prettier output, try running the 

```
python -m grading.test graders.training.ONYEN
``` 

At this point, the Type Safety and Lint tests should pass.

### 6. Unit Testing
Finally, let’s get into the meat of your work: unit testing. Create a file named `training_test.py` inside of the folder named after your ONYEN. Begin filling in unit tests based on the template below  to evaluate a piece of code for accuracy and robustness. 

### 7. README.md
Last but not least, create a file called README.md in the same ONYEN directory as your other files. 

Be sure to include the following content in your README:
- Title and Short Introductory Description
- Setup Instructions: What students need to do in their workspace directory to begin working on the project?
- (Optional) Guided Instructions: When the project is substantial enough to require step-by-step guidance at parts, add a section for it.
- Requirements: Technical requirements the unit tests will certainly check for.
- Formatting and Documentation:  Expectations for documentation which is standard throughout the semester.
- Code Review: Details that TAs may look for in manual grading.

### 8. Save Your Changes
Your practice grader looks great! To save these changes, enter the command 
```
git commit -m “You message here.” 
```
with a message of your choice in the terminal. Then, enter the command 
```
git push origin [branch-name]
```
 which in this case [branch-name] should be replaced with grader-training-ONYEN . 
 
 Next, switch back to the master branch with the command 
 ```
 git switch master.
 ``` 
 
 Merge in your changes with the command 
 
 ```
 git merge [branch-name]
 ``` 
 where again, [branch-name] will be grader-training-ONYEN. Finally, push these changes with the command
 
 ```
 git push origin master
 ``` 
 Your changes will only be pushed if you have been added as a Contributor in GitHub. You should see your changes in the online repo if you were successful. 

## The Real Deal 
Your practice grader looks great! Now, what about a grader for an actual 110 assignment?
Piece of cake. Follow the exact same steps as the tutorial, except take care of the following notes:
You should still `git switch --create [branch-name]` to a new branch with a name that includes your ONYEN and the task you are taking on.
Instead of utilizing the respective training directories (`team110/code/autograder/training` & `team110/code/autograder/graders/training`), you will utilize the exercises directories.


As a reminder, `team110/code/autograder/exercises` will contain the reference implementation and `team110/code/autograder/graders/exercises` will contain the grader package.

The name of the reference implementation files is what we will expect students to name their own submission files. The path of the files should also follow from how we have it set up in our own repo—thus, we cannot create a grader for exercises in the training directory.
As assignments grow larger, your unit test may span across more than one `_test.py` file. You do not need to limit yourself to just 1 file.
You may also need to utilize more complex functionality beyond just assertions, check out the Helpers and Modules section to see what resources are at your disposal.

## Deploying a Grader
When you are ready to deploy the grader to Gradescope, complete the following steps:
Run the command 
```
python -m grading.build [grader_module]
```

which generates a .zip file with all of the necessary contents. 

Next, locate your zip file and open the `run_autograder` file and modify the `GRADER` variable to be correct if it is not.

Find the assignment in Gradescope and click “Configure Autograder.” Then select “Update” or “Replace Autograder” and upload your own `.zip` file. 

Go back to VS Code and generate a submission `.zip` for your reference implementation using the command `python -m grading.submission [directory or file]`. 

Once your autograder builds successfully in Gradescope,  select “Test Autograder” and upload the .zip file for your reference implementation. 
If your autograder was scoring 100% locally, it should score the same on Gradescope. All tests should be visible. If you can see only linting or otherwise, this may be a dependency issue. Go ahead and contact Alyssa.



