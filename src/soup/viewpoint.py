from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime

htmlText =requests.get('https://www.viewpointmag.com').text

source = BeautifulSoup(htmlText, 'lxml')
viewpoint = {}
viewpoint["articles"] = []

for article in source.find_all('article'):
    result ={}
    result["author"] = ", ".join([a.text.strip() for a in article.select('header > div > a')])
    result ["title"] = article.select_one('header > h2').get_text()
    result["date"] = datetime.strptime(article.select_one('header>div>time').get_text().replace(',', ""), '%B %d %Y').date()
    result["url"]= article.select_one('a').get('href')
    viewpoint["articles"].append(result)



