import requests
import pytest
import time

# Import API services
from client.auth0_service_objects import Auth0UserAPI, Auth0ManagementAPI, Auth0Service

# Import helpers
from helpers import get_management_api_access_token_internal

import os
from dotenv import load_dotenv

load_dotenv()

# * --- VARIABLES ---
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
MACHINE_CLIENT_ID = os.getenv("AUTH0_MACHINE_CLIENT_ID")
MACHINE_CLIENT_SECRET = os.getenv("AUTH0_MACHINE_CLIENT_SECRET")
DEFAULT_APP_CLIENT_ID = os.getenv("AUTH0_DEFAULT_APP_CLIENT_ID")

# * --- FIXTURES ---
@pytest.fixture(scope="module")
def admin_api_client() -> Auth0ManagementAPI: 
    """
        Pytest fixture to provide an instance of Admin API class
    """
    token = get_management_api_access_token_internal(AUTH0_DOMAIN, MACHINE_CLIENT_ID, MACHINE_CLIENT_SECRET)
    return Auth0ManagementAPI(AUTH0_DOMAIN, token)

@pytest.fixture(scope="module")
def user_api_client() -> Auth0UserAPI:
    """
        Pytest fixture to provide an instance of User API class for easier interactions
    """
    return Auth0UserAPI(AUTH0_DOMAIN, DEFAULT_APP_CLIENT_ID)

# * --- TESTS ---
def test_something(user_api_client : Auth0UserAPI):
    email = "random@gmail.com"
    password = "StrongPassword!123"
    response : requests.Response = user_api_client.signup_user(email, password)

    assert response.status_code == 200, \
        f"Status code is {response.status_code}, but supposed to be {200}, \
        JSON = {response.json}"