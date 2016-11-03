import json
import sys
import requests
import time
from clint.textui import progress

class DBUploader():
	CARDS_URL = 'https://mtgjson.com/json/AllCards.json'
	
	def upgrade(self):
		data = b''
		request = requests.get(self.CARDS_URL, stream=True)
		total_length = int(request.headers.get('content-length'))

		for chunk in progress.bar(request.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
			data += chunk

		json_file = json.loads(data.decode('utf-8'))

		if json_file is not None:
			with open('AllCards.json', 'w+') as file_cursor:
				file_cursor.write(json.dumps(json_file))
