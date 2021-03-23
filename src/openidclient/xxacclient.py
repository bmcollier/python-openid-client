import requests


def get_token(client_secret, code) -> str:
    print(code)
    url = "http://localhost:8080/auth/realms/archaeopteryx/protocol/openid-connect/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": "auth-code-flow-client",
        "code": code,
        "redirect_uri": "http://localhost:8000/callback"
    }
    #"client_secret": "4db1f944-7c78-4b22-8d3f-f25a8f31fc3d",
    response = requests.post(url, data=data)
    print(response.json())
    return response.json().get("access_token", "ERROR")
