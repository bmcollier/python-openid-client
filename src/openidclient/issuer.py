class TokenSet:

    def __init__(self, claims):
        self.claims = claims


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

        def callback(self, callback_url, params, code_verifier) -> TokenSet:
            return TokenSet("some claims")

        def userinfo(self, access_token):
            return "user info"

        def refresh(self) -> TokenSet:
            return TokenSet("some claims")

        class Handle:

            def __init__(self, user_code, verification_uri, verification_uri_complete):
                self.user_code = user_code
                self.verification_uri = verification_uri
                self.verification_uri_complete = verification_uri_complete

            def poll(self):
                # Keep on polling until we have a tokenset
                return TokenSet("some claims")

        def get_device_authorization(self):
            return self.Handle("code", "uri", "complete_uri")

