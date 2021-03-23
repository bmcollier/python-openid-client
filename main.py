from src.openidclient import xxclient
from src.callback import server

def run():
    grant_type = "password"
    client_id = "test"
    client_secret = "9629249e-be2d-41f0-b057-1431d0401ba9",
    username = "ben"
    password = "wilson1"
    scope = "openid"
    endpoint = "http://localhost:8080/auth/realms/master/protocol/openid-connect/token"
    connection = xxclient.Connection(endpoint)
    print(connection.get_token(grant_type, client_id, client_secret, username, password, scope))


if __name__ == '__main__':
    server.serve()


