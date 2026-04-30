---
title: To-do List Web App
author:
  - Ezri White
page: explore
template: overview
---

## Getting started

> In this tutorial you will create a todo list web application! We will learn some basic HTML, CSS and Flask and your website will be able to save data to render on different pages while it is running. Flask is a python library used for web development and is actually what we use while developing this course's website!

We will begin this tutorial from scratch! Start setting up the following to prepare:

1. On github.com, click the green New Repository button and name the repository `todo-list-tutorial`.
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

```{.html .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Intro to Web Dev!</title>
    </head>
    <body>
        <p>Hello World!</p>
        <p class='hello' >Hello World!</p>
        <p class='hello' >Hello World!</p>
        <p class='hello' id='world' >Hello World!</p>
    </body>
</html>
```

3. Make sure the file is saved and then right click the file in the file explorer and click reveal in finder (Mac) or show in folder (Windows).
4. In finder / file explorer, right click on the file and open it with google chrome. You should now see a basic webpage that says Hello World!

### HTML Tags

So what exactly did we add to the `index.html` file? HTML is made up of elements wrapped with `tags` that help label pieces of content. For instance, The `<p></p>` tag that surrounds `Hello World!` indicates that we are adding a `paragraph` element to our webpage.

There are many types of html `tags` that allow us to specify what type of content we are adding to a page: headings, paragraphs, bulleted lists, etc. Some`tags` can hold other `tags` inside of them which allows us to work towards creating complex webpages.

### Task: styles.css

1. Make a new file in your repository named `styles.css`. This file name is a convention for the CSS file that holds the core styling.
2. Copy and paste the following CSS snippet into the file:

```{.css .numberLines startFrom="1"}
p {
    color: #75c3f7;
  }
```

3. Make sure the file is saved and then add the following `link` tag inside the `<head></head>` tag in your `index.html` file. This will link your CSS file to your HTML file so that the styles we add are applied to our webpage.

```{.html.numberLines startFrom="1"}
<link rel='stylesheet' href='styles.css' />
```

4. Once both files are saved, reload the chrome page with your webpage and you should see the color of all the `Hello World!` texts change! Now add the following CSS snippet: 

```{.css .numberLines startFrom="1"}
.hello {
    color: #befe9f;
  }
```

When you refresh the page again you should see the bottom three `Hello World!`'s have changed to green. In `index.html` you may notice the last three `Hello World!`'s are labeled with `class='hello'`. Sometimes we may not want to apply a style to every single element of the `<p>` tag type (or other types). Instead we can label groups of elements with a class and then select the class in our css file to style it. We did this with the `hello` class when we changed the bottom `Hello World!`'s to green.

5. One other option for styling specific elements is id's. Add the following CSS snippet: 

```{.css .numberLines startFrom="1"}
#world {
    color: #cfa3df;
  }
```

When you refresh the page again you should see the last `Hello World!` has changed to purple. In `index.html` you may notice the last `Hello World!` is labeled with `id='world'`. If you want to apply a style to a singular element then you should use an Id. Id's SHOULD NEVER be added to more than one element, they are intended to be unique identifiers. Id's can be useful for styling because they are even more specific than classes. Notice that the last `Hello World` element is also labeled with `class='hello'` but the styling for the id overrode it.

> Note: pay attention to the syntax for selecting different css rules to style. If you are styling all elements of a `tag` type, you simply write the tag name and then the rules. If you are styling a class, you preface it's name with a `.` and if you are styling an `id` you preface it's name with a `#`.


## Basic Flask

### Task: Setting up Flask

1. Create a new directory in your repo named `templates` and move your `index.html` file inside of it.
2. Create a new directory in your repo named `static` and move your `styles.css` file inside of it.
3. You'll need to install the Flask library before getting started. In a new terminal, paste and run the following command:

```
python -m pip install Flask
```

4. Once that finishes, create a new file called `app.py` in your repo and add the following code snippet.

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

### Task: Adding a new page

1. Create a new file called `create-todo.html` in your `templates` folder and paste the following HTML into it.

