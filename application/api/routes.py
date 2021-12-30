from application.api import bp
from application.service.price_service import PriceService
from flask import jsonify

@bp.route('/prices/<song_id>', methods=['GET'])
def get_price(song_id):
	service = PriceService()
	res = service.get_latest_bid_ask(song_id)
	return jsonify(res)
