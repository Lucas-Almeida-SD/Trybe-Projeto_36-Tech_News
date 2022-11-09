import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news


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

    news_link_list = selector.css(".entry-title a::attr(href)").getall()

    return news_link_list


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_link = selector.css(".next.page-numbers::attr(href)").get()

    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)

    url_selector = "//link[@rel='canonical']/@href"
    title_selector = "h1.entry-title::text"
    timestamp_selector = ".entry-header-inner .post-meta .meta-date::text"
    writer_selector = (
        ".entry-header-inner .post-meta .meta-author  .author a::text"
    )
    comments_count_selector = ".comment"
    summary_selector = ".cs-container .entry-content p"
    tags_selector = ".post-tags a::text"
    category_selector = ".entry-details .meta-category .label::text"

    url = selector.xpath(url_selector).get()
    title = selector.css(title_selector).get()
    timestamp = selector.css(timestamp_selector).get()
    writer = selector.css(writer_selector).get()
    comments_count = len(selector.css(comments_count_selector).getall())
    summary = selector.css(summary_selector).get()
    tags = selector.css(tags_selector).getall()
    category = selector.css(category_selector).get()

    summary_regex = r'<(?:\"[^\"]*\"["\"]*|"[^"]*"["\"]*|[^"\">])+>'

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": ''.join(re.split(summary_regex, summary)).strip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    news_list = list()
    news_links = list()
    page_url = 'https://blog.betrybe.com'

    while len(news_links) < amount:
        news_links.extend(scrape_novidades(fetch(page_url)))
        page_url = scrape_next_page_link(page_url)

    for link in news_links[: amount]:
        news = scrape_noticia(fetch(link))
        scraped_news = news
        news_list.append(scraped_news)

    create_news(news_list)
    return news_list
