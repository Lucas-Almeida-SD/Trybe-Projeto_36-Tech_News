from tech_news.database import search_news
import re
from datetime import datetime


# Requisito 6
def search_by_title(title):
    news_list = search_news(
        {"title": {"$regex": re.compile(f"{title}", re.IGNORECASE)}}
    )
    news_tuple = [(news["title"], news["url"]) for news in news_list]

    return news_tuple


# Requisito 7
def search_by_date(date):
    splited_date = date.split('-')
    year = int(splited_date[0])
    month = int(splited_date[1])
    day = int(splited_date[2])

    try:
        datetime(year, month, day)
    except ValueError:
        raise ValueError("Data inválida")

    news_list = search_news({"timestamp": '/'.join(splited_date[::-1])})
    news_tuple = [(news["title"], news["url"]) for news in news_list]

    return news_tuple


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
