import requests
from bs4 import BeautifulSoup
from bs4.element import Comment
import urllib.request


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def is_video_element(element):
    return element.name == 'iframe' or element.name == 'video' or element.name == 'object' or element.name == 'embed'


def text_from_html(body):
    soup = BeautifulSoup(body, 'html.parser')
    # Assuming the article is contained within an <article> tag
    article = soup.find('article')
    if article:
        for video in article.find_all(is_video_element):
            video.extract()  # Remove video elements from the article
        texts = article.findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)
    return ''  # Return an empty string if no article is found


def get_body_text_from_urls(url_list):
    body_text_list = []
    for url in url_list:
        try:
            html = urllib.request.urlopen(url).read()
            body_text = text_from_html(html)
            body_text_list.append(body_text)
        except Exception as e:
            print(f"Error fetching content from {url}: {e}")
            body_text_list.append('')  # Append an empty string on error
    return body_text_list


# List of URLs to scrape
url_list = [
    'https://www.theguardian.com/world/2023/oct/13/why-israel-palestine-conflict-history',
    # Add another example URL
    'https://www.cnn.com/middleeast/live-news/israel-news-hamas-war-10-15-23/index.html',
]

body_text_list = get_body_text_from_urls(url_list)

for i, body_text in enumerate(body_text_list):
    print(f"Body Text for URL {i + 1}:\n{body_text}\n")
