from . import openid_connect
from config import *
from flask import render_template, redirect, request, session
import requests, jwt

#########################################################################################################################

@openid_connect.route('/auth_code')
def auth_code_flow():
    return render_template('auth_code.html')

@openid_connect.route('/auth_code/auth')
def auth_code_flow_auth():
    try:
        issuer = ISSUER
    except:
        return 'Missing OpenID provider issuer URL. Update the "config.py" file and try again.'

    auth_endpoint = AUTHORIZATION_ENDPOINT
    redirect_uri = AC_REDIRECT_URI
    client_id = AC_CLIENT_ID
    scopes = AC_SCOPES

    auth_url = auth_endpoint + \
        '?redirect_uri=' + redirect_uri + \
        '&client_id=' + client_id + \
        '&response_type=code' + \
        '&scope=' + scopes 

    return redirect(auth_url)

@openid_connect.route('/auth_code/callback')
def auth_code_flow_callback():
    session['code'] = request.args.get('code')
    session['session_state'] = request.args.get('session_state')

    return render_template('auth_code/callback.html', code=session['code'], state=session['session_state'])

@openid_connect.route('/auth_code/token')
def auth_code_flow_token():
    token_url = TOKEN_ENDPOINT

    data = {'grant_type':'authorization_code', 'code':session['code'], \
        'redirect_uri':AC_REDIRECT_URI, 'client_id':AC_CLIENT_ID, \
        'client_secret':AC_CLIENT_SECRET}

    response = requests.post(token_url, data, verify=False)
    response = response.json()

    session['access_token'] = response['access_token']
    session['id_token'] = response['id_token']

    return render_template('auth_code/token.html', access_token=session['access_token'], id_token=session['id_token'])

@openid_connect.route('/auth_code/claims')
def auth_code_flow_claims():
    claims = jwt.decode(session['id_token'], options={"verify_signature": False})

    return render_template('auth_code/claims.html', claims=claims)

#########################################################################################################################

@openid_connect.route('/implicit')
def implicit_flow():
    return render_template('implicit.html')

@openid_connect.route('/implicit/auth')
def implicit_flow_auth():
    try:
        issuer = ISSUER
    except:
        return 'Missing OpenID provider issuer URL. Update the "config.py" file and try again.'

    auth_endpoint = AUTHORIZATION_ENDPOINT
    redirect_uri = I_REDIRECT_URI
    client_id = I_CLIENT_ID
    scopes = I_SCOPES

    auth_url = auth_endpoint + \
        '?redirect_uri=' + redirect_uri + \
        '&client_id=' + client_id + \
        '&response_type=token' + \
        '&scope=' + scopes 

    return redirect(auth_url)

@openid_connect.route('/implicit/callback')
def implicit_flow_callback():
    session['access_token'] = request.args.get('access_token')
    session['id_token'] = request.args.get('id_token')
    session['session_state'] = request.args.get('session_state')

    return render_template('implicit/callback.html', access_token=session['access_token'], id_token=session['id_token'], state=session['session_state'])

#########################################################################################################################

@openid_connect.route('/client_cred')
def hybrid_flow():
    return render_template('openid_connect/client_cred.html')