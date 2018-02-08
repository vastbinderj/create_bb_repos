#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth

#
# This script will create a set of new & empty
# repositories on bitbucket. To use it, replace
# all the fields inside <>'s including the brackets
#
# Note:
# You must create client credentials on bitbucket.org
# as a prerequisite step for this script to work.
#
# You may also need to install the requests library
# > pip3 install requests


# Bitbucket API URIs
repo_endpoint = 'https://api.bitbucket.org/2.0/repositories/'
oauth_endpoint = 'https://bitbucket.org/site/oauth2/access_token'

# bitbucket API Params
# username = '<USERID'
username = '<USERID'
# bitbucket project key or UUID
# project_key = '<PROJECT_KEY>'
project_key = '<PROJECT_KEY>'
# name of file to read from
# list_of_repos = '<NAME_OF_FILE>'
list_of_repos = '<NAME_OF_FILE>'

# bitbucket client credentials
# client_key = '<CLIENT_ID>'
client_key = '<CLIENT_ID>'
# client_secret = '<CLIENT_SECRET>'
client_secret = '<CLIENT_SECRET>'


# request a bearer token
def bearer_token():
    key = client_key
    secret = client_secret
    oauth_url = oauth_endpoint
    data = {'grant_type': 'client_credentials'}

    resp = requests.post(oauth_url, auth=HTTPBasicAuth(key, secret), data=data)
    json = resp.json()
    return json['access_token']


# standard payload to create a private repo
payload = {
    "scm": "git",
    "project": {
        "key": project_key
    },
    "is_private": "true"
}


# read the repository list from a file
def read_file():
    file = open(list_of_repos, 'r')
    repo_array = file.readlines()
    return repo_array


if __name__ == "__main__":

    repo_list = read_file()

    token = bearer_token()
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    for r in repo_list:
        # format the url
        endpoint = repo_endpoint + username + '/' + r
        res = requests.post(endpoint, json=payload, headers=headers)
        print("Created " + res.json()['name'])
