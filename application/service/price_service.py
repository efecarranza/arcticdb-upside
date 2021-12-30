import pandas as pd
from application.db.store import Store
from datetime import datetime

class PriceService:
    def __init__(self):
        self.db = Store()

    def msg_to_dataframe(self, prices):
        for k,v in prices['bookPrices'].items():
            price_data = {
                'bid': [v['bid']],
                'ask': [v['ask']],
                'timestamp': [datetime.now()]
            }
            df = pd.DataFrame(data=price_data)
            self.store_data(k, df)
            return df

    def store_data(self, song_id, df):
        self.db.write(song_id, df)
        print(self.db.read(song_id))
