import os, json, random, requests, datetime, csv, shutil

WEBHOOK_URL = os.environ['WEBHOOK_URL']
DEVELOPMENT_CHANNEL_URL = os.environ['DEVELOPMENT_CHANNEL_URL']
PRODUCTION_CHANNEL_URL = os.environ['PRODUCTION_CHANNEL_URL']
ENVIRONMENT = os.environ['ENVIRONMENT']

def post_message():

    if not os.path.isfile("/tmp/rinban.csv"):
        shutil.copyfile("./rinban.csv", "/tmp/rinban.csv")

    sentence = make_sentence(assign())
    requests.post(make_url(), data=json.dumps({ "text": sentence }))
    next_assign()

def assign():
    with open('rotation.json', 'r') as f:
        return json.load(f)[assign_number()]

def assign_number():
    lastrow = sum(1 for i in open('/tmp/rinban.csv'))
    with open('/tmp/rinban.csv') as f:
        l = [row for row in csv.reader(f)]
        return l[lastrow - 1][0]

def next_assign():
    with open('/tmp/rinban.csv', 'a', newline="") as f:
       csv.writer(f).writerow([get_next_assign_number()])

def get_next_assign_number():
    MAX_MEMBER = '4'
    if assign_number() == MAX_MEMBER:
        return '1'
    else:
        return str(int(assign_number()) + 1)

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

if __name__ == '__main__':
    post_message()
