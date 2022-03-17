import requests, json, re

class OsmApi:

	def __init__(self, lat, lon, location, zoom=None):
		self.lat = lat
		self.lon = lon
		self.location = location
		self.zoom = zoom

	def get_data(self, txt, form):
		if form == 'json':
			if txt == '[]' or txt == '{}':
				self.lat = self.lon = self.location = ''
			else:
				data = json.loads(txt)
				if type(data) == list:
					data = data[0]
				self.lat = data['lat']
				self.lon = data['lon']
				self.location = data['display_name']
		elif form == 'xml':
			lat = re.search("(?<=lat=').*?'", txt)
			if lat == None:
				self.lat = self.lon = self.location = ''
			else:
				self.lat = lat.group(0)[:-1:]
				self.lon = re.search("(?<=lon=').*?'", txt).group(0)[:-1:]
				self.location = re.search("(?<=display_name=').*?'", txt).group(0)[:-1:]


	def direct_request(self, form='json'):
		URL = f'https://nominatim.openstreetmap.org/search?q={self.location}&format={form}'
		r = requests.post(URL)
		self.get_data(r.text, form)

		return (self.lat, self.lon, r.status_code)

	def reverse_request(self, form='json'):
		URL = f'https://nominatim.openstreetmap.org/reverse.php?lat={self.lat}&lon={self.lon}{["", "&zoom="+self.zoom][int(self.zoom != None)]}&format={form}'
		r = requests.post(URL)
		self.get_data(r.text, form)
		return (self.location, r.status_code)