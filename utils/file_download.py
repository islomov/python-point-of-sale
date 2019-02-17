import requests


def download_image(url, auth=None):
    try:
        response = requests.get(url, headers=dict(Authorization=auth), timeout=(1, 5))
        return response.content
    except requests.exceptions.RequestException:
        return None
