class Issuer:

    def __init__(self, url):
        self.metadata = ""
        self.name = ""

    @staticmethod
    def discover(url):
        return Issuer(url)

    class Client:

        def __init__(self, call_parameters: dict):
            pass

        def authorization_url(self, auth_payload: dict):
            pass

        def callback_params(self, request):
            pass

        class TokenSet:

            def __init__(self, claims):
                self.claims = claims

        def callback(self, callback_url, params, code_verifier) -> TokenSet:
            return self.TokenSet("some claims")

        def userinfo(self, access_token):
            return "user info"

        def refresh(self) -> TokenSet:
            return self.TokenSet("some claims")
