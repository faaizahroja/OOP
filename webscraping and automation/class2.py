# Topic: Scrap data from a static website
# packages needed: 
# 1. requests - to request data from the website
# 2. BeautifulSoup - to beautify the data
# Installation process:
# pip install requests
# pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
res = request.get(url)
soup = BeautyfulSoup(res.text, "html.parser")

quotes = soup.find_all("span", class_="text")
for q in quotes[:5]:
    print(q.text)