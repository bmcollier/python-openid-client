import requests

class Connection:

    def __init__(self, url): #, auth_token_endpoint, token_endpoint, client_id, client_secret, scope):
        #response = requests.get(connection)
        #print(response.text)
        self.url = url

    def get_token(self, grant_type, client_id, client_secret, username, password, scope) -> str:
        data = {
            "grant_type": grant_type,
            "client_id": client_id,
            "client_secret": client_secret,
            "username": username,
            "password": password,
            "scope": scope
        }
        response = requests.post(self.url, data=data)
        return response.json().get("access_token", None)