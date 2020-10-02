from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime


htmlText = requests.get(
    "https://roarmag.org/essays",
).text

source = BeautifulSoup(htmlText, "lxml")

main = source.select("main > section:nth-of-type(2) > div:nth-of-type(2) > div")

roar_mag={}
roar_mag["articles"] = []

for article in main[0].select('article > div'):
    result = {}
    result["title"] = article.find('h1').get_text()
    result["author"] = ", ".join(a.text.strip() for a in article.select('.articleMeta--Post > li > a'))
    result["date"] = datetime.strptime(article.select_one('ul > li:nth-of-type(2)').get_text().replace(",", ""), "%B %d %Y").date()
    result["url"] = article.find('a').get('href')
    roar_mag["articles"].append(result)
    


