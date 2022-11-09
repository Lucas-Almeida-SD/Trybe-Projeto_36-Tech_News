from tech_news.database import search_news
import re


# Requisito 6
def search_by_title(title):
    news_list = search_news(
        {"title": {"$regex": re.compile(f"{title}", re.IGNORECASE)}}
    )
    news_tuple = [(news["title"], news["url"]) for news in news_list]

    return news_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
