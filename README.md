# authflow

## Welcome to Authflow!
This application provides users with the ability to visualize different single sign-on flows, depending on the protocol being used.

Created using Python, this app is hosted on Heroku and uses Auth0 as its identity provider. If you would like to clone and use a different provider, you are able to do so, by changing the config.py file settings.

### OpenID Connect
As of now, the only support flows for OpenID Connect are authorization code flow and implicit flow. The code credentials flow is coming soon.

### SAML
There are no SAML flows currently supported, but SP-initialized flows will be supported in the future.

