import requests



class Auth0Service:
    """
        Base class for both Admin and User interactions with API.
        Requires domain
    """
    def __init__(self, domain):
        self.domain = domain
        if not self.domain:
            raise ValueError("No domain was provided")
        
    def make_request(self, method, endpoint, headers=None, json_payload=None, params=None):
        """
            Any kind of request to API
        """
        url = f"https://{self.domain}{endpoint}"
        try:
            response = requests.request(method=method, url=url, headers=headers, json=json_payload, params=params)
            return response
        except Exception as e:
            print(f"API Error: {method} {url} failed with {e.response.status_code} - {e.response.text}")
            raise

class Auth0ManagementAPI(Auth0Service):
    """
        Class for Admin interactions with API.
        Requires domain and management API token
    """
    def __init__(self, domain, management_api_token):
        super().__init__(domain)
        self.management_api_token = management_api_token
        self.headers = {
            "Authorization": f"Bearer {self.management_api_token}",
            "Content-type": "application/json"
        }
    
    def create_user():
        pass
    def delete_user():
        pass
    
    # TODO: All other functions that are Admin part

class Auth0UserAPI(Auth0Service):
    """
        Class for User interaction with API.
        Requires domain
    """
    def __init__(self, domain, default_app_client_id):
        super().__init__(domain)
        self.headers = {
            "Content-type": "application/json"
        } 
        self.default_app_client_id = default_app_client_id
        # ? Do I need anything else?
    
    def log_in():
        pass

    def do_something():
        pass

    def signup_user(self, email, password, connection="Username-Password-Authentication"):
        """Signs up a new user via the Authentication API."""
        endpoint = "/dbconnections/signup"
        json_payload = {
            "client_id": self.default_app_client_id, # ! what is it?
            "email": email,
            "password": password,
            "connection": connection
        }
        print(f"Auth API: Signing up {email}...")
        response = self.make_request("POST", endpoint, json_payload=json_payload)
        return response

    # TODO: All other functions that are User part
