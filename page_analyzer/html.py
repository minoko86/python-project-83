from bs4 import BeautifulSoup
import requests


def get_seo_data(response):
    soup = BeautifulSoup(response.text, 'html.parser')

    h1_tag = soup.find('h1')
    h1 = h1_tag.text if h1_tag else None

    title_tag = soup.title
    title = title_tag.text if title_tag else None

    description_tag = soup.find('meta', attrs={'name': 'description'})
    description = description_tag['content'] \
        if description_tag else None

    return h1, title, description


def get_response(url):
    try:
        response = requests.get(url.name)
        response.raise_for_status()
    except requests.RequestException:
        return None
    if response and response.status_code == 200:
        return response

    return None
