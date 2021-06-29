"""
Author: Ruben Rudov
Date: 29/06/2021
Purpose: Trying some location tracks and its uses
"""

from Handlers.Structures import DataTypesHandler
from VoiceActions.Commands import say
import requests
import json


def get_data():
    url = 'https://extreme-ip-lookup.com/json/'
    r = requests.get(url)
    data = json.loads(r.content.decode())
    return data


def main():
    data = get_data()
    data["ipName"] = "XXX.XXX.XXX.XXX/X"
    data["query"] = "XXX.XXX.XXX.XXX/X"
    data["ipType"] = "IP type is censored"
    DataTypesHandler.print_data_recursively(data)
    print("\n")

    # say(data["city"], 0)  # Works.. commented for muting the response of the bot ...
    print(f"Latitude X Longitude coordinates: {data['lat']} X {data['lon']}")


if __name__ == "__main__":
    main()
