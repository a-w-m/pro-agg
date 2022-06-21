from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime


def create_headers():
    return {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"
    }

def is_request_successful(response):
    if response.status_code == 200:
        return True
    else:
        return False


def get_html_text(response):
    if response.status_code == 200:
        return response.text


def get_title(article):
    return article.select_one("h3").string


def get_author(article):
    return article.select_one("article > a").string
    # return ", ".join(a.text.strip() for a in article.select(".name"))


def get_date(article):
    # return article.select("div:nth-of-type(1) > div:nth-of-type(2)")
    return (
        datetime.strptime(article.select_one("div:nth-of-type(1) > div:nth-of-type(2)").get_text(), "%B %d, %Y")
        .strftime("%m.%d.%y")
    )


def get_url(article):
    return article.select_one("h3 > a").get("href")

def get_author_url(article):
    return article.select_one("article > a").get("href")


def get_article_data(source):

    result = []
    for article in zip(range(4), source.select("main > div > div:nth-of-type(2) > article")):

        data = {}


        data["title"] = get_title(article[1])
        data["author"] = get_author(article[1])
        data["author_url"] = get_author_url(article[1])
        data["url"] = get_url(article[1])
        data["date"] = get_date(article[1])





        result.append(data)

    return result


def get_baffler(articles):
    return {"articles": articles}

def run_baffler():
    response = requests.get("https://thebaffler.com/latest", headers=create_headers())
    if (is_request_successful(response)):
        html_text = get_html_text(response)
        source = BeautifulSoup(html_text, "lxml")
        articles = get_article_data(source)
        return get_baffler(articles)

if __name__ == '__main__':
    print(run_baffler())
 
