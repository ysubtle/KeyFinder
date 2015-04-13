import webapp2
from base import Base
import json
import time

class Index(Base):
	def get(self):
		self.render('index.html')

class Search(Base):
	def post(self):
		payload = self.request.body
		pl_dict = json.loads(payload)
		terms = pl_dict['terms'].split(',')

		raw_data = open('data.json')
		data = json.load(raw_data)
		print data[0]

		results = {
			'comments': [],
			'time': 0
		}

		start_time = time.time()
		for i in data:
			matches = True
			for term in terms:
				if term not in i['text']:
					matches = False
			if matches == True:
				results['comments'].append(i['text'])

		end_time = time.time()

		results['time'] = end_time - start_time

		self.json(200, results)

app = webapp2.WSGIApplication([
	('/', Index),
	('/search', Search)
],
	debug=True
)