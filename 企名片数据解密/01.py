import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import json

import execjs

import requests

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Origin': 'https://www.qimingpian.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'unionid': '',
}

response = requests.post('https://vipapi.qimingpian.cn/Activity/channelInformationByChannelName', headers=headers,
                         data=data)
# print(response.text)
j_res = json.loads(response.text)
# print(j_res)
data = j_res['encrypt_data']
# print(data)
with open('./01.js', 'r', encoding='utf-8') as f:
    js_content = f.read()
    JS_run = execjs.compile(js_content)
res_list = JS_run.call("s", data)
# print(res_list['list'])
for item in res_list['list']:
    print(item['news_id'], item['content'])
