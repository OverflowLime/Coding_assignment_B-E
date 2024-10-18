from flask import Flask, jsonify, request
from rest_api.jsonPlaceHolder import JsonPlaceholderClient
from typing import Any


app = Flask(__name__)
client = JsonPlaceholderClient()


@app.route('/posts', methods=['GET'])
def get_posts() -> Any:
    """List all posts"""
    posts = client.fetch_posts()
    return jsonify(posts)


@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id: int) -> Any:
    """List a single post by id"""
    post = client.fetch_post_by_id(post_id)
    return jsonify(post)


@app.route('/posts', methods=['POST'])
def create_post() -> Any:
    """Create a new post"""
    post_data = request.json
    if not isinstance(post_data, dict):
        return jsonify({"error": "Invalid input"}), 400
    created_post = client.create_post(post_data)
    return jsonify(created_post), 201


@app.route('/users', methods=['GET'])
def get_users() -> Any:
    """Get all users"""
    users = client.fetch_users()
    return jsonify(users)


@app.route('/comments', methods=['GET'])
def get_coments() -> Any:
    """Get all comments"""
    users = client.fetch_comments()
    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