```{.html .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Create Todo!</title>
    </head>
    <body>
        <form method="post">
            <label for="title">Todo title:</label>
            <br />
            <input type="text" id="title" name="title">
            <br />
            <br />
            <label for="description">Todo description:</label>
            <br />
            <input type="text" id="description" name="description">
            <br />
            <br />
            <input type="submit" value="Create">
        </form>
    </body>
</html>
```

2. Return to your `index.html` file and add the following HTML element in the body.

```{.html .numberLines startFrom="1"}
<a href="/create-todo">Create Todo!</a>
```

3. If you attempt to click on `Create Todo!` while viewing your `index.html` file on chrome, you will get an error! This is because we need to define the route to the `create-todo` URL in our `app.py` file. Add the following code snippet in `app.py`, save all the files, and attempt to click `Create Todo!` again.

```{.python .numberLines startFrom="1"}
@app.route('/create-todo')
def create_todo():
    return render_template("create-todo.html")
```

## Handling Methods

In order to add interactivity to the create todo page on our site we need to learn about HTTP request methods. We won't need to know a lot about HTTP, but a simple definition for HTTP is a defined set of rules or protocols for fetching resources such as our HTML or CSS files.

Two of these rules are the `GET` and `POST` methods. The `GET` method is a basic protocol for viewing or _getting_ some resource such as our `index.html` file. The `POST` method is a protocol for updating or inserting new data. You can imagine when you _post_ something on social media the data is getting uploaded so that everyone can now see your post.

### Task: Form Submission

When we click the submit button that we defined in our `create-todo.html` file, we want to show the user that they succesfully created a new todo item. The easiest way to do this is by setting up a new HTML `template` that we will render instead of `create-todo.html` when the user submits the form. For now we will hardcode the success view, but later we will actually show the new todo.

1. Create a new file in your templates folder named `success.html` that will be used to confirm the creation of the todo. Add the following HTML to this file:

```{.html .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
     <p>Successfully created todo!!!</p>
</html>
```

2. Notice how the HTML for the form in `create-todo.html` says `method="post"`. When you click the submit button inside the form element it will use the HTTP protocol `POST`. This makes sense since we are going to be saving or _posting_ new data for the users answers when they click the submit button. We can use this fact to render our sucsess template in our `create_todo` function. First, we will need to import the `request` ability from Flask. Update the Flask import at the top of your `app.py` file:

```{.python .numberLines startFrom="1"}
from flask import Flask, render_template, request
```

3. Now we are ready to handle different types of requests. Update your `create_todo` function in `app.py` as seen below:

```{.python .numberLines startFrom="1"}
@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        return render_template("success.html")
    return render_template("create-todo.html")
```

3. Now, when you click the Submit button when viewing your `/create-todo` page, our function will check if the request method was `POST` and render a success if so. Otherwise, we will see our normal create todo page. Keep in mind that the route or URL in your browser still shows `/create-todo` since all we changed is what is rendered in our `create_todo` function.

### Task: Returning to Create Page

We also want users to be able to create more todos so we will add a button that lets us return to the create view.

1. Add the following HTML snippet into your `success.html` template underneath `<p>Successfully created todo!!!</p>`:

```{.html .numberLines startFrom="1"}
    <form method="get">
        <input type="submit" value="Create another!">
    </form>
```

2. In this `form` we specified that `method="get"`. This makes sense since we are just requesting the `create-todo.html` view instead of updating or posting any data. We could now update our `create_todo` method to the code snippet below, but it is actually logically equivalent to what we have already written since any method that is not `POST` will render our `create_todo.html` file as a default so there is no need.

```{.python .numberLines startFrom="1"}
@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        return render_template("success.html")
    if request.method == "GET":
        return render_template("create-todo.html")
    return render_template("create-todo.html")
```

3. If you try clicking the `Create another!` button you should now see the create view. It should be easy to navigate between these two views now.

## Working With Data

When a user submits their new todo we want to be able to store and display their result! Let's learn how to check what a user inputted into the form.

