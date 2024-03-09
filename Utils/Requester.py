import time
import requests

class Requester:
	def __init__(self, token):
		self.headers = {}
		self.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0"
		self.headers["Accept"] = "application/json, text/javascript, */*; q=0.01"
		self.headers["Content-Type"] = "application/json"
		self.headers["X-Requested-With"] = "XMLHttpRequest"
		self.headers["origin"] = "https://discord.com"
		self.headers["Referer"] = "https://discord.com/"
		self.headers["authorization"] = token
		
		self.baseUrl = "https://discord.com/api/v9/"

	def post(self,url,payload):
		result = requests.post(self.baseUrl + url,data=payload,headers=self.headers)
		return result

	def patch(self,url,data):
		result = requests.patch(self.baseUrl + url,data=data,headers=self.headers)
		return result
	
	def get(self,url,params=None):
		result = requests.get(self.baseUrl + url,headers=self.headers,params=params)
		return result
