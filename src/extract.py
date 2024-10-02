from client import ContributionsClient
import os


def do_something(data):
    print(data)


def get_data():
    # https://dev.socrata.com/foundry/data.wa.gov/kv7h-kjye
    # The max results per page are 1000
    app_token = os.environ['app_token']
    headers = {'Accept': 'application/json',
               'X-App-token': app_token}
    url = 'https://data.wa.gov/resource/kv7h-kjye.json'
    client = ContributionsClient(url, headers)
    client.paginate_contributions(do_something, 1000)
