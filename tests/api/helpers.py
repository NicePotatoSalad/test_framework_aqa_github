import requests

# Helper to get the Management API token (used by fixtures)
def get_management_api_access_token_internal(domain, client_id, client_secret):
    """Internal function to get the M2M token."""
    token_url = f"https://{domain}/oauth/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "audience": f"https://{domain}/api/v2/",
        "grant_type": "client_credentials"
    }
    response = requests.post(token_url, json=payload)
    response.raise_for_status()
    return response.json()["access_token"]
