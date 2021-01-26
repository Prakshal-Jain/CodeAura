import requests
import json
from bs4 import BeautifulSoup

# This function gets all the updated events from MLH website and write the output to a json file. This file can be read at frontend to display events.
# Need to call this function every 24 hours to update the file.

def get_updates(location):
    result = requests.get('https://mlh.io/events')
    content = result.content

    soup = BeautifulSoup(content, 'lxml')
    # Data Structure:
    # [{event-name: ______, event-logo: ______, event-date: ______, ribbon yellow: ______, event-location: ______, event-link:  ______}]

    data = []
    all_events = soup.find_all("div", class_="event-wrapper")
    for info in all_events:
        dict = {}
        dict["event-name"] = info.find("h3", class_="event-name").text
        dict["event-link"] = info.find("a", class_="event-link")["href"]
        dict["event-logo"] = info.find("div", class_="event-logo").find("img")["src"]
        dict["event-date"] = {"start": info.find("meta", itemprop="startDate")["content"],
                              "end": info.find("meta", itemprop="endDate")["content"]}
        dict["event-mode"] = info.find("div", class_="ribbon yellow").text.strip()
        dict["event-location"] = info.find("span", itemprop="city").text + ", " + info.find("span",
                                                                                            itemprop="state").text

        # Filters all the items with non None values
        dict = {k: v for k, v in dict.items() if v is not None}
        data.append(dict)

    retData = json.dumps(data, indent=1)
    f = open(location, "w")
    f.write(retData)
    f.close()


get_updates("hackthons.json")

# Creator: prakshal@buffalo.edu (Prakshal Jain)
# Data-Source: https://mlh.io/events
# Dependency: pip install requests , pip install beautifulsoup4
