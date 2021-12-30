from application.api import bp
from application.service.price_service import PriceService
from application.db.store import Store
from flask import jsonify

service = PriceService(Store())

@bp.route('/prices/<song_id>', methods=['GET'])
def get_price(song_id):
	res = service.get_latest_bid_ask(song_id)
	return jsonify(res)
