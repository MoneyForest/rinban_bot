import os
import json
import requests
import datetime

WEBHOOK_URL = os.environ['WEBHOOK_URL']
DEVELOPMENT_CHANNEL_URL = os.environ['DEVELOPMENT_CHANNEL_URL']
PRODUCTION_CHANNEL_URL = os.environ['PRODUCTION_CHANNEL_URL']
ENVIRONMENT = os.environ['ENVIRONMENT']

def post_message():
    assignee = assignor()
    sentence = make_sentence(assignee)
    requests.post(make_url(), data=json.dumps({ "text": sentence }))

def assignor():
    with open('rotation.json', 'r') as f:
        assignee = json.load(f)[weekday()]
        return assignee

def make_sentence(assignee):
    sentence = '今日は ' + assignee + ' Trello見てね！ :pray:'
    return sentence

def make_url():
    url = ''
    if ENVIRONMENT == 'DEVELOPMENT':
        url = WEBHOOK_URL + DEVELOPMENT_CHANNEL_URL
    elif ENVIRONMENT == 'PRODUCTION':
        url = WEBHOOK_URL + PRODUCTION_CHANNEL_URL
    return url


def weekday():
    weekday = datetime.date.today().weekday()
    return str(weekday)

if __name__ == '__main__':
    post_message()
