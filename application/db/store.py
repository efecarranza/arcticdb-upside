from arctic import Arctic, TICK_STORE

class Store:
    def __init__(self):
        db = Arctic('localhost')
        db.initialize_library('Prices')
        price_lib = db['Prices']
        self.db = price_lib

    def write(self, song_id, df):
        self.db.append(song_id, df, upsert=True)

    def read(self, song_id):
        return self.db.read(song_id).data
