---
title: Web Development
author:
  - Ezri White
page: explore
template: overview
---

## Getting started

> In this tutorial you will create a website with the beginnings of a Harry Potter House quiz! We will learn some basic HTML, CSS and Flask and your website will be able to save data to render on different pages while it is running. Flask is a python library used for web development and is actually what we use while developing this course's website!

We will begin this tutorial from scratch! Start setting up the following to prepare:

1. On github.com, click the green New Repository button and name the repository `web-dev-tutorial`.
   - Leave it public
   - Check the Add a README option
2. Navigate to the repo you just created on github and click the green code button. Copy the HTTPS URL from the box that opens.
3. Open VSCode and then at the top of your screen click View > Command Palette.
   - In the command palette start to type `Git:Clone` and hit enter.
   - Paste the URL in the box that pops up and hit enter.
   - You can leave the location on your computer as default or select a location you prefer.
4. Open your newly cloned repository in vscode!

## Languages and Tools

HTML and CSS are the building blocks for the entire web. They are markup languages used for defining and styling content. The final tool needed for basic web development is a scripting language. Javascript or Typescript are the most commonly used scripting languages in web development, but in this tutorial we will use python.

> HTML stands for HyperText Markup Language and is the standard languge used for defining content on web pages! CSS stands for Cascading Style Sheets and is what we use to style the content defined with HTML.

### Task: Developer Tools

1. Navigate to an online news article or website that you visit frequently **on google chrome**. This page is made with HTML and CSS as core building blocks and we can actually inspect them!
2. At the top of your screen select View > Developer > Developer Tools.
   - Mac shortcut: Option + ⌘ + J
   - Windows shortcut: Shift + CTRL + J
3. Select the arrow tool in the top left corner of the tool box. You can use this tool to inspect specific elements and edit them in browser!
4. Using the tool, select the headline or title of the page you are on. You should see the HTML for that headline pop up in the Dev Tools Box. If you double click into the text you can go ahead and edit it!

Developer Tools are one of the most important things to make use of when working on a web project so make sure to take note of how to access them!

## CSS and HTML

A basic webpage can be created with a single file and styled with a second. From there you can continue to add new page and evolve your website!

### Task: index.html

1. Make a new file in your repository named `index.html`. This file name is a convention for the HTML file that represents your home page.
2. Copy and paste the following HTML snippet into the file:

```{ .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Intro to Web Dev!</title>
    </head>
    <body>
        <p>Hello World!</p>
    </body>
</html>
```

3. Make sure the file is saved and then right click the file in the file explorer and click reveal in finder (Mac) or show in folder (Windows).
4. In finder / file explorer, right click on the file and open it with google chrome. You should now see a basic webpage that says Hello World!

### HTML Tags

So what exactly did we add to the `index.html` file? HTML is made up of elements wrapped with `tags` that help label pieces of content. For instance, The `<p></p>` tag that surrounds `Hello World!` indicates that we are adding a `paragraph` element to our webpage.

These `tags` can hold other `tags` as well!
<!-- TODO: Talk more about basic html -->

### Task: styles.css

1. Make a new file in your repository named `styles.css`. This file name is a convention for the CSS file that holds the core styling.
2. Copy and paste the following CSS snippet into the file:

```{ .numberLines startFrom="1"}
p {
    color: #75c3f7;
  }
```

3. Make sure the file is saved and then add the following `link` tag inside the `<head></head>` tag in your `index.html` file. This will link your CSS file to your HTML file so that the styles we add are applied to our webpage.

```{ .numberLines startFrom="1"}
<link rel='stylesheet' href='styles.css' />
```

4. Once both files are saved, reload the chrome page with your webpage and you should see the color of the `Hello World!` text change!

<!-- ### CSS Selectors

TODO: add content on CSS selectores -->

## Basic Flask

<!-- TODO: blurb on code -->

### Task: Setting up Flask

1. Create a new directory in your repo named `templates` and move your `index.html` file inside of it.
2. Create a new directory in your repo named `static` and move your `styles.css` file inside of it.
3. Create a new file called `app.py` in your repo and add the following code snippet.