### Task: Obtaining the data

Now we will grab the submitted data from the form and then display it on the success page.

1. In order to show the success page we will need to add a variable into our `success.html` file. Add the following below `<p>Successfully created todo!!!</p>`:

```{.html .numberLines startFrom="1"}
<p> Title: {{title}}</p>
<p> Description: {{description}}</p>
```

> The `{{title}}` syntax is similar to what you have already worked with while using `f-strings`. In our case we are telling our `success.html` template to expect two `str` variables named `title` and `description`.

2. Now we need to make sure to pass the `title` and `description` variables to the `render_template` function. Update the `create_todo` function to the following:

```{.python .numberLines startFrom="1"}
@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":

        title: str = request.form['title']
        description: str = request.form['description']

        if title == '':
            return render_template("create-todo.html")

        return render_template("success.html", title=title, description=description)
    return render_template("create-todo.html")
```

> - In this code snippet we first grab the data for the `title` and `description` and store them into variables.

- Then we make sure that the user filled out at least the title. If they didn't, we go back to the `create-todo.html` view.
- Finally we pass our `title` and `description` variables to the `render_template` function.

3. Navigate to your `/create-todo` page and make a todo. When you press create your webpage should display a success page that shows the details of the todo you just created!

### Task: Storing the Data

We also want to be able to keep track of all succesfully created todos and therefore need to be able to store our data instead of just displaying it once. In modern web development, the handling, storing and fetching of data is what is usually called `backend` development. In our program we will do a simple version of this by storing our data in global variables that our `app` file can access.

1. We want to use best practices while accomplishing this so we will now define a class for a `todo` to keep our code organized and readable. We could write this class in our `app.py` file but for organization we will add a helper file for classes and functions. Create a new file named `helpers.py` and add the following class:

```{.python .numberLines startFrom="1"}
class todo:
    id: int
    title: str
    description: str

    def __init__(self, id: int, title: str, description: str):
        self.id = id
        self.title = title
        self.description = description
```

> We need todos to be uniquely identifiable. For instance, what if we had two todos titled _Do Laundry_ with no descriptin or matching descriptions? There would be no way to tell them apart. For this reason, we make sure to store an `id` field along with the `title` and `description` fields.

2. To use this class in our app, add the following import statement into your `app.py` file:

```{.python .numberLines startFrom="1"}
from helpers import todo
```

3. We also need to define our global variables that we will use to store our data. Add the following variables underneath your global `app` variable in your `app.py` file:

```{.python .numberLines startFrom="1"}
todo_list: list[todo] = []
todo_count: int = 0
```

> We will use the `todo_list` global variable to keep a list of all created todos. We will use the `todo_count` to keep track of how many todos we have so far and what the next `id` number should be.

4. Let's incorporate the storing of data into our `create_todo` function. Update the `create_todo` functionality to the following code snippet:

```{.python .numberLines startFrom="1"}
@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count

        title: str = request.form['title']
        description: str = request.form['description']

        if title == '':
            return render_template("create-todo.html")

        new_todo: todo = todo(todo_count, title, description)
        todo_list.append(new_todo)

        todo_count += 1

        return render_template("success.html", title=title, description=description)
    return render_template("create-todo.html")
```


> - First, we label our `todo_list` and `todo_count` as global variables since we plan to update them.
- Then we create a new `todo` object and append it to our global `todo_list` list.
- Finally we want to increment the `todo_count` variable so that the next todo will have a new `id`.

### Task: Displaying All Todos

With all of the data from each created todo being stored, we can render a page that shows the whole todo list!

1. First lets add a new template we can use for displaying all results. Create a new file in the `templates` directory and name it `view-list.html`.
2. Add the following HTML to the file and save it.

```{.html .numberLines startFrom="1"}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>View List!</title>
    </head>
    <body>
        <h2>Todo List</h2>
        {% for todo in todo_list %}
            <br/>
            <h4>{{todo.title}}</h4>
            <p>{{todo.description}}</p>
        {% endfor %}
    </body>
</html>
```

