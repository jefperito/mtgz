import json
import requests

class DBUploader():
	CARDS_URL = 'https://mtgjson.com/json/AllCards.json'

	def upgrade(self):
		request = requests.get(self.CARDS_URL)
		json_file = json.loads(request.content.decode('utf-8'))
		
		if json_file is not None:
			with open('AllCards.json', 'w+') as file_cursor:
				file_cursor.write(json.dumps(json_file))

