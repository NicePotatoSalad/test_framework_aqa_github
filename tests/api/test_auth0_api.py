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

# * VARIABLES
AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
MACHINE_CLIENT_ID = os.getenv("AUTH0_MACHINE_CLIENT_ID")
MACHINE_CLIENT_SECRET = os.getenv("AUTH0_MACHINE_CLIENT_SECRET")

# * FIXTURES
@pytest.fixture(scope="module")
def get_management_api_client(): 
    """
    Pytest fixture to provide a token for Admin interactions
    """
    token = get_management_api_access_token_internal(AUTH0_DOMAIN, MACHINE_CLIENT_ID, MACHINE_CLIENT_SECRET)
    return token


