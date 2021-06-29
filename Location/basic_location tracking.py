"""
Author: Ruben Rudov
Date: 29/06/2021
Purpose: Trying some location tracks and its uses
"""

from Handlers.Structures import DataTypesHandler
from Handlers.ColoredStrings import Colors
import requests
import json


def get_data():
    url = 'https://extreme-ip-lookup.com/json/'
    r = requests.get(url)
    data = json.loads(r.content.decode())
    return data


def main():
    data = get_data()
    data["ipName"] = f"{Colors.FAIL}XXX.XXX.XXX.XXX/X{Colors.END}"
    data["query"] = f"{Colors.FAIL}XXX.XXX.XXX.XXX/X{Colors.END}"
    data["ipType"] = f"{Colors.FAIL}IP type is censored{Colors.END}"
    DataTypesHandler.print_data_recursively(data)
    print("\n")

    # say(data["city"], 0)  # Works.. commented for muting the response of the bot ...
    print(f"Latitude X Longitude coordinates: {data['lat']} X {data['lon']}")


if __name__ == "__main__":
    main()
