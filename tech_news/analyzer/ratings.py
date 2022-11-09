from tech_news.database import search_news, find_news


def generate_news_tuple(news_list):
    return [(news["title"], news["url"]) for news in news_list]


def generate_category_by_quantity(category_list):
    category_by_quantity = dict()

    for category in category_list:
        count_category = category_list.count(category)
        if count_category in category_by_quantity:
            category_by_quantity[count_category].add(category)
        else:
            category_by_quantity[count_category] = {category}

    return category_by_quantity


# Requisito 10
def top_5_news():
    news_list = search_news(
        {"$query": {}, "$orderby": {"comments_count": -1, "title": 1}}
    )

    return generate_news_tuple(news_list[:5])


# Requisito 11
def top_5_categories():
    news_list = find_news()
    category_list = [news["category"] for news in news_list]
    category_by_quantity = generate_category_by_quantity(category_list)
    sorted_category = list()

    for element in sorted(category_by_quantity, reverse=(True)):
        sorted_category.extend(sorted(category_by_quantity[element]))

    return sorted_category
