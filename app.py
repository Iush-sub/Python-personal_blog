
import json
from flask import Flask, render_template,request,redirect






app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog")
def blog():
    posts = load_posts()
    return render_template("blog.html", posts=posts)




def post_list(post_id):
    posts = load_posts()

    for post in posts:
        if post["id"] == post_id:
            return post

    return None




def load_posts():
    with open("posts.json", "r") as file:
        return json.load(file)

if __name__ == "__main__":
    app.run(debug=True,port=8000)
