import webapp2
from base import Base
import json

class Index(Base):
	def get(self):
		self.render('index.html')

class Search(Base):
	def post(self):
		payload = self.request.body
		terms = json.loads(payload)
		term = terms['terms']

		raw_data = open('data.json')
		data = json.load(raw_data)
		print data[0]

		results = []

		for i in data:
			if term in i['text']:
				results.append(i.text)

		self.json(200, results)

app = webapp2.WSGIApplication([
	('/', Index),
	('/search', Search)
],
	debug=True
)