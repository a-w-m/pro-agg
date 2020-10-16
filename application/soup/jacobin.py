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
    return article.find("a", class_="hm-dg__link").get_text().strip()


def get_author(article):
    return ", ".join(
        [a.text.strip() for a in (article.find_all("a", class_="hm-dg__author-link"))]
    )


def get_date(article):
    return datetime.strptime(
        article.find("time").get("datetime"), "%Y-%m-%d %H:%M:%S"
    ).date().strftime("%m.%d.%y")


def get_url(article):
    return "https://jacobinmag.com" + article.find("a", class_="hm-dg__link").get(
        "href"
    )

def get_author_url(article):
    return "https://jacobinmag.com" + article.find("a", class_="hm-dg__author-link").get('href')


def get_article_data(source):
    result = []
    for article in source.find_all("article"):
        data = {}

        data["title"] = get_title(article)
        data["author"] = get_author(article)
        data["date"] = get_date(article)
        data["url"] = get_url(article)
        data["author_url"] = get_author_url(article)

        result.append(data)
    return result


def get_jacobin(articles):

    return {"articles": articles}

def run_jacobin():
        response = requests.get("https://www.jacobinmag.com")
        if(is_request_successful(response)):
            html_text = get_html_text(response)
            source = BeautifulSoup(html_text, "lxml").select_one(".hm-sd-b__container")
            articles = get_article_data(source)
            return get_jacobin(articles)


if __name__ == '__main__':
    print(run_jacobin())


