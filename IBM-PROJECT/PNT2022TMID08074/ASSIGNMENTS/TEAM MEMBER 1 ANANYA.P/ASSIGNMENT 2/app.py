from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route('/user/<username>')
def show_user_profile(username):
    return f"Hii {escape(username)}"

@app.route('/post/<int:post_id>')
def show_user_post(post_id):
    return f"Post: {escape(post_id)}"

@app.route('/register')
def sign_up():
    return render_template("register.html")

@app.route('/login')
def log_in():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
