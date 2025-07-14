# tests/test_user_profile_api.py
import pytest
from tests.api.client.github_api_client import GitHubApiClient
import os
import random
import string

# --- Configuration ---
TEST_USERNAME = "NicePotatoSalad" 

GITHUB_PAT = os.environ.get("GITHUB_PAT") 
if not GITHUB_PAT:
    # Fallback for local testing if env var not set, remove for production!
    print("WARNING: GITHUB_PAT environment variable not set. Using a dummy value (API update tests will fail).")
    # You MUST replace this with your actual token for update tests to pass!
    # GITHUB_PAT = "ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


# --- Fixture for API Client ---
@pytest.fixture(scope="module")
def api_client():
    """
    Provides a GitHubApiClient instance for API tests.
    Uses 'module' scope as client can be reused across tests in the module.
    """
    if not GITHUB_PAT:
        pytest.skip("GITHUB_PAT environment variable not set. Skipping API tests that require authentication.")
    return GitHubApiClient(token=GITHUB_PAT)

@pytest.fixture(scope="function") 
def restore_user_bio(api_client):
    """
    Fixutre for saving current user bio before the test and 
    recovering afterwards
    """
    # SETUP
    print("\n--- Setup: Saving original user bio ---")
    response = api_client.get_authenticated_user_profile()
    if response.status_code != 200:
        pytest.fail(f"Failed to get authenticated user profile for cleanup setup: {response.text}")
    
    original_bio = response.json().get("bio", "")
    print(f"Original bio: '{original_bio}'")

    yield # Здесь будет выполняться сам тест

    # TEARDOWN
    print(f"\n--- Teardown: Restoring user bio to original: '{original_bio}' ---")
    restore_response = api_client.update_authenticated_user_profile(bio=original_bio)
    if restore_response.status_code != 200:
        print(f"WARNING: Failed to restore user bio. Status: {restore_response.status_code}, Response: {restore_response.text}")
        pytest.fail("Failed to update the user bio")
    else:
        print("User bio restored successfully.")


# --- Test Functions ---

def test_get_public_user_profile_success(api_client):
    """
    Test: Verify fetching public user profile data for a known user.
    """
    response = api_client.get_user_profile(TEST_USERNAME)

    # 1. Assert HTTP Status Code
    assert response.status_code == 200, \
        f"Expected status 200 for public profile, got {response.status_code}. Response: {response.text}"

    # 2. Assert JSON response structure and content
    user_data = response.json()

    assert "login" in user_data, "Response JSON missing 'login' field"

    assert user_data["login"] == TEST_USERNAME, \
        f"Expected username '{TEST_USERNAME}', got '{user_data['login']}'"
    
    assert "id" in user_data, "Response JSON missing 'id' field"
    assert "public_repos" in user_data, "Response JSON missing 'public_repos' field"
    assert isinstance(user_data["public_repos"], int), "'public_repos' is not an integer"

    print(f"Successfully fetched profile for {TEST_USERNAME}. Public Repos: {user_data['public_repos']}")


def test_get_public_user_profile_not_found(api_client):
    """
    Test: Verify fetching profile for a non-existent user returns 404.
    """
    non_existent_username = "this-user-definitely-does-not-exist-1234567890abc"
    response = api_client.get_user_profile(non_existent_username)

    assert response.status_code == 404, \
        f"Expected status 404 for non-existent user, got {response.status_code}. Response: {response.text}"
    
    error_data = response.json()
    assert "message" in error_data, "Error response missing 'message' field"
    assert "Not Found" in error_data["message"], "Error message does not contain 'Not Found'"


@pytest.mark.skipif(not GITHUB_PAT, reason="Requires GITHUB_PAT environment variable for authentication.")
def test_update_user_bio_empty(api_client, restore_user_bio):
    """
    Test: Update the authenticated user's profile bio to be empty.
    """
    response = api_client.update_authenticated_user_profile(bio="")

    assert response.status_code == 200, \
        f"Expected status 200 for empty bio update, got {response.status_code}. Response: {response.text}"
    
    updated_profile_data = response.json()
    assert "bio" in updated_profile_data, "Updated profile response missing 'bio' field"
    assert updated_profile_data["bio"] == "" or updated_profile_data["bio"] == None, \
        f"Bio not emptied correctly. Expected empty, got '{updated_profile_data['bio']}'"
    
    print("Bio successfully emptied.")

    # Clean up: restore original bio
    # For MVP, we'll leave it as is. In real scenarios, restore to a known state.
    # For this specific test, if you run it repeatedly, your bio will be empty.
    # Consider restoring a default bio after this test.