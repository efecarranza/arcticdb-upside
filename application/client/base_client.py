import base64
import websocket
import time
import logging
import json
from application.service.price_service import PriceService
from application.db.store import Store

class BaseClient:
    def __init__(self):
        self.username = 'upsideatsbeta@gmail.com'
        self.password = 'testUpside.123'
        self.api_url = ''
        self.stream_url = 'wss://kxf3vqpfbj.execute-api.us-west-2.amazonaws.com/beta'
        self.logger = logging.getLogger(__name__)
        self.msg_received = 0
        self.ws = None
        self.service = PriceService(Store())

    def on_message(self, ws, msg):
        print("Message received: ", msg)
        self.msg_received += 1
        msg_dict = json.loads(msg)
        self.process_msg(msg_dict)
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

        self.ws = websocket.WebSocketApp(
            "wss://kxf3vqpfbj.execute-api.us-west-2.amazonaws.com/beta",
            header=[headerValue],
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.ws.on_open = self.on_open
        self.ws.run_forever()

    def process_msg(self, msg):
        df = self.service.msg_to_dataframe(msg)
