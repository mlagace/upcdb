import urllib2, json

class UPCDB():
	class UPC():
		def __init__(self, data):
			if data['valid'] == "false":
				self.valid = False
			else:
				self.valid = True

			if 'reason' in data:
				self.reason      = data['reason']
			else:			
				self.name        = data['itemname']
				self.number      = data['number']
				self.description = data['description']
				self.price       = data['price']
				self.ratingsup   = data['ratingsup']
				self.ratingsdown = data['ratingsdown']
				self.reason      = None

		def todict(self):
			return {'valid'       : self.valid,
					'reason'      : self.reason,
					'name'        : self.name,
					'number'      : self.number,
					'description' : self.description,
					'price'       : self.price,
					'ratingsup'   : self.ratingsup,
					'ratingsdown' : self.ratingsdown
					}

	def __init__(self, apikey, api='http://www.upcdatabase.org/api/json'):
		self.apikey = apikey

		if api.endswith("/"):
			self.api = api
		else:
			self.api = '%s/' % (api)

	def get(self, upc):
		try:
			f = urllib2.urlopen('%s%s' % (self.api, '/'.join([self.apikey, upc])))
			return self.UPC(json.loads(f.read()))
		except Exception as e:
			return self.UPC(json.loads({'valid': 'false', 'reason': e.message}))