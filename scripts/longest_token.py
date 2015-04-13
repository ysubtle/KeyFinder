import json

def longest_token():
	# Opens json store of comment data
	raw_data = open('../data.json')
	data = json.load(raw_data)

	longest_token = ''
	length = 0
	for d in data:
		for t in d['text'].split(' '):
			if len(t) > length:
				longest_token = t
				length = len(t)

	return "Longest token is: " + longest_token + " at " + str(length)

print longest_token()