> You may notice some more odd looking syntax inside of the `<body></body>` tags in this snippet. This file expects a list of `todo` objects in a variable `todo_list`. It then uses a python `for` loop to iterate through each user in the list and add some html tags for each todo's data. For instance, if the first todo created was titled `Watch Game` and the description was `8:00pm`, this html would be generated for it: `<br/><h4>Watch Game</h4><p>8:00pm</p>`.

3. Finally, we need to add a new route where we can display our template and pass it our `todo_list`. Add the following function snippet in your `app.py` file.

```{.python .numberLines startFrom="1"}
@app.route('/view-todo-list')
def view_todo_list():
    return render_template('view-list.html', todo_list=todo_list)
```

> Here we are simply rendering our `view-list.html` template and passing it our `todo_list` as an argument.

4. Try creating a few todo items on the create-todo page. Then try navigating to `/view-todo-list` in your browser. You should see the data from every todo submission!


## Bonus: Menu and Styling

In this bonus task you will add a navigation menu to your site and improve the general looks of your web app! Finishing this bonus step will give you a great starting point to customize for your own project.

1. In your `static` folder create a new file named `bootstrap.min.css`. Then visit [this link](https://github.com/ezriwhite/hack110-todo-demo/blob/main/static/bootstrap.min.css) and click the button that looks like two overlapping rounded squares and says _Copy raw contents_. This will copy the entire contents of the file to your clipboard. Then return to the file you just made and use your computers paste shortcut to add what you copied into the file. Save the file. 

> Bootstrap is a _front-end framework_ which essentially means pre written CSS rules that you can use instead of writing your own. In step one you are adding a copy of these rules into our static folder so we can use them!

2. Right click on your `static` folder and click _Reveal in Finder_ or _Reveal in File Explorer_ to determine where the folder is located on your computer. Now visit [this link](https://github.com/ezriwhite/hack110-todo-demo/blob/main/static/logo.png) and press the _Download_ button above the Comp 110 logo png. Find where on your computer the download has saved and then move or drag the png image into your static folder. Confirm the name of this file is exactly `logo.png`. Alternatively, you may download any png image you wish at this step, move it into the static folder, and rename it to `logo.png`.

3. We will also add some of our own css rules from the course website to the `styles.css` file. Copy and paste the following into your `styles.css` file:

```{.css .numberLines startFrom="1"}
@import url("https://fonts.googleapis.com/css?family=Quicksand&display=swap");

/** ---------------------- GENERAL ---------------------- **/

html {
  min-height: 100%;
}

body {
  background: linear-gradient(to bottom right, #e6e3e3, #e0e0e0);
  color: #555555;
  font-size: 1em;
  font-family: "Quicksand";
  background-attachment: fixed;
}

.container {
  margin-top: 1rem;
}

/** ---------------------- NAVBAR ---------------------- **/

.navbar {
  z-index: 1;
  background: #f5f5f5;
  border-image: linear-gradient(
    to right,
    #fe9f9f,
    #fec79f,
    #fadf94,
    #befe9f,
    #9ffec5,
    #9fedfe,
    #cfa3df,
    #fe9fe9
  );
  border-left: 0px;
  border-right: 0px;
  border-top: 0px;
  border-bottom: 5px solid;
  border-image-slice: 1;
  width: 100%;
  height: 6.2em;
}

.navbar-expand {
  -webkit-box-orient: horizontal;
  -webkit-box-direction: normal;
  flex-flow: row nowrap;
  -webkit-box-pack: start;
  justify-content: flex-start;
}

.nav-item {
  margin-left: 2em;
  vertical-align: bottom;
}

.nav-link {
  font-family: "Quicksand";
  font-size: 2.25vw;
  font-weight: bold;
  color: #727272;
  text-shadow: 0px 0px 0px #e6e6e6;
  letter-spacing: 0.15em;
  margin-top: 0.5em;
}

.nav-link:hover {
  color: #aaaaaa;
}

img.logo {
  max-height: 7vw;
}
```

4. To ensure that all the new CSS we have added is displayed, make sure the following two lines are inside the `<head></head>` tag on every single html template in the `templates` folder:

```{.html .numberLines startFrom="1"}
<link rel='stylesheet' href='/static/bootstrap.min.css'>
<link rel='stylesheet' href='/static/styles.css'>
```

5. Finally we will add our navbar menu! Copy and paste the following html snippet inside the `<body></body>` tag but above any other html you have written inside the body:

```{.html .numberLines startFrom="1"}
<!-- navigation bar -->
    <nav class="navbar navbar-expand">
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <a href="/"><img class="logo" src="/static/logo.png" alt="logo"></a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/">home</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/create-todo">create</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/view-todo-list">view</a>
                </li>
            </ul>
        </div>
    </nav>
```

> In order to be able to use this menu bar from every page of our webapp, we must make sure to add it to every template file!

Refresh your web app and try navigating around your site using the new menu.

## Bonus: Add Categories

In this bonus task you will add the ability to categorize your todos by color in the list display.

1. First we need to add the ability to select a color category during the creation of a todo. In the `create-todo.html` file, add the following html snippet right above the `Create` button html:

```{.html .numberLines startFrom="1"}
            <label for="color">Color:</label>
            <select id="color" name="color">
                <option value="grey">Grey</option>
                <option value="red">Red</option>
                <option value="orange">Orange</option>
                <option value="yellow">Yellow</option>
                <option value="green">Green</option>
                <option value="blue">Blue</option>
                <option value="purple">Purple</option>
                <option value="pink">Pink</option>
            </select>
            <br />
            <br />
```
When you create a todo make sure this dropdown menu is showing up. If you would like to define names for the categories besides the colors, you can replace the capitalized color names with categories such as `School`, `Work`, `Sport`, etc. Just be sure not to change the lowercase `value="red"` part of each option as it is needed for the functionality you are adding to work.

2. Now we need to update our "Backend" to handle this new piece of data. First we will update our todo class in the `helpers.py` file to incorporate a color:

```{.python .numberLines startFrom="1"}
class todo:
    id: int
    title: str
    description: str
    color: str

    def __init__(self, id: int, title: str, description: str, color: str):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
```
We also need to update our `create_todo` route function to read and store the color data. Update this function in the `app.py` file to the following:

```{.python .numberLines startFrom="1"}
@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count
        
        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']

        if title == '':
            return render_template("create-todo.html")

        new_todo: todo = todo(todo_count, title, description, color)
        todo_list.append(new_todo)

        todo_count += 1

        return render_template("success.html", , title=title, description=description)
    return render_template("create-todo.html")
```
We are now reading and storing the data for the color category we added in the create todo form and are ready to change our view list display to reflect this!

3. We will start updating the display of the view list by adding some new css rules. In your `styles.css` file add the following css:

```{.css .numberLines startFrom="1"}
.todo {
  padding: 10px;
  border-radius: 10px;
  margin-bottom: 5px;
  border-width: 2px;
  border-style: solid;
}

.grey-border { border-color: #cac9c9;}
.red-border { border-color: #fe9f9f;}
.orange-border { border-color: #fec79f;}
.yellow-border { border-color: #fadf94;}
.green-border {border-color: #befe9f;}
.blue-border {border-color: #9fedfe;}
.purple-border {border-color: #cfa3df;}
.pink-border {border-color: #fe9fe9;}
```
Here we are adding some general styling for every todo under the css class `todo`. We also set up 8 different css classes to help us assign different borders to different todos.

4. Finally we need to update our template to use the generic todo styling and a specific border styling based on the color/category property of each todo. Update the for loop in `view-list.html` to the following:

```{.html .numberLines startFrom="1"}
        {% for todo in todo_list %}
            <div class="todo {{todo.color}}-border">
                <h4>{{todo.title}}</h4>
                <p>{{todo.description}}</p>
            </div>
        {% endfor %}
```

Here we are surrounding each title and description with a `div` element that we can turn into a container with a border using our css `todo` class. We also add the `{{todo.color}}-border` class to the `div` element. For a specific todo that had the color property of `purple`, this snippet would evaluate to `purple-border` and therefore apply the `purple-border` css class styling we added to `styles.css` in step 3.

Make sure all files are saved then attempt to create a few todos with different categories. When you go to view them they should display with different color borders!

## Bonus: Checking off Items

One hallmark of any great todo list is the ability to mark items as complete or incomplete. In this extension, you will modify individual todo list items to contain a button which will check them off, and use some additional styling to visually distinguish complete items from incomplete ones.

1. First, we'll add some new styling for a todo item that is checked off:

```
.checked {
  background-color: lime;
  opacity: 0.2;
}
```

When the checked class is attached to a todo item, it will have a lime background and appear blurred out due to the decreased opacity (default opacity is 1, 0 is fully invisible).

But how do we distinguish a checked todo item from an unchecked one? Our `todo` class currently contains no data for determining this! Let's add a `checked` property, of type `bool`, that will be `False` when an item is unchecked, and `True` when it is checked.

```{.python .numberLines startFrom="1"}
class todo:
    id: int
    title: str
    description: str
    color: str
    checked: bool

    def __init__(self, id: int, title: str, description: str, color: str):
        self.id = id
        self.title = title
        self.description = description
        self.color = color
        self.checked = False # Every new item begins as unchecked
```

2. Inside your `view-list.html` template, there is currently a for-in loop responsible for rendering each of the items. Replace the current for-in loop with the following code snippet

```{.numberLines startFrom="1"}
    {% for i in range(todo_list| length) %} {% set todo = todo_list[i] %}
      <div
        class="todo {{ 'checked' if todo.checked else ''}}"
      >
      <div>
        <form action="/view-todo-list" method="POST">
          <button
            type="submit"
            style="float: right"
            value="{{i}}"
            name="check-button"
            id="check-button"
          >
            {{'Uncheck' if todo.checked else 'Check'}}
          </button>
        </form>
        </div>
        <h4>{{todo.title}}</h4>
        <p>{{todo.description}}</p>
      </div>
      {% endfor %}
```

(You'll notice that some tags take up multiple lines now. This is purely for readability and is totally ok!)

Notice several changes to the html that renders each todo item:

- Each todo item now contains a button attached to a form. The form submits with the POST method like we've seen before, and we'll handle that submission shortly.
- We've changed the for-in loop to now go through each _index_ of the todo_list, rather than each item. This is important, as it will allow us to mark each button with the todo item it corresponds to!
  - We also `set` a `todo` variable to be equal to `todo_list[i]` so that the rest of the html looks the same.
- Each buttons 'value' property matches it to an index of the `todo_list`.
- Every button has the same `name` and `id`, `check-button`

> The most interesting part of these is the presence of new conditional statements, of this form:

```
{{ value1 if boolean_condition else value2 }}
```

These are called _ternary expressions_, and are present in many programming languages (including python!) The expression will evaluate to `value1` when `boolean_condition` is `True`, and `value2` when `boolean_condition` is `False`. For example, the Button's text content is

```
{{'Check' if not todo.checked else 'Uncheck'}}
```

meaning that the button will say Check when `todo.checked` is `False` (the item is not checked) and `Uncheck` when `todo.checked` is `True`. The same is true for the button's classes - the checked class will be applied when `todo.checked` is `True`, but not when it is `False`.

3. Now that we've laid the groundwork with html and css, we need to change our python code to handle when a user pushes one of the buttons. Change your `view_todo_list` method to the following:

```{.python .numberLines startFrom="1"}
@app.route('/view-todo-list', methods=["GET", "POST"])
def view_todo_list():
    if request.method == "POST" and len(todo_list) > 0:
        idx: int = int(request.form['check-button'])
        todo_list[idx].checked = not todo_list[idx].checked
    return render_template('view-list.html', todo_list=todo_list)
```

`view_todo_list` now supports those POST requests we'll be sending when a user presses a button. When a user presses a button, the `request.form['check-button']` will contain the _index_ of `todo_list` that they want to check/uncheck (see the button's value attribute!!). From there, we go into the `todo_list` and flip its `checked` property. If it was `True`, it will become `False`, and vice versa. Then, when the page reloads, the item will be seen as checked, and the styling will be applied!

(The check that `len(todo_list) > 0` is not required, but can prevent crashing when you refresh the page and potentially empty out your todo_list...)


## Bonus: Editing Tasks 

Note: The Checking Items Bonus must be complete to implement the Editing Tasks bonus.

In this bonus task you will add the ability to edit your tasks from the view list page. We will do this using a feature of flask that allows us to use variables in our routes. We can make use of this feature in order to show an edit page for an individual todo.

1. Lets define two more files in our `templates` directory for displaying an edit form page and successful edit page. Create a new file in `templates` named `edit-todo.html`. Copy and paste the contents of your `create-todo.html` file into the new edit file.

2. Create a new file in `templates` named `edit-success.html`. Copy and paste the contents of your `success.html` file into the new success file. Update the contents of this file to say something about a successful edit instead of a successful creation. You can also add the following html tag somewhere in your body for an easy way of returning to the view list page:

```{.html}
<a href="/view-todo-list">Return to list view</a>
```

3. Now we need to add a route for rendering these new templates. Add the following code snippet in your `app.py` file:

```{.python .numberLines startFrom="1"}
@app.route('/edit-todo<todo_number>', methods=["GET", "POST"])
def edit_todo(todo_number: str):
    if request.method == "POST":
        global todo_list

        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']

        if title == '':
            return render_template("edit-todo.html")

        todo_list[int(todo_number)].title = title
        todo_list[int(todo_number)].description = description
        todo_list[int(todo_number)].color = color

        return render_template("edit-success.html")
    return render_template('edit-todo.html', todo=todo_list[int(todo_number)])
```

> This route is slightly more complex than ones we have defined previously. The syntax `<todo_number>` defines an unknown in the URL with a variable name of `todo_number`. When this route is accessed, it will pass the given `todo_number` to the `edit_todo` function. Then the `todo_number` can be converted to an `int` and used to select the correct todo our of our `todos` list. For instance, if we navigate to the URL `/edit-todo2`, we could expect to be shown all the data about the third todo that was created. (Since we started at 0)

4. Most of the logic in the `edit_todo` function matches the `create_todo` function. Notice however, that when we render the `edit-todo.html` template we pass it a todo. Let's update the copied HTML in `edit-todo.html` to show the values of the todo we are trying to edit.

```{.html .numberLines startFrom="1"}
        <input type="text" id="title" name="title">
        // updates to
        <input type="text" id="title" name="title" value="{{todo.title}}">

        <input type="text" id="description" name="description">
        // updates to
        <input type="text" id="description" name="description" value="{{todo.description}}">

        <input type="submit" value="Create">
        // updates to
        <input type="submit" value="Update">
```
Now if you create a todo, then visit the url `/edit-todo0`, you should see the original text displayed and be able to edit and save your changes with the Update button.

5. Finally we need to add an edit button to each todo on the view list page. Add the following html snippet for a button underneath the Check/ Uncheck button (but within the div tag that surrounds it).

```{.html .numberLines startFrom="1"}
<form action="/edit-todo{{i}}" method="GET">
    <button type="submit" style="float: right" value="{{i}}" name="edit-button" id="edit-button" todo-id="{{i}}">
        Edit
    </button>
</form>
``` 

> Here the specified route for the action adds the `i` counter/ todo id so that when you click this button it navigates to that specific todo based on it's id number.

Try creating a few todos and then clicking edit from the view list page to get to your edit page!

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

<!-- #### [Finished Tutorial Code](https://github.com/ezriwhite/todo-list-tutorial)

This code should be identical to yours after completing the tutorial. -->

#### [Styled Starter Code](https://github.com/ezriwhite/hack110-todo-demo)

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
