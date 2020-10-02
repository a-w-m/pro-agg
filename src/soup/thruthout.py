from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime

htmltext = requests.get('https://www.truthout.org/latest/').text

source = BeautifulSoup(htmltext, 'lxml')

truthout = {}
truthout["articles"] = []

for article in source.select('article'):
    result = {}
    result["title"] = article.select_one('article > div:nth-of-type(2) > div:nth-of-type(2) > h2 > a').get_text()
    result["author"] = ", ".join([a.text.strip() for a in (article.select('.url.fn'))])
    result["date"] = datetime.fromisoformat(article.select_one('.published.updated.meta-data').get('datetime')).date()
    result["url"] = article.select_one('article > div:nth-of-type(2) > div:nth-of-type(2) > h2 > a').get('href')
    
    truthout["articles"].append(result)
    
    
