import requests
from bs4 import BeautifulSoup
import csv
import re

# URL of the webpage containing the table
url = "https://eclipse.gsfc.nasa.gov/SEpath/SEpath2001/SE2024Apr08Tpath.html"

# Send an HTTP GET request to fetch the webpage content
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the eclipse path data
    table = soup.find('pre')

    # Extract text from the <pre> tag and split into rows
    rows = table.get_text().split('\n')

    for row in rows:
      info = row.split('  ')
      if len(info) <= 9 and len(info) > 5 and info[0] != '':
        print(info)
