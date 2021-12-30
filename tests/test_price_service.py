import pandas as pd
from application.service.price_service import PriceService
from datetime import datetime

def test_create_dataframe():
	service = PriceService()
	msg = {"bookPrices":{"WHOAMI":{"bid":1.8,"ask":1.88}}}
	df = pd.DataFrame(data={
		'bid': [msg['bookPrices']['WHOAMI']['bid']],
		'ask': [msg['bookPrices']['WHOAMI']['ask']],
		'timestamp': [datetime.now()]
	})
	res = service.msg_to_dataframe(msg)
	assert df['bid'].equals(res['bid'])
	assert df['ask'].equals(res['ask'])

def test_write_to_db():
	service = PriceService()
	msg = {"bookPrices":{"WHOAMI":{"bid":1.8,"ask":1.88}}}
	df = pd.DataFrame(data={
		'bid': [msg['bookPrices']['WHOAMI']['bid']],
		'ask': [msg['bookPrices']['WHOAMI']['ask']],
		'timestamp': [datetime.now()]
	})
	res = service.msg_to_dataframe(msg)
	service.store_data('WHOAMI', res)
