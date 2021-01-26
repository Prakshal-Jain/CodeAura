import csv

import requests
import json
from bs4 import BeautifulSoup
import itertools
from openpyxl import Workbook

# This function gets all the updated events from MLH website and write the output to a json file. This file can be read at frontend to display events.
# Need to call this function every 24 hours to update the file. Generates JSON and CSV files.

def get_updates(filename):
    result = requests.get('https://mlh.io/events')
    content = result.content

    soup = BeautifulSoup(content, 'lxml')
    # Data Structure:
    # [{event-name: ______, event-logo: ______, event-start-date: ______, event-end-date: ______, ribbon yellow: ______, event-location: ______, event-link:  ______}]

    data = []
    all_events = soup.find_all("div", class_="event-wrapper")
    for info in all_events:
        dict = {}
        dict["event-name"] = info.find("h3", class_="event-name").text
        dict["event-link"] = info.find("a", class_="event-link")["href"]
        dict["event-logo"] = info.find("div", class_="event-logo").find("img")["src"]
        dict["event-start-date"] = info.find("meta", itemprop="startDate")["content"]
        dict["event-end-date"] = info.find("meta", itemprop="endDate")["content"]
        dict["event-mode"] = info.find("div", class_="ribbon yellow").text.strip()
        dict["event-location"] = info.find("span", itemprop="city").text + ", " + info.find("span",
                                                                                            itemprop="state").text

        # Filters all the items with non None values
        dict = {k: v for k, v in dict.items() if v is not None}
        data.append(dict)

    retData = json.dumps(data, indent=1)
    f = open(filename+".json", "w")
    f.write(retData)
    f.close()

    with open(filename+".csv", 'w') as csvfile:
        fields = ["event-name", "event-link", "event-logo", "event-start-date", "event-end-date", "event-mode", "event-location"]
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for d in data:
            writer.writerow(d)


get_updates("hackthons")

# Creator: prakshal@buffalo.edu (Prakshal Jain)
# Data-Source: https://mlh.io/events
# Dependency: pip install requests , pip install beautifulsoup4
