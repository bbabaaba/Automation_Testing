import requests

class HttpRequest(object):
	
	def __init__(self,url,host='http://mobile.ximalaya.com',token=None):
		self.url = url
		self.host = host
		self.token = token

	def get(self,with_token=False,headers=None):
		if with_token == False:
			if headers == None:
				headers = {'User-Agent': 'ting_v4.7.1_c11(CFNetwork, iPhone OS 8.4, iPhone6,2)'}
			url = self.host+self.url
			#print url
			res = requests.get(url=url,
                    headers=headers)
			return res
		else:
			if headers == None:
				headers = {'Cookie':'1&_token='+self.token,'User-Agent': 'ting_v4.7.1_c11(CFNetwork, iPhone OS 8.4, iPhone6,2)'}
			url = self.host+self.url
			#print url
			res = requests.get(url=url,
                    headers=headers)
			return res
		
	def post(self,datas=None,content_type='application/x-www-form-urlencoded',headers=None):
		if datas == None:
			return 'please input correct datas.'
		if content_type == 'application/x-www-form-urlencoded':
			if headers == None:
				headers = {'Cookie':'1&_token='+self.token,'User-Agent': 'ting_v4.7.1_c11(CFNetwork, iPhone OS 8.4, iPhone6,2)'}
			url = self.host+self.url
			#print url
			res = requests.post(url=url,
                    data=datas,
                    headers=headers)
			return res
		elif content_type == 'application/octet-stream':
			url = self.host+self.url
			#print url
			res = requests.post(url=url,
                    data=datas,
                    headers={u'Content-Type':u'application/octet-stream',u'Content-Length':str(len(datas)),'User-Agent': 'ting_v4.7.1_c11(CFNetwork, iPhone OS 8.4, iPhone6,2)'})
			return res
		#'''
		elif content_type == 'multipart/form-data':
			url = self.host+self.url
			#print url
			res = requests.post(url=url,
                    data=datas,
                    headers=headers)
			return res
		#'''