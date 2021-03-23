from openidclient.issuer import Issuer
issuer = Issuer.discover('https://accounts.google.com')
print('Discovered issuer {} {}', issuer.name, issuer.metadata)

#second test
client = issuer.Client({
  "client_id": 'zELcpfANLqY7Oqas',
  "client_secret": 'TQV5U29k1gHibH5bx1layBo0OSAvAbRT3UYW3EWrSYBB5swxjVfWUa1BS8lqzxG/0v9wruMcrGadany3',
  "redirect_uris": ['http://localhost:3000/cb'],
  "response_types": ['code'],
  # id_token_signed_response_alg (default "RS256")
  # token_endpoint_auth_method (default "client_secret_basic")
})

from openidclient import generators
code_verifier = generators.code_verifier()
# store the code_verifier in your framework's session mechanism, if it is a cookie based solution
# it should be httpOnly (not readable by javascript) and encrypted.

code_challenge = generators.code_challenge(code_verifier)

client.authorization_url({
  "scope": 'openid email profile',
  "resource": 'https://my.api.example.com/resource/32178',
  "code_challenge": True,
  "code_challenge_method": "S256"
})

#Following a token with an auth code

params = client.callback_params(req)
token_set = client.callback('https://client.example.com/callback', params, code_verifier)
print("Received and validated tokens {}", token_set)
print("Validated ID Token claims {}", token_set.claims())

#Then call the userinfo endpoint

userinfo = client.userinfo(access_token)
print("userinfo {}", userinfo)