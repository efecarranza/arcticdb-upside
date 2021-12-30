from flask import Flask
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

    with app.app_context():
        from application.api import bp as api_bp
        app.register_blueprint(api_bp)

    return app
