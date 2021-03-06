from bs4 import BeautifulSoup
import requests
import lxml
from datetime import datetime

def is_request_successful(response):
    if response.status_code == 200:
        return True
    else:
        return False

def get_html_text(response):
    if response.status_code == 200:
        return response.text


def get_title(article):
    return article.find("h1").get_text()


def get_author(article):
    return ", ".join(
        a.text.strip() for a in article.select(".articleMeta--Post > li > a")
    )


def get_date(article):
    return datetime.strptime(
        article.select_one("ul > li:nth-of-type(2)").get_text().replace(",", ""),
        "%B %d %Y",
    ).date().strftime("%m.%d.%y")


def get_url(article):
    return article.find("a").get("href")

def get_author_url(article):
    return article.select_one(".articleMeta--Post > li > a").get("href")


def get_article_data(source):

    result = []
    for article in source.select("article > div"):
        data = {}

        data["title"] = get_title(article)
        data["author"] = get_author(article)
        data["author_url"] = get_author_url(article)
        data["date"] = get_date(article)
        data["url"] = get_url(article)

        result.append(data)

    return result


def get_roar(articles):
    return {"articles": articles}

def run_roarmag():
    response = requests.get("https://roarmag.org/essays")
    if(is_request_successful(response)):
        html_text = get_html_text(response)
        source = BeautifulSoup(html_text, "lxml").select(
            "main > section:nth-of-type(2) > div:nth-of-type(2) > div"
        )[0]
        articles = get_article_data(source)
        return get_roar(articles)

if __name__ == '__main__':
    print(run_roarmag())


    
