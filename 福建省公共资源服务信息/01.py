import json
import time
from datetime import datetime
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import execjs
import requests

cookies = {
    'ASP.NET_SessionId': 'xewkqh3ex2dd5dk0hnqaz0b0',
}
with open("./01.js", 'r', encoding='utf-8') as f:
    js_data = f.read()
    JS_run = execjs.compile(js_data)
# 获取当前时间的时间戳
timestamp = datetime.now().timestamp()

# 将时间戳转换为13位格式
timestamp_13 = int(timestamp * 1000)
# print(timestamp_13)
json_data = {
    "ts": timestamp_13,
    "pageSize": 20,
    "AREACODE": "",
    "M_PROJECT_TYPE": "",
    "KIND": "GCJS",
    "GGTYPE": "",
    "PROTYPE": "",
    "timeType": "6",
    "BeginTime": "2023-07-05 00:00:00",
    "EndTime": "2024-01-05 23:59:59"
}
portalSign = JS_run.call("d", json_data)
print(portalSign)
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    # 'Cookie': 'ASP.NET_SessionId=xewkqh3ex2dd5dk0hnqaz0b0',
    'DNT': '1',
    'Origin': 'https://ggzyfw.fj.gov.cn',
    'Referer': 'https://ggzyfw.fj.gov.cn/business/list/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'portal-sign': portalSign,
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
response = requests.post('https://ggzyfw.fj.gov.cn/FwPortalApi/Trade/TradeInfo', cookies=cookies, headers=headers,
                         json=json_data)
resp = json.loads(response.text)
t = resp['Data']
if t is not None:
    a_list = JS_run.call("b", t)
    j_list = json.loads(a_list)
    print(j_list['Table'])
    for item in j_list['Table']:
        print(item)
else:
    print(resp)
