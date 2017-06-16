import json
import sys
import requests
import time
from clint.textui import progress

class DBUploader():
	CARDS_URL = 'https://mtgjson.com/json/AllCards.json'
	
	def upgrade(self):
		etag = self.get_etag()
		
		headers = {}
		if len(etag) > 0:
			headers = {'If-None-Match': etag}

		request = requests.get(self.CARDS_URL, stream=True, headers = headers)
		
		if request.status_code is 200:
			print('Downloading new database...')
			
			json_file = self.load_data(request)
			if json_file is not None:
				with open('AllCards.json', 'w+') as file_cursor:
					file_cursor.write(json.dumps(json_file))

			with open('data.txt', 'w+') as cursor_file:
				cursor_file.write(request.headers.get('ETag'))

			print('done!')


	def get_etag(self):
		with open('data.txt', 'a+') as cursor_file:
			cursor_file.seek(0)
			return cursor_file.readline()


	def load_data(self, request):
		total_length = len(request.content)

		data = b''
		for chunk in progress.bar(request.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
			data += chunk

		return json.loads(data.decode('utf-8'))