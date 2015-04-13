import webapp2

env = jinja2.Environment(
    loader=jinja2.PackageLoader('app', 'templates'),
    trim_blocks=True
)

class Base(webapp2.RequestHandler):
	def render(self, html_path):
		html = env.get_template(html_path)
		self.response.write(html.render({}))