import requests
from typing import List, Dict, Any, Optional


class JsonPlaceholderClient:
    BASE_URL: str = "https://jsonplaceholder.typicode.com"

    def _make_request(self, endpoint: str, method: str = "GET",
                      data: Optional[Dict[str, Any]] = None) -> Any:
        url = f"{self.BASE_URL}/{endpoint}"
        response = requests.request(method, url, json=data)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise ValueError(f"Failed to fetch {endpoint}: {str(e)}") from e

        return response.json()

    def fetch_posts(self) -> List[Dict[str, Any]]:
        """
        Fetches all posts from the API.

        :return: A list of posts.
        :raises: ValueError if the response is not a list.
        """
        response = self._make_request("posts")
        if isinstance(response, list):
            return response
        raise ValueError("Expected a list of posts")

    def fetch_post_by_id(self, post_id: int) -> Dict[str, Any]:
        """
        Fetches a single post by id from the API.

        :param post_id: The ID of the post to fetch.
        :return: A dictionary representing the post.
        :raises: ValueError if the response is not a dictionary.
        """
        response = self._make_request(f"posts/{post_id}")
        if isinstance(response, dict):
            return response
        raise ValueError("Expected a dictionary for a single post")

    def create_post(self, post_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new post with the given data.

        :param post_data: A dictionary containing the post data.
        :return: A dictionary representing the created post.
        :raises: ValueError if the response is not a dictionary.
        """
        response = self._make_request("posts", method="POST", data=post_data)
        if isinstance(response, dict):
            return response
        raise ValueError("Expected a dictionary for the created post")

    def fetch_users(self) -> List[Dict[str, Any]]:
        """
        Fetches all users from the API.

        :return: A list of users.
        :raises: ValueError if the response is not a list.
        """
        response = self._make_request("users")
        if isinstance(response, list):
            return response
        raise ValueError("Expected a list of users")

    def fetch_comments(self) -> List[Dict[str, Any]]:
        """
        Fetches all comments from the API.

        :return: A list of comments.
        :raises: ValueError if the response is not a list.
        """
        response = self._make_request("comments")
        if isinstance(response, list):
            return response
        raise ValueError("Expected a list of comments")
