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


class ContributionsClient():
    def __init__(self, url, headers):
        self.client = Client(url, headers)

    def get_contributions(self, offset, step):
        # Get contributions for elections year >= 2024
        # The max results per page are 1000
        params = {'$offset': offset,
                  '$order': 'id',
                  '$limit': step,
                  '$where': 'election_year >= 2024'}
        return self.client.get(params)

    def paginate_contributions(self, func, step):
        # Takes in a function to execute with response and a step
        # to paginate results
        offset = 0
        response = self.get_contributions(offset, step)

        while response.json():
            func(response.json())
            offset += step
            response = self.get_contributions(offset, step)
