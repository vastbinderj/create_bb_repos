#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth


# Simple oauth example using requests module
#
# replace <KEY> and <SECRET> with your client credentials

# request a bearer token
def bearer_token():
    key = <KEY>
    secret = <SECRET>
    oauth_url = 'https://bitbucket.org/site/oauth2/access_token'
    data = {'grant_type': 'client_credentials'}

    rs = requests.post(oauth_url, auth=HTTPBasicAuth(key, secret), data=data)
    return rs.json()


if __name__ == "__main__":

    data = bearer_token()
    print(data['access_token'])
