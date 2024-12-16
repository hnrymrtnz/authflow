SECRET_KEY = 'N3n2-bJko1n49Am2-J015I'

# OpenID Connect Keycloak Configuration
ISSUER = 'https://dev-efxkhtkp2616hoy5.us.auth0.com/'
AUTHORIZATION_ENDPOINT = 'https://dev-efxkhtkp2616hoy5.us.auth0.com/authorize'
TOKEN_ENDPOINT = 'https://dev-efxkhtkp2616hoy5.us.auth0.com/oauth/token'
USERINFO_ENDPOINT = 'https://dev-efxkhtkp2616hoy5.us.auth0.com/userinfo'

# Authorization Code Flow
AC_CLIENT_ID = '1XBtyViD2SOHwfbmLFH5wU4EIDP80JDX'
AC_CLIENT_SECRET = 'h_2vGN5sxwl24zOaGZfM9csL-uu7bpwTEuqJckO17tcX5YW3tgrWE7NLK4YkPnyO'
AC_SCOPES = 'openid profile'
AC_REDIRECT_URI = 'http://localhost:5000/openid_connect/auth_code/callback'

# Implicit Grant Flow
I_CLIENT_ID = 'uNMHvwCmP9l7iPGIayptGzjftoHE23Lw'
I_CLIENT_SECRET = 'os5Y2ojOzdEVexOVwOED3nDGpbj6RxhBmEQrogDlTPBYMDVgZr2bznRGYSfHu3u4'
I_SCOPES = 'openid profile'
I_REDIRECT_URI = 'http://localhost:5000/openid_connect/implicit/callback'

