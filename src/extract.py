from client import Client
import os


def create_client():
    # Creates client to get from public dataset
    # 'Contributions to Candidates and Political Committees'
    # https://dev.socrata.com/foundry/data.wa.gov/kv7h-kjye
    app_token = os.environ['app_token']
    headers = {'Accept': 'application/json',
               'X-App-token': app_token}
    url = 'https://data.wa.gov/resource/kv7h-kjye.json'
    client = Client(url, headers)
    return client


def get_contributions(client, offset):
    # Get contributions for elections year >= 2024
    # The max results per page are 1000
    params = {'$offset': offset,
              '$order': 'id',
              '$limit': '1000',
              '$where': 'election_year >= 2024'}
    return client.get(params)


def paginate_contributions():
    client = create_client()
    offset = 0
    response = get_contributions(client, offset)

    while response.json():
        print(f'Getting data with offset: {offset}')
        # TODO: put data in database
        offset += 1000
        response = get_contributions(client, offset)