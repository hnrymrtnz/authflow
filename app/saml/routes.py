from . import saml
from flask import render_template

@saml.route('/sp')
def index():
    return render_template('saml/sp.html')