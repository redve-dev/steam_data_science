import json
from requests import get
import os
import logging

logging.basicConfig(level=logging.INFO, filename='logs')

def get_data_from_api(input_file):
    with open(input_file) as file:
        vals = json.loads(file.read())
        return perform_request(vals)

def get_data_from_file(path):
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        logging.error(f"Path: {path} - Does not exist, or is empty")
        raise OSError
    with open(path, 'r') as file:
        return json.loads(file.read())

def perform_request(parameters):
    api = "https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/?"

    try:
        logging.info('trying to make a request')
        response = get(url=api, params=parameters, timeout=5)
        logging.info('http request performed succesfully')
    except:
        logging.critical("couldn't perform request")
        exit("check logs")
    return json.loads(response.text)

def save_to_file(path, data):
    if not os.access(path, os.W_OK) and os.path.exists(path):
        logging.error(f"no permissions to save the file in {path}")
        raise PermissionError

    with open(path, 'w') as file:
        file.write(json.dumps(data, indent=4))
