from openidclient.issuer import Issuer
issuer = Issuer.discover('https://accounts.google.com')
print('Discovered issuer {} {}', issuer.name, issuer.metadata)

client = issuer.Client({
  "client_id": 'zELcpfAN33LqY7Oqas',
  "redirect_uris": ['http://localhost:3000/cb'],
  "response_types": ['id_token'],
  # id_token_signed_response_alg (default "RS256")
})

handle = client.get_device_authorization()
print("User Code: {}", handle.user_code)
print("Verification URI: {}", handle.verification_uri)
print("Verification URI (complete): {}", handle.verification_uri_complete)

token_set = handle.poll()
print("Received tokens {}", token_set)

