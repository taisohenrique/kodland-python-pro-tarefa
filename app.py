from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

#  Banco de dados simulado em memória (lista de postagens)
posts = [
    {
        "id": 1,
        "title": "Bem-vindo ao Blog do Flask!",
        "content": "Este é o primeiro post. Flask é um framework web Python leve e poderoso.",
        "author": "Tassio Henrique",
        "date": "2026-03-18"
    }
]

next_id = 2  # Controla a geração de ID


@app.route("/")
def index():
    """Home page — lists all posts."""
    return render_template("index.html", posts=posts)


@app.route("/post/<int:post_id>")
def view_post(post_id):
    """Post detail page."""
    post = next((p for p in posts if p["id"] == post_id), None)
    if post is None:
        return "Post not found", 404
    return render_template("post.html", post=post)


@app.route("/new", methods=["GET", "POST"])
def new_post():
    """Create a new post."""
    global next_id
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        content = request.form.get("content", "").strip()
        author = request.form.get("author", "Anonymous").strip()

        if title and content:
            post = {
                "id": next_id,
                "title": title,
                "content": content,
                "author": author or "Anonymous",
                "date": datetime.now().strftime("%Y-%m-%d")
            }
            posts.append(post)
            next_id += 1
            return redirect(url_for("index"))

    return render_template("new_post.html")


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete_post(post_id):
    """Delete a post by ID."""
    global posts
    posts = [p for p in posts if p["id"] != post_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
