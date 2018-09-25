from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
	"""根据指定的国家名返回国别码"""
	for code, name in COUNTRIES.items():
		if name == country_name:
			return code

	#若未找到则返回None
	return None