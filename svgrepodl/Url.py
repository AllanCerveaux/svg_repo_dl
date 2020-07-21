import re
import requests

class Url:
	def __init__(self, url):
		self.url = url

	def httpGetResponse(self):
		"""Return status code of url
		Returns:
			[number] -- Status code
		"""
		return requests.get(self.url).status_code

	def collectionName(self):
		"""Split URL and get collection name
		Arguments:
			url {[string]} -- URL of SVGREPO Collection
		Returns:
			[string] -- Collection Name
		"""
		url_splited = self.url.split('/')
		url_splited = [i for i in url_splited if i]
		return url_splited.pop()

	def checker(self):
		"""Regex check if given by user equal to svgrepo collection
		Arguments:
			url {string} --  URL of SVGREPO Collection
		Return:
			[boolean] -- Check if url match with pattern
		"""
		pattern =  '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)[a-z0-9]+([\-\.]svgrepo+)\.[a-z]{2,5}(\/collection\/)([a-zA-Z0-9-_]+)/?$'
		return re.match(pattern, self.url)
