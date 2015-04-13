from lxml import html
import requests
import json

def update_comments():
	f = open('../data.json', 'w')
	results = []
	page = requests.get('http://www.dcrainmaker.com/2015/01/stryd-first-running.html')
	tree = html.fromstring(page.text)
	print tree
	comments = tree.xpath('//*[@class="comment-body"]')

	for c in comments:
		p_select = c.xpath("p")
		text = ''
		# Selects all p elements in comment-body and extracts text
		for p in p_select:
			if p.text_content():
				text += p.text_content()
				text += '\n '

		# Selects parent element of comment-body
		parent = c.getparent()
		# Grabs author element
		a_select = parent[0]
		# Selects author name
		a_p_select = a_select.xpath("cite")[0]
		if a_p_select.text_content() == None:
			author = a_p_select[0].text_content()
		else:
			author = a_p_select.text_content()

		# Grabs date element
		t_select = parent[2]
		t_p_select = t_select[0]
		# Select date text
		time = t_p_select.text_content()

		results.append({
			'text': text,
			'author': author,
			'time': time
		})

	# Verifies # of comments
	print len(results)

	f.write(json.dumps(results, indent=4, sort_keys=True))
	f.close()

update_comments()