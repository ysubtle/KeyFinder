import webapp2
from base import Base

class Index(Base):
	def get(self):
		self.render('index.html')

app = webapp2.WSGIApplication([
	('/', Index)
],
	debug=True
)