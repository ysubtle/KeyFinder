import webapp2
import jinja2
import json

env = jinja2.Environment(
    loader=jinja2.PackageLoader('templates', ''),
    trim_blocks=True
)

class Base(webapp2.RequestHandler):
	def render(self, html_path):
		html = env.get_template(html_path)
		self.response.write(html.render({}))

	def json(self, code, ctx):
		self.response.set_status(code)
		self.response.write(json.dumps(ctx))
		return None