import base64
import websocket
import time
import logging

class BaseClient:
    def __init__(self):
        self.username = 'upsideatsbeta@gmail.com'
        self.password = 'testUpside.123'
        self.api_url = ''
        self.stream_url = 'wss://kxf3vqpfbj.execute-api.us-west-2.amazonaws.com/beta'
        self.logger = logging.getLogger(__name__)
        self.msg_received = 0
        self.ws = None

    def on_message(self, ws, msg):
        print("Message received: ", msg)
        self.msg_received += 1
        if self.msg_received > 10:
            ws.close()

    def on_error(self, ws, error):
        print("Error: ", error)


    def on_close(self, ws):
        print("Closing WebSocket...")


    def on_open(self, ws):
        print("Opening WebSocket...")
        time.sleep(1)

    def connect(self):
        email = bytes(self.username, encoding='utf-8')
        pw = bytes(self.password, encoding='utf-8')
        _str = (base64.b64encode(email + b':' + pw)).decode('ascii')
        headerValue = 'Authorization: Basic {0}'.format(_str)

        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(
            "wss://kxf3vqpfbj.execute-api.us-west-2.amazonaws.com/beta",
            header=[headerValue],
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open
        self.ws.run_forever()
