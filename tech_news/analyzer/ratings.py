from tech_news.database import search_news


def generate_news_tuple(news_list):
    return [(news["title"], news["url"]) for news in news_list]


# Requisito 10
def top_5_news():
    news_list = search_news({"$query": {}, "$orderby": {
        "comments_count": -1, "title": 1
    }})

    return generate_news_tuple(news_list[:5])


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
