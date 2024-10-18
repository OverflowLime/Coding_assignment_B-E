import pytest
from flask.testing import FlaskClient
from rest_api.app import app
from rest_api.jsonPlaceHolder import JsonPlaceholderClient
import requests_mock


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def base_url():
    return JsonPlaceholderClient.BASE_URL


def test_get_posts(client: FlaskClient, base_url: str):
    with requests_mock.Mocker() as m:
        m.get(f'{base_url}/posts', json=[{'id': 1, 'title': 'Test Post'}])
        response = client.get('/posts')
        assert response.status_code == 200
        assert response.json == [{'id': 1, 'title': 'Test Post'}]


def test_get_post_by_id(client: FlaskClient, base_url: str):
    with requests_mock.Mocker() as m:
        m.get(f'{base_url}/posts/1', json={'id': 1, 'title': 'Test Post'})
        response = client.get('/posts/1')
        assert response.status_code == 200
        assert response.json == {'id': 1, 'title': 'Test Post'}


def test_create_post(client: FlaskClient, base_url: str):
    with requests_mock.Mocker() as m:
        m.post(f'{base_url}/posts', json={'id': 101, 'title': 'New Post'})
        response = client.post('/posts', json={'title': 'New Post', 'body': 'Test body', 'userId': 1})
        assert response.status_code == 201
        assert response.json == {'id': 101, 'title': 'New Post'}


def test_get_users(client: FlaskClient, base_url: str):
    with requests_mock.Mocker() as m:
        m.get(f'{base_url}/users', json=[{'id': 1, 'name': 'Test User'}])
        response = client.get('/users')
        assert response.status_code == 200
        assert response.json == [{'id': 1, 'name': 'Test User'}]


def test_get_comments(client: FlaskClient, base_url: str):
    with requests_mock.Mocker() as m:
        m.get(f'{base_url}/comments', json=[{'id': 1, 'name': 'Test Comment'}])
        response = client.get('/comments')
        assert response.status_code == 200
        assert response.json == [{'id': 1, 'name': 'Test Comment'}]
