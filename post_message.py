# -*- coding: utf-8 -*-
import os
import json
import requests
import datetime

WEBHOOK_URL = os.environ['WEBHOOK_URL']
TIMES_MONEYFOREST_URL = os.environ['TIMES_MONEYFOREST_URL']
MFX_DEV_URL = os.environ['MFX_DEV_URL']

def post_message():
    url = WEBHOOK_URL + MFX_DEV_URL
    assignee = assignor()
    sentence = make_sentence(assignee)
    requests.post(url, data=json.dumps({ "text": sentence }))

def assignor():
    with open('rotation.json', 'r') as f:
        assignee = json.load(f)[weekday()]
        return assignee

def make_sentence(assignee):
    sentence = '今日は ' + assignee + ' Trello見てね!'
    return sentence

def weekday():
    weekday = datetime.date.today().weekday()
    return str(weekday)

if __name__ == '__main__':
    post_message()
