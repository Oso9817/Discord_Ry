import urllib.request, json, sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

#from lbcapi import api

class checkOnline():
	"""docstring for ClassName"""
	def __init__(self):
			self.user = None
			self.USMC = 'USMC1991'
			self.Jay = 'Jay909'
			self.checkProfile = 1
			#self.whomOnline()


	def requestUrl(self, url):
		req = urllib.request.Request(
    	url, 
    	data=None, 
    	headers={
        	'User-Agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'
    	}
		)

		self.rawData = urllib.request.urlopen(req)
		self.string = self.rawData.read().decode('utf-8')
		print(self.string)
#https://localbitcoins.com/accounts/profile/USMC1991/
#https://localbitcoins.com/accounts/profile/Jay909/
	def whomOnline(self):
		self.checkProfile = int(input('1) USMC1991 \n2) Jay909 \n> '))
		print(self.checkProfile)
	#check for online-status online-status-online in source code of profs
	def checkOnline(self):
		if self.checkProfile == 1:
			try:
				self.requestUrl('https://localbitcoins.com/accounts/profile/USMC1991/')
			except Exception as e:
				raise e
		if self.checkProfile == 2:
			try:
				self.requestUrl('https://localbitcoins.com/accounts/profile/Jay909/')
			except Exception as e:
				raise e

			

checkOnline().checkOnline()




