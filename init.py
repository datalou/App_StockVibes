from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 't04ed79743c10bdb3feb493c26be801f9'

    from .routes import main
    app.register_blueprint(main)

    return app