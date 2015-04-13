import json

def longest_token():
	# Opens json store of comment data
	raw_data = open('../data.json')
	data = json.load(raw_data)

	longest_tokens = []
	lengths = []
	for d in data:
		for t in d['text'].split(' '):
			if len(t) > 15:
				longest_tokens.append(t)
				lengths.append(len(t))

	print(longest_tokens)
	print(lengths)

longest_token()