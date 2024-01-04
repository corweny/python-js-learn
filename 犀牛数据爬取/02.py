import json
import subprocess
from functools import partial

subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')
import chardet
import requests
import execjs

cookies = {
    'btoken': 'GPF8B4XCUR0J47W8UG0HF1MNC26K0827',
    'hy_data_2020_id': '18ccdb9724cef7-07fd41d51023bc-26031051-2073600-18ccdb9724d1bfc',
    'hy_data_2020_js_sdk': '%7B%22distinct_id%22%3A%2218ccdb9724cef7-07fd41d51023bc-26031051-2073600-18ccdb9724d1bfc%22%2C%22site_id%22%3A211%2C%22user_company%22%3A105%2C%22props%22%3A%7B%7D%2C%22device_id%22%3A%2218ccdb9724cef7-07fd41d51023bc-26031051-2073600-18ccdb9724d1bfc%22%7D',
    'sajssdk_2020_cross_new_user': '1',
    'Hm_lvt_42317524c1662a500d12d3784dbea0f8': '1704258532',
    'Hm_lpvt_42317524c1662a500d12d3784dbea0f8': '1704263608',
}

headers = {
    'authority': 'www.xiniudata.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://www.xiniudata.com',
    'referer': 'https://www.xiniudata.com/industry/newest',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 '
                  'Safari/537.36',
}
page = 20
# 分页查询，调用js加密后进行请求
with open("./02.js", 'r', encoding="utf-8") as f1:
    js_code = f1.read()
result = execjs.compile(js_code)
s = result.call('main', page)
print(s)
response = requests.post(
    'https://www.xiniudata.com/api2/service/x_service/person_industry_list/list_industries_by_sort',
    # cookies=cookies,
    headers=headers,
    json=s
)
data = response.content
data = json.loads(data)

l = data['d']
# print(l)
list_json = ''
# 开始解密字符串
try:
    with open("./03.js", 'r', encoding='utf-8') as f2:
        js_source_code = f2.read()
        # print(js_source_code)
        compiled_js = execjs.compile(js_source_code)
    list_json = compiled_js.call('decode1', l)
except Exception as e:
    print(f"An error occurred: {e}")

list_json = list_json['a']
# print(list_json)
s = json.loads(list_json)
if s['code'] != 0:
    print(s['codeMessage'])
    exit()
for item in s['list']:
    print(item['name'], item['event'])
