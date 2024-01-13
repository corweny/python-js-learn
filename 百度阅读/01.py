import execjs
import requests
headers = {
    'authority': 'novel-content-new.cdn.bcebos.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'dnt': '1',
    'origin': 'https://boxnovel.baidu.com',
    'referer': 'https://boxnovel.baidu.com/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
}

params = {
    'md5hash': '34aa600842a4e42eb6c8beac9c72116b',
    'timestamp': '1705050980',
}
response = requests.get('https://novel-content-new.cdn.bcebos.com/6742163404127555724', params=params, headers=headers)
a = response.text
# print(bin(bytes(bytearray(a,"utf-8"))))
# print(bin(bytes(bytearray("Hello, world!", "utf-8"))))
byte_array = bytearray(a, "utf-8")
binary_string = ""
for byte in byte_array:
    binary_string += format(byte, "08b")  # 将每个字节转换为 8 位二进制并拼接
# print(binary_string)
with open('./01.js', 'r', encoding='utf-8') as f:
    js_code = f.read()
    JS_run = execjs.compile(js_code)
# print(binary_string)
res = JS_run.call("main", binary_string)

print(res)
