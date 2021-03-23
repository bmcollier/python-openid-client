from openidclient.issuer import Issuer
issuer = Issuer.discover('https://accounts.google.com')
print('Discovered issuer {} {}', issuer.name, issuer.metadata)

client = issuer.Client({
  "client_id": 'zELcpfAN44LqY7Oqas',
  "redirect_uris": ['http://localhost:3000/cb'],
  "response_types": ['id_token'],
  # id_token_signed_response_alg (default "RS256")
})

client.authorizationUrl({
  "scope": 'openid email profile',
  "response_mode": 'form_post',
  "nonce": "nonce",
})

params = client.callback_params(req)
token_set = client.callback('https://client.example.com/callback', params, nonce)
print("Received and validated tokens {}", token_set)
print("Validated ID Token claims {}", token_set.claims())

