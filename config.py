SECRET_KEY = 'N3n2-bJko1n49Am2-J015I'

# OpenID Connect Keycloak Configuration
ISSUER = 'http://localhost:8080/realms/master'
CLIENT_ID = 'authflow-client'
CLIENT_SECRET = 'NYKmCduux6hPI60dLPiFoIQ5jwpnehoc'
SCOPES = 'openid'
REDIRECT_URI = 'http://localhost:5000/openid_connect/auth_code/callback'
AUTHORIZATION_ENDPOINT = 'http://localhost:8080/realms/master/protocol/openid-connect/auth'
TOKEN_ENDPOINT = 'http://localhost:8080/realms/master/protocol/openid-connect/token'
USERINFO_ENDPOINT = '"http://localhost:8080/realms/master/protocol/openid-connect/userinfo'