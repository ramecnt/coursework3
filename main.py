from flask import Flask, render_template, request, jsonify
from utils import *
import logging

app = Flask(__name__, template_folder="templates")
app.config['JSON_AS_ASCII'] = False
logging.basicConfig(level=logging.INFO, filename='logs/api.log', format='%(asctime)s [%(levelname)s] %(message)s')


@app.route("/")
def main_page():
    return render_template("index.html", posts=get_posts_all())


@app.route("/posts/<int:x>")
def post_page(x):
    comments = get_comments_by_post_id(x)
    post = get_posts_by_pk(x)
    return render_template("post.html", comments=comments, post=post)


@app.route("/search/")
def search_page():
    query = request.args.get('s')
    return render_template("search.html", posts=search_for_posts(query), )


@app.route("/users/<username>")
def user_posts(username):
    posts = get_posts_by_user(username)
    return render_template("user-feed.html", posts=posts, name=username)


@app.route("/api/posts")
def api_posts():
    logging.info("Зашел на api по всем пользователям")
    return jsonify(get_posts_all())


@app.route("/api/posts/<post_id>")
def api_post(post_id):
    logging.info(f"Зашел на api по {post_id} пользователю")
    return jsonify(get_posts_by_pk(post_id))


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Такой страницы не существует</h1>", 404


@app.errorhandler(500)
def error_on_server(e):
    return "<h1>Произошла ошибка на сервере</h1>", 500


if __name__ == "__main__":
    app.run()
