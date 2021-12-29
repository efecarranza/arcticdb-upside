from application import create_app
from threading import Thread
from application.client.base_client import BaseClient

app = create_app()

def start_socket():
    client = BaseClient()
    client.connect()

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
