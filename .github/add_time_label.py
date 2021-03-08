import sys
import json
import requests

args = sys.argv
token = args[1]
sum_seconds = int(args[2])

if sum_seconds <= 1800:
  label = '瞬殺'
elif sum_seconds <= 10800:
  label = 'ちょっと厳しい'
else:
  label = 'だいぶかかった'

with open(environ.get('GITHUB_EVENT_PATH')) as f:
  events = json.load(f)
  headers = {'Authorization': 'token {}'.format(token)}
  payload = {'labels': [label]}
  api_url = events['issue']['url'] + '/labels'
  r = requests.post(api_url, headers=headers, data=json.dumps(payload))
  print(r)
