import json
from requests import get
import os
import logging

logging.basicConfig(level=logging.DEBUG, filename='logs')

class data_getter:
    def __init__(self,input_file='input.json', LoadFromFile=False, data_path='data.json'):
        if LoadFromFile:
            self.data = self.load_from_file(data_path)
            return

        if not os.path.exists(input_file) or os.path.getsize(input_file) == 0:
            logging.error(f"Couldn't read input file: {input_file}")
            raise OSError

        with open(input_file) as file:
            vals = json.loads(file.read())
            self.data = self.perform_request(vals)

    def load_from_file(self, path):
        if not os.path.exists(path) or os.path.getsize(path) == 0:
            logging.error(f"Path: {path} - Does not exist, or is empty")
            raise OSError

        with open(path, 'r') as file:
            return json.loads(file.read())

    def perform_request(self, data):
        api = "https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?"

        try:
            logging.info('trying to make a request')
            response = get(url=api, params=data, timeout=5)
            logging.info('http request performed succesfully')
        except:
            logging.critical("couldn't perform request")
            exit("check logs")
        return json.loads(response.text)

    def save_to_file(self, path):
        if not os.access(path, os.W_OK):
            logging.error(f"no permissions to save the file in {path}")
            raise PermissionError

        with open(path, 'w') as file:
            file.write(json.dumps(self.data, indent=4))

    def __str__(self):
        return str(self.data)

    def get_data(self):
        return self.data
