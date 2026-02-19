from flask import Flask, request
from flask import render_template

# Create a Flask instance
app = Flask(__name__)

# Define a route and its corresponding request handler
@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "About Page"

@app.route("/user/<username>")
def show_user(username):
    return f"User: {username}"

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

@app.route("/welcome/<user>")
def welcome(user):
    return render_template("index.html", title="Home Page", user=user)

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
