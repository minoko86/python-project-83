import requests


def get_response(url):
    try:
        response = requests.get(url.name)
        response.raise_for_status()
    except requests.RequestException:
        return None
    if response and response.status_code == 200:
        return response

    return None
