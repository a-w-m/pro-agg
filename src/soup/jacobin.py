from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime

# get html 

htmlText = requests.get("https://www.jacobinmag.com").text

# pass the html to BeautifulSoup

source = BeautifulSoup(htmlText, 'lxml') 

main = source.select('main > section:nth-of-type(2) > div')

jacobin = {}
jacobin["articles"] = []

for article in main[0].find_all('article'):
     result = {}
     
     result["title"] = article.find('a', class_= "hm-dg__link").get_text().strip()
     result["author"]= ", ".join([a.text.strip() for a in (article.find_all('a', class_= "hm-dg__author-link"))]) 
     result["date"] = datetime.strptime(article.find('time').get('datetime'), '%Y-%m-%d %H:%M:%S').date()
     result["url"] = "https://jacobinmag.com" + article.find('a', class_= "hm-dg__link").get('href')
     jacobin["articles"].append(result)

