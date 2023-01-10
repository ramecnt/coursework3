import pytest
from main import app
import utils


class TestAPI:
    def test_api_type_all(self):
        response = app.test_client().get('/api/posts')
        assert response.data[0] == ord("[")

    def test_api_type_concrete(self):
        response = app.test_client().get('/api/posts/1')
        assert response.data[0] == ord("{")

    def test_api_content_all(self):
        response = app.test_client().get('/api/posts')
        for i in range(len(response.json)):
            assert response.json[i].get("poster_name") == utils.get_posts_all()[i]["poster_name"]
            assert response.json[i].get("poster_avatar") == utils.get_posts_all()[i]["poster_avatar"]
            assert response.json[i].get("pic") == utils.get_posts_all()[i]["pic"]
            assert response.json[i].get("content") == utils.get_posts_all()[i]["content"]
            assert response.json[i].get("views_count") == utils.get_posts_all()[i]["views_count"]
            assert response.json[i].get("likes_count") == utils.get_posts_all()[i]["likes_count"]
            assert response.json[i].get("pk") == utils.get_posts_all()[i]["pk"]

    def test_api_content_concrete(self):
        response = app.test_client().get('/api/posts/1')
        assert response.json.get("poster_name") == "leo"
        assert response.json.get("poster_avatar") == "https://randus.org/avatars/w/c1819dbdffffff18.png"
        assert response.json.get(
            "pic") == "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80"
        assert response.json.get(
            "content") == "Ага, опять еда! Квадратная тарелка в квадратном кадре. А на тарелке, наверное, пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно."
        assert response.json.get("views_count") == 376
        assert response.json.get("likes_count") == 154
        assert response.json.get("pk") == 1
