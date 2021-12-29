from flask import Flask
# from flask_migrate import Migrate
# from application.api import bp
# from application.model import db
from threading import Thread
from application.client.base_client import BaseClient

def start_socket():
    client = BaseClient()
    client.connect()

def create_app():
    thread = Thread(target=start_socket)
    thread.daemon = True
    thread.start()
    app = Flask(__name__)
    # app.config.from_object('config.Config')

    # db.init_app(app)

    with app.app_context():
        from application.api import bp as api_bp
    #     from application.model import OAuth, User

    #     migrate = Migrate(app, db)
        app.register_blueprint(api_bp)

    return app

# from application import model