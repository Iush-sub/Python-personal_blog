
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

@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    posts = load_posts()

    for post in posts:
        if post["id"] == post_id:
            return render_template("post.html", post=post)

    return "Post not found"


def load_posts():
    with open("posts.json", "r") as file:
        return json.load(file)


@app.route("/admin")
def admin ():
    return render_template("admin.html")

@app.route("/admin/create", methods=["POST"])
def create_post():
    title = request.form["title"]
    content = request.form["content"]

    posts = load_posts()

    new_post = {
        "id": len(posts) + 1,
        "title": title,
        "content": content
    }

    posts.append(new_post)

    with open("posts.json", "w") as file:
        json.dump(posts, file, indent=4)

    return redirect("/blog")



@app.route("/admin/edit/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    posts = load_posts()

    post = None
    for p in posts:
        if p["id"] == post_id:
            post = p
            break

    if request.method == "POST":
        post["title"] = request.form["title"]
        post["content"] = request.form["content"]

        with open("posts.json", "w") as file:
            json.dump(posts, file, indent=4)

        return redirect("/blog")

    return render_template("edit.html", post=post)





if __name__ == "__main__":
    app.run(debug=True,port=8000)
