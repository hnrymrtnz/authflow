SECRET_KEY = 'N3n2-bJko1n49Am2-J015I'

# OpenID Connect Keycloak Configuration
ISSUER = 'http://localhost:8080/realms/master'
AUTHORIZATION_ENDPOINT = 'http://localhost:8080/realms/master/protocol/openid-connect/auth'
TOKEN_ENDPOINT = 'http://localhost:8080/realms/master/protocol/openid-connect/token'
USERINFO_ENDPOINT = '"http://localhost:8080/realms/master/protocol/openid-connect/userinfo'

# Authorization Code Flow
AC_CLIENT_ID = 'authflow-auth_code'
AC_CLIENT_SECRET = 'NYKmCduux6hPI60dLPiFoIQ5jwpnehoc'
AC_SCOPES = 'openid'
AC_REDIRECT_URI = 'http://localhost:5000/openid_connect/auth_code/callback'

# Implicit Grant Flow
I_CLIENT_ID = 'authflow-implicit'
I_CLIENT_SECRET = 'ccw31u7PtazDXqgTt3UDA8al6xGKUhKg'
I_SCOPES = 'openid'
I_REDIRECT_URI = 'http://localhost:5000/openid_connect/implicit/callback'

