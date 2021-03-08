import sys
import requests

args = sys.argv
token = args[1]
api_url = args[2] + '/labels'
sum_seconds = int(args[3])

if sum_seconds <= 1800:
  label = '瞬殺'
elif sum_seconds <= 10800:
  label = 'ちょっと厳しい'
else:
  label = 'だいぶかかった'

headers = {'Authorization': 'token {}'.format(token)}
payload = {'labels': [label]}
r = requests.post(api_url, headers=headers, data=json.dumps(payload))
print(r)
