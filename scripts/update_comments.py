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
		for p in p_select:
			if p.text:
				text += p.text
				text += '\n '

		parent = c.getparent()
		# print dir(parent)
		# print parent.getchildren()
		a_select = parent[0]
		a_p_select = a_select.xpath("cite")[0]
		if a_p_select.text == None:
			author = a_p_select[0].text
		else:
			author = a_p_select.text

		t_select = parent[2]
		t_p_select = t_select[0]
		time = t_p_select.text

		results.append({
			'text': text,
			'author': author,
			'time': time
		})

	res = comments[0].xpath("p")

	print len(results)

	f.write(json.dumps(results, indent=4, sort_keys=True))
	f.close()



update_comments()