```{.python .numberLines startFrom="1"}
from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

4. Since we have moved the `styles.css` file we need to make sure to update our reference to it in `index.html`. Change `<link rel='stylesheet' href='styles.css' />` to `<link rel='stylesheet' href='/static/styles.css' />`.

5. To run your app we need to run the `app.py` file as a python module: `python -m app` and then open your browser to the link it spits out in the terminal (http://127.0.0.1:5000/)

<!-- ### Routes and URLS

TODO: Add content on routes / URLS -->

### Task: Adding a new page

1. Create a new file called `quiz.html` in your `templates` folder and paste the following HTML into it.

```{ .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Take the Quiz!</title>
    </head>
    <body>
        <form method="post">
            <label for="fname">First name:</label>
            <br />
            <input type="text" name="fname">
            <br />
            <label for="lname">Last name:</label>
            <br />
            <input type="text" name="lname">
            <br />
            <label for="animal">Favorite animal:</label>
            <select name="animal">
                <option value="lion">lion</option>
                <option value="snake">snake</option>
                <option value="eagle">eagle</option>
                <option value="badger">badger</option>
            </select>
            <br />
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
```

2. Return to your `index.html` file and add the following HTML element in the body.

```{ .numberLines startFrom="1"}
<a href="/quiz">take quiz</a>
```

3. If you attempt to click on take quiz while viewing your `index.html` file on chrome, you will get an error! This is because we need to define the route to the quiz URL in our `app.py` file. Add the following code snippet in `app.py`, save all the files, and attempt to click take quiz again.

```{.python .numberLines startFrom="1"}
@app.route('/quiz')
def quiz():
    return render_template("quiz.html")
```

## Handling Methods

In order to add interactivity to the quiz form on our site we need to learn about HTTP request methods. We won't need to know a lot about HTTP, but a simple definition is HTTP is a defined set of rules or protocols for fetching resources such as our HTML or CSS files.

Two of these rules are the `GET` and `POST` methods. The `GET` method is a basic protocol for viewing or _getting_ some resource such as our `index.html` file. The `POST` method is a protocol for updating or inserting new data. You can imagine when you _post_ something on social media the data is getting uploaded so that everyone can now see your post.

### Task: Form Submission

When we click the submit button that we defined in our `quiz.html` file, we want to show the user what result they got on the quiz. The easiest way to do this is by setting up a new HTML `template` that we will render instead of `quiz.html` when the user submits the form. For now we will hardcode the users result, but later we will actually evaluate the users answers.

1. Create a new file in your templates folder named `result.html` that will be used to show the result of the quiz. Add the following HTML to this file:

```{ .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Take the Quiz!</title>
    </head>
    <body>
        <p>You were sorted into ravenclaw!</p>
    </body>
</html>
```

2. Notice how the HTML for the form in `quiz.html` says `method="post"`. When you click the submit button inside the form element it will use the HTTP protocol `POST`. This makes sense since we are going to be saving or _posting_ new data for the users answers when they click the submit button. We can use this fact to render our result template in our quiz function. First, we will need to import the `request` ability from Flask. Update the Flask import at the top of your `app.py` file:

```{.python .numberLines startFrom="1"}
from flask import Flask, render_template, request
```

3. Now we are ready to handle different types of requests. Update your `quiz` function in `app.py` as seen below:

```{.python .numberLines startFrom="1"}
@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        return render_template("result.html")
    return render_template("quiz.html")
```

3. Now, when you click the Submit button when viewing your `/quiz` page, our function will check if the request method was `POST` and render a result if so. Otherwise, we will see our normal quiz page. Keep in mind that the route or URL in your browser still shows `/quiz` since all we changed is what is rendered in our `quiz` function.

### Task: Returning to Quiz

We also want users to be able to take the quiz again so we will add a button that lets us return to the quiz view.

1. Add the following HTML snippet into your `result.html` template underneath `<p>You were sorted into ravenclaw!</p>`:

```{ .numberLines startFrom="1"}
<form method="get">
    <input type="submit" value="Take the quiz again!">
</form>
```

2. In this `form` we specified that `method="get"`. This makes sense since we are just requesting the `quiz.html` view instead of updating or posting any data. We could now update our `quiz` method to the code snippet below, but it is actually logically equivalent to what we have already written since any method that is not `POST` will render our `quiz.html` file as a default so there is no need.

```{.python .numberLines startFrom="1"}
@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        return render_template("result.html")
    if request.method == "GET":
        return render_template("quiz.html")
    return render_template("quiz.html")
```

3. If you try clicking the `Take the quiz again!` button you should now see the quiz view. It should be easy to navigate between these two views now.

## Working With Data

When a user submits their quiz we want to be able to evaluate their result! Let's learn how to check what a user inputted into the quiz form.

### Task: Evaluating the Result

1. Once a user submits the form we will need a function that can check which house they will be sorted into. We could write this function in our `app.py` file but for organization we will add a helper file instead. Create a new file named `helpers.py`
2. Paste in the following function:

```{.python .numberLines startFrom="1"}
def find_house(animal: str) -> str:
    if animal == 'eagle':
        return 'Ravenclaw'
    elif animal == 'lion':
        return 'Gryffindor'
    elif animal == 'badger':
        return 'Hufflepuff'
    else:
        return 'Slytherin'
```

3. Currently the only question in our quiz is picking an animal, so our sorting function is pretty simple. Given the selected animal, this function can determine which house a user should be sorted into. In your own projects, this function could be more exciting! To use this function in our app, add the following import statement into your `app.py` file:

```{.python .numberLines startFrom="1"}
from helpers import find_house
```

### Task: Displaying the Result

Now that we have a function for sorting, all that is left is to grab the submitted data from the form and then display our result!

1. In order to show the result of the quiz we will need to add a variable into our `result.html` file. Change `<p>You were sorted into ravenclaw!</p>` to the following:

```{.numberLines startFrom="1"}
<p>You were sorted into {{house}}!!!</p>
```

> The `{{house}}` syntax is similar to what you have already worked with while using `f-strings`. In our case we are telling our `result.html` template to expect a `str` variable called `house`.

2. Now we need to make sure to pass the `house` variable to the `render_template` function. Update the `quiz` function to the following:

```{.python .numberLines startFrom="1"}
@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        animal: str = request.form['animal']

        if fname == '' or lname == '':
            return render_template("quiz.html")

        house: str = find_house(animal)

        return render_template("result.html", house=house)
    return render_template("quiz.html")
```

> - In this code snippet we first grab the date for the first name or `fname`, last name or `lname` and the chosen `animal` and store them into variables.

- Then we make sure that the user filled out both the first name and last name fields. If they didn't, we go back to the `quiz.html` view.
- If all fields were filled out, we use our `find_house` function to check the house and store it in a variable.
- Finally we pass our `house` variable to the `render_template` function.

3. Navigate to your `/quiz` page and take the quiz. When you press submit your webpage should display the correct house you were sorted into!

## Displaying Stored Data

### Task: Storing the Data

We also want to be able to keep track of the results of previous users and therefore need to be able to store our user data instead of just displaying it once. In modern web development, the handling, storing and fetching of data is what is usually called `backend` development. In our program we will do a simple version of this by storing our user data in global variables that our `app` file can access.

1. We want to use best practices while accomplishing this so we will now define a class for a `user` to keep our code organized and readable. In your `helpers.py` file add the following class:

```{.python .numberLines startFrom="1"}
class user:
    id: int
    first_name: str
    last_name: str
    house: str

    def __init__(self, id: int, fname: str, lname: str, house: str):
        self.id = id
        self.first_name = fname
        self.last_name = lname
        self.house = house
```

> We need users to be uniquely identifiable. For instance, what if we had two users named John Smith who were both Hufflepuffs? There would be no way to tell them apart. For this reason, we make sure to store an `id` field along with the `first_name`, `last_name` and `house` fields.

2. To use this class in our app, update the `helpers` import statement into your `app.py` file:

```{.python .numberLines startFrom="1"}
from helpers import find_house, user
```

3. We also need to define our global variables that we will use to store our data. Add the following underneath your global `app` variable in your `app.py` file:

```{.python .numberLines startFrom="1"}
users: list[user] = []
user_number: int = 0
```

> We will use the `users` global variable to keep a list of all users who have taken the quiz so far. We will use the `user_number` to keep track of how many users we have so far and what the next user `id` should be. (Note: we could just use the length of the list, but for clarity purposes will use an extra variable here)

4. Let's incorporate the storing of data into our `quiz` function. Update the `quiz` functionality to the following code snippet:

```{.python .numberLines startFrom="1"}
@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        global users
        global user_number

        fname: str = request.form['fname']
        lname: str = request.form['lname']
        animal: str = request.form['animal']

        if fname == '' or lname == '':
            return render_template("quiz.html")

        house: str = find_house(animal)
        new_user: user = user(user_number, fname, lname, house)
        users.append(new_user)

        user_number += 1

        return render_template("result.html", house=house)
    return render_template("quiz.html")
```

> - First, we label our `users` and `user_number` variables as global variables we plan to update.

- After finding the users house, we can create a new `user` object using the `user_number` as the `id` field and append it into our global `users` list.
- Finally we want to increment the `user_number` variable so that the next user will have a new `id`.

### Task: Displaying All Results

With all of the data from each submission to our quiz being stored, we can render a page that shows every users results!

1. First lets add a new template we can use for displaying all results. Create a new file in the `templates` directory and name it `all-results.html`.
2. Add the following HTML to the file and save it.

```{ .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Take the Quiz!</title>
    </head>
    <body>
        <h2>Welcome to results!</h2>
        {% for user in users %}
        <p>{{user.first_name}} {{user.last_name}} is in {{user.house}}</p>
        {% endfor %}
    </body>
</html>
```

> You may notice some more odd looking syntax inside of the `<body></body>` tags in this snippet. This file expects a list of `user` objects in a variable `users`. It then uses a python `for` loop to iterate through each user in the list and add a `<p></p>` tag for each users data. For instance, if the first person who filled out the quiz was named `Harry Potter` and selected `lion` as their favorite animal, the first `<p></p>` tag added would look like `<p>Harry Potter is in Gryffindor</p>`.

3. Finally, we need to add a new route where we can display our template and pass it our `users` list. Add the following function snippet in your `app.py` file.

```{.python .numberLines startFrom="1"}
@app.route('/all-results')
def all_results():
    return render_template('all-results.html', users=users)
```

> Here we are simply rendering our `all-results.html` template and passing it our users list as an argument.

4. Take the quiz a few times and make sure to submit. Then try navigating to `/all-results` in your browser. You should see the data from every quiz submission!

### Task: Individual Results

Flask also allows us to use variables in our routes. We can make use of this feature in order to return to individual users and display their data. This particular functionality is useful for things like displaying a user page in web apps that have logins!

1. Lets define one more file in our `templates` directory for displaying all information about a particular user. Create a new file in `templates` named `user.html`.
2. Paste the following HTML into the file:

```{ .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Take the Quiz!</title>
    </head>
    <body>
        <p>Hello {{user.first_name}} {{user.last_name}}</p>
        <p>You are in {{user.house}} !!!</p>
    </body>
</html>
```

> This template expects a variable called `user` of the class type `user` that we defined earlier. It then renders the important information stored in the user object.

3. Now we need to add a route for rendering this `user.html` template. Add the following code snippet in your `app.py` file:

```{.python .numberLines startFrom="1"}
@app.route('/user<usernumber>')
def display_user(usernumber: str):
    return render_template('user.html', user=users[int(usernumber)])
```

> This route is slightly more complex than ones we have defined previously. The syntax `<usernumber>` defines an unknown in the URL with a variable name of `usernumber`. When this route is accessed, it will pass the given `usernumber` to the `display_user` function. Then the `usernumber` can be converted to an `int` and used to select the correct user our of our `users` list. For instance, if we navigate to the URL `/user2`, we could expect to be shown all the data about the third person who took the quiz. (Since we started at user0)

4. Take the quiz at least once and then try navigating to the URL `/user0` in your browser. You should see only the data for this user! Try taking the quiz again and then navigate to `/user1`


## Bonus: Hot Reload

As you develop a new project, it can get tedious to have to refresh your browser every time you make a small style change to see the update. Instead we can make the browser auto-refresh every time you save a file. This behavior is commonly called live refresh or hot reload.

1. Open a new terminal and run `pip install livereload`
2. Create a new file in your repo named `dev.py`
3. Paste in the following code snippet and save.

```{.python .numberLines startFrom="1"}
from app import app
from livereload import Server

if __name__ == '__main__':
   server = Server(app.wsgi_app)
   server.serve()
```

4. Whenever you would like to run your app with livereload run `python -m dev` in your terminal and open your browser to `http://127.0.0.1:5500/`

## Documentation, Tools and Resources

#### [Finished Tutorial Code](https://github.com/ezriwhite/finished-web-tutorial)

This code should be identical to yours after completing the tutorial.

#### [Styled Starter Code](https://github.com/ezriwhite/flask_experiment_hack110)

This code is the same as the tutorial with some more exciting styling and navigation bar already built. Feel free to use this to kickstart your project!

#### [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/quickstart/#what-to-do-if-the-server-does-not-start)

Check this documentation for any questions related to flask.

#### [W3Schools Introduction to HTML](https://www.w3schools.com/html/html_intro.asp)

This is a great site for learning more about basic HTML.

#### [W3Schools Introduction to CSS](https://www.w3schools.com/html/html_css.asp)

This is a great site for learning more about basic CSS.

### Helpful VSCode Extensions

To add these extensions, click the Extensions tab on the sidebar in vscode. (Looks like three squares with a fourth square drifting away) Then you can search for and install the extensions you would like.

- `Auto Close Tag`: automatically adds closing tags to your HTML code.
- `Auto Rename Tag`: when you rename an opening HTML tag, automatically changes the closing tag to match.
- `Paste and Indent`: automatically adds the appropriate indents to code pasted into your project.
- `Color Highlight`: displays swatches of and highlights CSS colors in your code for easy identification.
- `Beautify`: automatically formats HTML and CSS code.
  - To get this to work, click Settings (the cog in the bottom left corner)
  - Click the { } curly braces in the top right corner
  - Copy and paste this in the curly braces: "editor.formatOnSave": true
- `Better Jinja`: syntax highlighting for jinja
