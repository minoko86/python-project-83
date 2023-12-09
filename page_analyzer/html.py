from bs4 import BeautifulSoup


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
