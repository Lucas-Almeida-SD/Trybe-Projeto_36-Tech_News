from tech_news.database import search_news
import re
from datetime import datetime


def generate_news_tuple(news_list):
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 6
def search_by_title(title):
    news_list = search_news(
        {"title": {"$regex": re.compile(f"{title}", re.IGNORECASE)}}
    )

    return generate_news_tuple(news_list)


# Requisito 7
def search_by_date(date):
    splited_date = date.split("-")
    year = int(splited_date[0])
    month = int(splited_date[1])
    day = int(splited_date[2])

    try:
        datetime(year, month, day)
    except ValueError:
        raise ValueError("Data inválida")

    news_list = search_news({"timestamp": "/".join(splited_date[::-1])})

    return generate_news_tuple(news_list)


# Requisito 8
def search_by_tag(tag):
    news_list = search_news(
        {
            "tags": {
                "$elemMatch": {"$regex": re.compile(f"{tag}", re.IGNORECASE)}
            }
        }
    )

    return generate_news_tuple(news_list)


# Requisito 9
def search_by_category(category):
    news_list = search_news(
        {"category": {"$regex": re.compile(f"{category}", re.IGNORECASE)}}
    )

    return generate_news_tuple(news_list)
