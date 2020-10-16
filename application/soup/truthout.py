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
    return article.select_one(
        "article > div:nth-of-type(2) > div:nth-of-type(2) > h2 > a"
    ).get_text()


def get_author(article):
    return ", ".join([a.text.strip() for a in (article.select(".url.fn"))])


def get_date(article):
    return (
        datetime.fromisoformat(
            article.select_one(".published.updated.meta-data").get("datetime")
        )
        .date()
        .strftime("%m.%d.%y")
    )


def get_url(article):
    return article.select_one(
        "article > div:nth-of-type(2) > div:nth-of-type(2) > h2 > a"
    ).get("href")


def get_author_url(article):
    return article.select_one(".url.fn").get("href")


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


def get_truthout(articles):
    return {"articles": articles}


def run_truthout():
    response = requests.get("https://www.truthout.org/latest/")
    if is_request_successful(response):
        html_text = get_html_text(response)
        source = BeautifulSoup(html_text, "lxml")
        articles = get_article_data(source)
        return get_truthout(articles)


if __name__ == "__main__":

    print(run_truthout())