from flask import Blueprint

saml = Blueprint('saml', __name__, template_folder='templates')

from . import routes