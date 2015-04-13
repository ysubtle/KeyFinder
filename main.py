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
		# Grabs JSON input and puts it in dict
		payload = self.request.body
		pl_dict = json.loads(payload)

		# Split the comma seperated terms
		terms = pl_dict['terms'].split(',')
		# Create a regex that matches if any of the terms are present. Each term must be surronded by non letter characters.
		pattern = '(\W('
		for term in terms:
			if term != '':
				pattern += re.escape(term)
				pattern += '|'
		pattern = pattern[:-1]
		pattern += ')\W)'

		# Opens json store of comment data
		raw_data = open('data.json')
		data = json.load(raw_data)

		# Creates result dictionary
		results = {
			'comments': [],
			'time': 0
		}

		# Start search timer
		start_time = time.time()

		# Looks at each comment
		for i in data:
			matches = False
			# If regex match, flag for match
			if re.search(pattern, i['text'], re.I):
				matches = True
			# Appends to result list
			if matches == True:
				results['comments'].append(i)

		# Stop search timer
		end_time = time.time()

		results['time'] = end_time - start_time

		# Returns result in JSON
		self.json(200, results)

app = webapp2.WSGIApplication([
	('/', Index),
	('/search', Search)
],
	debug=True
)