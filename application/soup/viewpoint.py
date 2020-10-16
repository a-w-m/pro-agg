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
        return response.text



def get_title(article):
    return article.select_one("header > h2").get_text()


def get_author(article):
    return ", ".join([a.text.strip() for a in article.select("header > div > a")])


def get_date(article):
    return datetime.strptime(
        article.select_one("header>div>time").get_text().replace(",", ""), "%B %d %Y"
    ).date().strftime("%m.%d.%y")


def get_url(article):
    return article.select_one("a").get("href")

def get_author_url(article):
    return article.select_one("header > div > a").get("href")


def get_article_data(source):

    result = []

    for article in source.select("article"):
        data = {}
        data["title"] = get_title(article)
        data["author"] = get_author(article)
        data["author_url"] = get_author_url(article)
        data["date"] = get_date(article)
        data["url"] = get_url(article)

        result.append(data)

    return result


def get_viewpoint(articles):
    return {"articles": articles}

def run_viewpoint():
    response = requests.get("https://www.viewpointmag.com", headers = create_headers())
    if is_request_successful(response):
        html_text = get_html_text(response)
        source = BeautifulSoup(html_text, "lxml")
        articles = get_article_data(source)
        return get_viewpoint(articles)
        


if __name__ == '__main__':
    print(run_viewpoint())
