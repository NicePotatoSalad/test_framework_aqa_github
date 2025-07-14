# api/github_api_client.py
import requests

class GitHubApiClient:
    """
    Client for interacting with the GitHub REST API.
    """
    BASE_URL = "https://api.github.com"

    def __init__(self, token: str = None):
        """
        Initializes the API client.
        :param token: Personal Access Token for authentication.
        """
        self.headers = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }
        if token:
            self.headers["Authorization"] = f"Bearer {token}"
        self.token = token # Сохраняем токен для проверки

    def get_user_profile(self, username: str):
        """
        Fetches public profile information for a given user.
        :param username: The GitHub username.
        :return: requests.Response object.
        """
        url = f"{self.BASE_URL}/users/{username}"
        response = requests.get(url, headers=self.headers)
        return response

    def get_authenticated_user_profile(self): 
        """
        Fetches profile information for the authenticated user.
        Requires authentication.
        :return: requests.Response object.
        """
        if not self.token:
            raise ValueError("Authentication token is required for this operation.")
        url = f"{self.BASE_URL}/user" 
        response = requests.get(url, headers=self.headers)
        return response

    def update_authenticated_user_profile(self, name: str = None, bio: str = None, company: str = None):
        """
        Updates the profile of the authenticated user.
        Requires 'user' scope on the Personal Access Token.
        :param name: New name for the user.
        :param bio: New bio for the user.
        :param company: New company for the user.
        :return: requests.Response object.
        """
        if not self.token:
            raise ValueError("Authentication token is required for this operation.")
        url = f"{self.BASE_URL}/user" # Endpoint for the authenticated user
        payload = {}
        if name is not None:
            payload['name'] = name
        if bio is not None:
            payload['bio'] = bio
        if company is not None:
            payload['company'] = company
        
        if not payload:
            raise ValueError("At least one parameter (name, bio, company) must be provided for update.")

        response = requests.patch(url, json=payload, headers=self.headers)
        return response