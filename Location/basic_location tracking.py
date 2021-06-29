from Handlers.Structures import DataTypesHandler
from VoiceActions.Commands import say
import requests
import json

url = 'https://extreme-ip-lookup.com/json/'
r = requests.get(url)
data = json.loads(r.content.decode())

# Trying adam's module for data formatting
DataTypesHandler.print_data_recursively(data)
say(data["city"], 0)
