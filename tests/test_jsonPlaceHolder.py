import pytest
import requests_mock
from rest_api.jsonPlaceHolder import JsonPlaceholderClient


@pytest.fixture
def base_url():
    return JsonPlaceholderClient.BASE_URL


@pytest.fixture
def client(base_url):
    return JsonPlaceholderClient()


@pytest.mark.parametrize("endpoint, expected", [
    ("posts", [{"id": 1, "title": "Test Post"}]),
    ("users", [{"id": 1, "name": "Test User"}])
])
def test_fetch_data(client, base_url, endpoint, expected):
    with requests_mock.Mocker() as m:
        m.get(f"{base_url}/{endpoint}", json=expected)
        if endpoint == "posts":
            assert client.fetch_posts() == expected
        elif endpoint == "users":
            assert client.fetch_users() == expected


@pytest.mark.parametrize("endpoint, error", [
    ("posts", ValueError),
    ("users", ValueError),
])
def test_fetch_data_failure(client, base_url, endpoint, error):
    with requests_mock.Mocker() as m:
        m.get(f"{base_url}/{endpoint}")

        with pytest.raises(error):
            if endpoint == "posts":
                client.fetch_posts()
            elif endpoint == "users":
                client.fetch_users()


@pytest.mark.parametrize("post_data, expected", [
    ({"title": "foo", "body": "bar", "userId": 1},
     {"id": 101, "title": "foo", "body": "bar", "userId": 1})
])
def test_create_post(client, base_url, post_data, expected):
    with requests_mock.Mocker() as m:
        m.post(f"{base_url}/posts", json=expected)
        assert client.create_post(post_data) == expected


@pytest.mark.parametrize("post_id,expected", [
    (1, {"id": 1, "title": "Test Post"})
])
def test_fetch_post_by_id(client, base_url, post_id, expected):
    with requests_mock.Mocker() as m:
        m.get(f"{base_url}/posts/{post_id}", json=expected)
        assert client.fetch_post_by_id(post_id) == expected


@pytest.mark.parametrize("post_id,error", [
    (99999, ValueError)
])
def test_fetch_post_by_id_failure(client, base_url, post_id, error):
    with requests_mock.Mocker() as m:
        m.get(f"{base_url}/posts/{post_id}", text="Not Found", status_code=404)
        with pytest.raises(error):
            client.fetch_post_by_id(post_id)
