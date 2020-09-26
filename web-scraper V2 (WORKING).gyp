"""Uses webscraping to retrieve html information from Google Trends for 
parsing""" 

# Imports 

import time 
import ssl
from requests import get 
from bs4 import BeautifulSoup

# Url for request 

url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"

# Used to create an unverified certificate. 

ssl._create_default_https_context = ssl._create_unverified_context

def html_parser():
    
    start = time.time()
    html = get(url) 

    """Parses the html into storable text""" 
    html_unparsed = html.text
    soup = BeautifulSoup(html_unparsed, "html.parser")
    titles_unformatted = soup.find_all("title")
    traffic_unformatted = soup.find_all("ht:approx_traffic")
    # Indexes through list to make data readable 
    titles = [x.text for x in titles_unformatted] 
    traffic = [] 
    for x in traffic_unformatted: 
        x = x.text 
        x = x.replace("+","")
        x = x.replace(",", "")
        traffic.append(x)
    print(traffic, titles)
    
html_parser() 