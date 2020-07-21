import requests

class HttpStatusCode:
	def __init__(self, url):
		self.url = url

	def httpGetResponse(self):
		return requests.get(self.url).status_code