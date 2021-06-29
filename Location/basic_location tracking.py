"""
Author: Ruben Rudov
Date: 29/06/2021
Purpose: Trying some location tracks and its uses
"""

from Handlers.Structures import DataTypesHandler
from VoiceActions.Commands import say
import requests
import json

url = 'https://extreme-ip-lookup.com/json/'
r = requests.get(url)
data = json.loads(r.content.decode())

DataTypesHandler.print_data_recursively(data)
say(data["city"], 0)
