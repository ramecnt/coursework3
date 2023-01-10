import utils
import json
import pytest


class Test_utils:
    def test_get_all(self):
        with open("./data/posts.json", "r", encoding="utf-8") as f:
            assert utils.get_posts_all() == json.load(f)

    def test_comments_all(self):
        with open("./data/comments.json", "r", encoding="utf-8") as f:
            assert utils.get_comments_all() == json.load(f)

    def test_get_post_by_user(self):
        assert utils.get_posts_by_user("hanna") == []
        with pytest.raises(ValueError):
            utils.get_posts_by_user(12)

    def test_get_comments_by_post_id(self):
        assert utils.get_comments_by_post_id(8) == []
        with pytest.raises(ValueError):
            utils.get_comments_by_post_id(12)

    def test_search_for_posts(self):
        with pytest.raises(TypeError):
            utils.search_for_posts(10)

    def test_get_post_by_pk(self):
       assert utils.get_posts_by_pk(10) == False