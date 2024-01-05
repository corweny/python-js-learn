import json
import execjs
import requests

cookies = {
    'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1704358337',
    'MALLSSID': '34486B6D614B6B4A424A4436387A5357446E4D706A6D576C5537765232344B637154526A2B6938532F3065692B484A70495A56656B4E6775784F555766386854',
    'Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b': '1704360532',
}
runtime = execjs.get()
with open("./01.js",'r',encoding='utf-8')as f:
    py_content = f.read()
    js = runtime.compile(py_content)
# 在这个运行环境中执行 JavaScript 代码

Token =js.call("getResCode")
headers = {
    'Accept': '*/*',
    'Accept-EncKey': Token,
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1704358337; MALLSSID=34486B6D614B6B4A424A4436387A5357446E4D706A6D576C5537765232344B637154526A2B6938532F3065692B484A70495A56656B4E6775784F555766386854; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1704360532',
    'DNT': '1',
    'Origin': 'https://webapi.cninfo.com.cn',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
url = "https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007"
data = {
    'tdate': '2024-01-03',
    'market': 'SZE',
}

response = requests.post(url, cookies=cookies, headers=headers, data=data)
res = json.loads(response.content)
print(res)
