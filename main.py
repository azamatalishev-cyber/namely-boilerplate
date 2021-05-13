import requests
from datetime import timedelta, date
from time import sleep
import subprocess
from urllib.parse import urljoin
from pprint import pprint


class Namely:

    def __init__(self, token):
        self.session = requests.Session()
        self.base_url = 'https://company.namely.com/api/v1'
        self.auth_token = token

    def send_api(self, method, endpoint, **kwargs):
        url = '{}{}'.format(self.base_url, endpoint)
        request = requests.Request(method,
                                   url,
                                   headers=self.get_headers(),
                                   **kwargs)
        prepped = request.prepare()
        response = self.session.send(prepped)
        response.raise_for_status()
        return response

    def get_headers(self):
        return {
            'Accept': 'application/json',
            'Authorization': 'Bearer {}'.format(self.auth_token)
        }


def main():
    # This is an example below that spits out the a json of the first 30 user profiles.
    # To get all you will need to paginate through.  
    # Adjust how you pass secrets to Namely object, this is obviously not the most secure way.
    drive = Namely(
        'Token here')
    response = drive.send_api('GET', '/profiles')
    pprint(response.json())
