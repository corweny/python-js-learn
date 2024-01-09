import time
import execjs
import requests


def first_get_cookie():
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Pragma': 'no-cache',
        'Referer': 'https://xueqiu.com/today',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://xueqiu.com/', headers=headers)
    return response.cookies


def sec_get_run_js():
    with open("./02.js", 'r', encoding='utf-8') as f:
        js_code = f.read()
        js_run = execjs.compile(js_code)
    return js_run.call('get_v2')


cookie = first_get_cookie()
acw_sc__v2 = sec_get_run_js()
cookie.set("acw_sc__v2", acw_sc__v2)
cookies = cookie.get_dict()
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'DNT': '1',
    'Referer': 'https://xueqiu.com/today',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'elastic-apm-traceparent': '00-ad35f3fe5522aadc23cf9ace79a03037-f71b6c9f9be0cb78-01',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'since_id': '-1',
    'max_id': '580608',
    'size': '15',
}

response = requests.get('https://xueqiu.com/statuses/hot/listV2.json', params=params, cookies=cookies,
                        headers=headers).json()
# print(response)
for item in response['items']:
    print('标题：' + item['original_status']['description'], '作者：' + item['original_status']['user']['screen_name'])
