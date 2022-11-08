import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    time.sleep(1)

    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
        return response.text

    except requests.ReadTimeout:
        return None

    except requests.HTTPError:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)

    news_link_list = selector.css('.entry-title a::attr(href)').getall()

    return news_link_list


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
