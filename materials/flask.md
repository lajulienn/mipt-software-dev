# Setting Up Flask
## Prerequisites
- Python 3.7 or higher installed on your machine.
- Basic knowledge of Python.

## Installation
First create a virtual environment for the new project (in IDE this is done automatically).

Flask can be installed using pip:

```bash
pip install Flask
```
Verify installation with:

```bash
python -m flask --version
```

# Your First Flask Application
```python
from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# Define a route and its corresponding request handler
@app.route("/")
def home():
    return "Hello, Flask!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
```

Explanation:
- `app = Flask(__name__)` creates your web app.
- `@app.route("/")` sets the URL endpoint (root path).
- The function below returns a response to that URL.
- `app.run(debug=True)` starts the server in debug mode (auto reloads and shows errors).

# Flask Routing
Routing connects URLs to Python functions.

```python
@app.route("/about")
def about():
    return "About Page"
```

Dynamic routes with variables:

```python
@app.route("/user/<username>")
def show_user(username):
    return f"User: {username}"
```
- `<username>` is a placeholder capturing URL parts.

# Request Methods
Flask supports different HTTP methods (GET, POST, etc.)

Example of handling POST and GET:

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"Logged in as {username}"
    return '''
      <form method="post">
        Username: <input name="username"><br>
        Password: <input name="password" type="password"><br>
        <input type="submit">
      </form>
    '''
```

# Templates (Jinja2)
Flask uses Jinja2 for templates, which allows you to separate Python logic from HTML.

Create a folder called `templates/` and inside it an index.html:

```html
<!doctype html>
<html>
<head><title>{{ title }}</title></head>
<body>
  <h1>Welcome, {{ user }}!</h1>
</body>
</html>
```

Then in your Flask app:

```python
from flask import render_template

@app.route("/welcome/<user>")
def welcome(user):
    return render_template("index.html", title="Home Page", user=user)
```

- `{{ ... }}` are placeholders replaced by Python variables.

# Static Files
Static files like CSS, JS, and images go into a folder named `static/`.

Example: `static/style.css`

Reference in a template:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```
# Flask Extensions
Flask's minimal core can be extended with official and third-party packages, e.g.:

- Flask-SQLAlchemy (database ORM)
- Flask-WTF (form validation)
- Flask-Login (user authentication)
- Flask-Migrate (database migrations)

Example of initializing an extension:

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
```

# Application Structure (Best Practice for Larger Apps)
```
/project
    /app
        __init__.py      # app creation and configuration
        routes.py        # route definitions
        models.py        # data models
        templates/       # html templates
        static/          # css/js/images
    config.py            # configuration file
    run.py               # server starter
```

`__init__.py` example:

```python
from flask import Flask

app = Flask(__name__)

from app import routes

```
# Debugging and Testing
- Use `app.run(debug=True)` for development mode.
- Use logging for error tracking.
- Use Flask's test client to write unit tests.

# Exercise
Build a simple Flask blog application with the following requirements:

- The homepage (`/`) lists titles of blog posts stored in-memory (a Python list).
- Clicking on a blog title leads to a detailed post page `/post/<id>` displaying the post content.
- Add a route to add new blog posts via a simple HTML form (`/new`). The form should accept a title and content.
- Use templates to render pages.
- Add basic CSS styling using static files.