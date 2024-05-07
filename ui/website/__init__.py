from flask import Flask



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thesecretkey'

    from .builds import builds
    from .users import users
    from .view import view
    from .components import components

    app.register_blueprint(builds, url_prefix='/')
    app.register_blueprint(users, url_prefix='/')
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(components, url_prefix='/')

    return app

