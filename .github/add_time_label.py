import sys
import json
import urllib.parse
import requests

args = sys.argv
print(args)
token = args[1]
base_url = args[2]
sum_seconds = int(float(args[3]))

if sum_seconds <= 1800:
  label = '瞬殺'
elif sum_seconds <= 10800:
  label = 'ちょっと厳しい'
else:
  label = 'だいぶかかった'

headers = {'Authorization': 'token {}'.format(token)}
api_url = base_url + '/labels/' + urllib.parse.quote('瞬殺')
requests.delete(api_url, headers=headers)
api_url = base_url + '/labels/' + urllib.parse.quote('ちょっと厳しい')
requests.delete(api_url, headers=headers)
api_url = base_url + '/labels/' + urllib.parse.quote('だいぶかかった')
requests.delete(api_url, headers=headers)

payload = {'labels': [label]}
api_url = base_url + '/labels'
r = requests.post(api_url, headers=headers, data=json.dumps(payload))
print(r)
