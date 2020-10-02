from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"}
htmlText = requests.get("https://thebaffler.com/latest", headers=headers).text

source = BeautifulSoup(htmlText, "lxml")

baffler = {}
baffler["articles"] = []

for index, article in zip(range(4), source.select('article')):
    result = {}

    result["title"] = article.select_one('.hed').get_text()
    result["author"] = ", ".join(a.text.strip() for a in article.select('.name'))
    result["date"]= datetime.strptime(article.select_one('.date').get_text(), '%B %d').replace(year=datetime.now().year).date()
    result["url"] = article.select_one('.hed > a').get('href')

    baffler["articles"].append(result)

