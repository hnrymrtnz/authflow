from flask import Blueprint

openid_connect = Blueprint('openid_connect', __name__, template_folder='templates/openid_connect')

from . import routes