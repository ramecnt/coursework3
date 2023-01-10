import json

def get_posts_all():
    with open("data/posts.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_comments_all():
    with open("data/comments.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_posts_by_user(name):
    l = 0
    global posts
    global comments
    result = []
    for i in posts:
        if name == i["poster_name"]:
            result.append(i)
            l += 1
        elif name == comments[i["pk"]-1]["commenter_name"]:
            l += 1
    if l == 0:
        raise ValueError
    return result

def get_comments_by_post_id(id):
    global posts
    global comments
    result = []
    l = 0
    for i in comments:
        if id == i["post_id"]:
            result.append(i)
            l += 1
        elif id == posts[i["post_id"]]["pk"]:
            l += 1
    if l == 0:
        raise ValueError
    return result


def search_for_posts(query):
    global posts
    result = []
    for i in posts:
        if query in i["content"]: result.append(i)
    return result


def get_posts_by_pk(pk):
    global posts
    for i in posts:
        if int(pk) == i["pk"]: return i
    return False

posts = get_posts_all()
comments = get_comments_all()
