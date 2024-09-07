import requests


class Client:
    def __init__(self, url, headers):
        self.url = url
        self.headers = headers

    def get(self, params=None):
        try:
            response = requests.get(
                    self.url,
                    headers=self.headers,
                    params=params)
            return response
        except Exception as e:
            print(f'An error has occurred: {e}')
