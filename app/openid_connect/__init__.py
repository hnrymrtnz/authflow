from flask import Blueprint

openid_connect = Blueprint('openid_connect', __name__, template_folder='templates')

from . import routes