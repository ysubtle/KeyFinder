import webapp2
from base import Base
import json
import time
import re

class Index(Base):
	def get(self):
		self.render('index.html')

class Search(Base):
	def post(self):
		payload = self.request.body
		pl_dict = json.loads(payload)
		terms = pl_dict['terms'].split(',')
		pattern = '(\W('
		for term in terms:
			pattern += re.escape(term)
			pattern += '|'
		pattern = pattern[:-1]
		pattern += ')\W)'

		print "PATTERN",pattern

		raw_data = open('data.json')
		data = json.load(raw_data)

		results = {
			'comments': [],
			'time': 0
		}

		start_time = time.time()
		for i in data:
			matches = False
			if re.search(pattern, i['text'], re.I):
				matches = True
			if matches == True:
				results['comments'].append(i)

		end_time = time.time()

		results['time'] = end_time - start_time

		self.json(200, results)

app = webapp2.WSGIApplication([
	('/', Index),
	('/search', Search)
],
	debug=True
)