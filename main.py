import webapp2
import base

class Index(webapp2.RequestHander):
	def get(self):
		self.render('home.html')