from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .openid_connect import openid_connect as openid_connect_blueprint
    app.register_blueprint(openid_connect_blueprint, url_prefix='/openid_connect')

    from .saml import saml as saml_blueprint
    app.register_blueprint(saml_blueprint, url_prefix='/saml')

    return app