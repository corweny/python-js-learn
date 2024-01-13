import requests

import execjs

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'EUI': 'TUVtkYbr9x/M4tFjxbcdNZKrXyFub1qB/iUySsjhcB3eIxLyFh1i8P2LL2JXF41TgCiMvGA/z6shtSU7wnopt51C3FfW6eGhsiDOUKDWHoNYOPaLBumB0lo9pbqWM/ESnVoC4uiBpusPK2+GeVWE34/tbHxATf7UEOYCfhKLgX0=.dXNlcg==',
    'Origin': 'https://account.xiaomi.com',
    'Referer': 'https://account.xiaomi.com/fe/service/login/password?_qrsize=180&sid=mi_eshop&qs=%253Fcallback%253Dhttp%25253A%25252F%25252Forder.mi.com%25252Flogin%25252Fcallback%25253Ffollowup%25253Dhttps%2525253A%2525252F%2525252Fwww.mi.com%2525252F%252526sign%25253DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%25252C%25252C%2526sid%253Dmi_eshop%2526_qrsize%253D180&callback=http%3A%2F%2Forder.mi.com%2Flogin%2Fcallback%3Ffollowup%3Dhttps%253A%252F%252Fwww.mi.com%252F%26sign%3DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%2C%2C&_sign=w1RBM6cG8q2xj5JzBPPa65QKs9w%3D&serviceParam=%7B%22checkSafePhone%22%3Afalse%2C%22checkSafeAddress%22%3Afalse%2C%22lsrp_score%22%3A0.0%7D&showActiveX=false&theme=&needTheme=false&bizDeviceType=&_locale=zh_CN',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

user_name = input("请输入用户名或者手机号码：")
password = input("请输入密码：")
# user: 3bHvPRPUgoPr72bccbYs0g==
# password 没找到
# _sign: 不清楚是什么
# hash=k()(c.password).toUpperCase()

with open('./01.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    js_run = execjs.compile(js_code)
res = js_run.call('main', user_name, password)
print(res)
data = {
    'bizDeviceType': '',
    'needTheme': 'false',
    'theme': '',
    'showActiveX': 'false',
    'serviceParam': '{"checkSafePhone":false,"checkSafeAddress":false,"lsrp_score":0.0}',
    'callback': 'http://order.mi.com/login/callback?followup=https%3A%2F%2Fwww.mi.com%2F&sign=NzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw,,',
    'qs': '%3Fcallback%3Dhttp%253A%252F%252Forder.mi.com%252Flogin%252Fcallback%253Ffollowup%253Dhttps%25253A%25252F%25252Fwww.mi.com%25252F%2526sign%253DNzY3MDk1YzczNmUwMGM4ODAxOWE0NjRiNTU5ZGQyMzFhYjFmOGU0Nw%252C%252C%26sid%3Dmi_eshop%26_qrsize%3D180',
    'sid': 'mi_eshop',
    '_sign': 'w1RBM6cG8q2xj5JzBPPa65QKs9w=',
    'user': user_name,
    'cc': '+86',
    'hash': res[1].upper(),
    '_json': 'true',
    'policyName': 'miaccount',
    'captCode': '',
}

response = requests.post('https://account.xiaomi.com/pass/serviceLoginAuth2', headers=headers, data=data)
print(response.text)
