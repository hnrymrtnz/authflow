from . import openid_connect
from flask import render_template

@openid_connect.route('/auth_code')
def auth_code_flow():
    return render_template('openid_connect/auth_code.html')

@openid_connect.route('/implicit')
def implicit_flow():
    return render_template('openid_connect/implicit.html')

@openid_connect.route('/client_cred')
def hybrid_flow():
    return render_template('openid_connect/client_cred.html')