from application.api import bp

@bp.route('/prices/<song_id>', methods=['GET'])
def get_price(song_id):
	return '<p>Price is $100</p>'
