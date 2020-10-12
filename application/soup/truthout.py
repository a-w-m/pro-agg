from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime


def get_html_text(response):
    if response.status_code == 200:
        return response.text


def get_title(article):
    return article.select_one(
        "article > div:nth-of-type(2) > div:nth-of-type(2) > h2 > a"
    ).get_text()


def get_author(article):
    return ", ".join([a.text.strip() for a in (article.select(".url.fn"))])


def get_date(article):
    return datetime.fromisoformat(
        article.select_one(".published.updated.meta-data").get("datetime")
    ).date().strftime("%m.%d.%y")


def get_url(article):
    return article.select_one(
        "article > div:nth-of-type(2) > div:nth-of-type(2) > h2 > a"
    ).get("href")


def get_article_data(source):

    result = []

    for article in source.select("article"):
        data = {}
        data["title"] = get_title(article)
        data["author"] = get_author(article)
        data["date"] = get_date(article)
        data["url"] = get_url(article)

        result.append(data)
    return result


def get_truthout(articles):
    return {"articles": articles}


response = requests.get("https://www.truthout.org/latest/")
html_text = get_html_text(response)
source = BeautifulSoup(html_text, "lxml")
articles = get_article_data(source)
truthout = get_truthout(articles)
