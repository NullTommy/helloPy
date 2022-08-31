# -*- coding: utf-8 -*
import json
import requests

d = {'apiUrl': 'https://api.muxiaoguo.cn/api/caihongpi?api_key=53e87ca7e48f35d9',
     'msgText': '【今日彩虹屁】',
     'msgSendUrl': 'https://open.feishu.cn/open-apis/bot/v2/hook/37ae5398-f44c-4c4a-b4fa-39e701e7ccd3'}

caiHongRes = requests.get(url=d['apiUrl'])
caiHongdata = json.loads(caiHongRes.text,encoding='bytes')
caiHongtext = caiHongdata['data']['comment']
d['msgText'] = d['msgText']+caiHongtext.encode('utf-8')
print(d['msgText'])
t = {
    'msg_type': "text",
    'content': {
        'text': d['msgText'],
    },
};
x = requests.post(d['msgSendUrl'], json=t)
print(x.text)
