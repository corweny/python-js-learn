import re
import time
import execjs
import requests
from bs4 import BeautifulSoup
# 获取二维码扫码登录qq音乐
qrcode_url = "https://open.weixin.qq.com/connect/qrconnect?appid=wx48db31d50e334801&redirect_uri=https%3A%2F%2Fy.qq.com%2Fportal%2Fwx_redirect.html%3Flogin_type%3D2%26surl%3Dhttps%3A%2F%2Fy.qq.com%2Fn%2Fryqq%2Fsearch%3Fw%3D%25E4%25BA%25BA%25E5%2595%258A&response_type=code&scope=snsapi_login&state=STATE&href=https%3A%2F%2Fy.qq.com%2Fmediastyle%2Fmusic_v17%2Fsrc%2Fcss%2Fpopup_wechat.css%23wechat_redirect"
qr = requests.get(url=qrcode_url)
html = BeautifulSoup(qr.content, 'html.parser')
print(html.find('img').get('src'))
uuid = html.find('img').get('src')[16:]
qrcode_img = 'https://open.weixin.qq.com' + html.find('img').get('src')
# 下载图片并保存到本地
response = requests.get(qrcode_img)
with open('qr_img.jpg', 'wb') as handler:
    handler.write(response.content)
print(uuid)
print("请手动打开目录下的图片文件，微信扫码...")
# window.wx_errcode=408;window.wx_code=''; 等待扫码
# window.wx_errcode=404;window.wx_code=''; 被扫码
# window.wx_errcode=405;window.wx_code='061lQlGa1nXiHG06VNFa1ybVm93lQlGG'; 扫码后
while True:
    time13 = round(time.time() * 1000)
    res = requests.get(f"https://lp.open.weixin.qq.com/connect/l/qrconnect?uuid={uuid}&last=404&_={time13}")
    print(res.text)
    time.sleep(1)
    pattern = r'\b{}\b'.format('405')

    if bool(re.search(pattern, res.text)):
        match = re.search(r"'([^']*)'", res.text)
        w_code = match.group(1)
        break
print("扫码成功，获取cookie,code=", w_code)
# 扫码成功后获取cookie
cookies = {
    'pgv_pvid': '4362410014',
    'fqm_pvqid': 'fcd79242-9778-4aee-a09d-95f4bc46cdc4',
    'fqm_sessionid': '4efc9949-569d-4cac-8462-d9fc0aa06dcb',
    'pgv_info': 'ssid=s712078452',
    'ts_last': 'y.qq.com/n/ryqq/search',
    'ts_uid': '4942556020',
    '_qpsvr_localtk': '0.9539757217742997',
}

headers = {
    'authority': 'u.y.qq.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

data = '{"comm":{"tmeAppID":"qqmusic","tmeLoginType":"1","g_tk":5381,"platform":"yqq","ct":24,"cv":0},"req":{"module":"music.login.LoginServer","method":"Login","param":{"strAppid":"wx48db31d50e334801","code":"' + w_code + '"}}}'

response = requests.post('https://u.y.qq.com/cgi-bin/musicu.fcg', cookies=cookies, headers=headers, data=data)

# print(response.cookies)
cookies = requests.utils.dict_from_cookiejar(response.cookies)
headers = {
    'authority': 'u.y.qq.com',
    'accept': 'application/json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    'dnt': '1',
    'origin': 'https://y.qq.com',
    'referer': 'https://y.qq.com/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}
while True:
    time_13 = round(time.time() * 1000)
    query = input("请输入想查询的歌曲：")

    with open('./02.js', 'r', encoding='utf-8') as f:
        js_run = execjs.compile(f.read())
    data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":"1152921504857790218","g_tk_new_20200303":651551008,"g_tk":651551008,"mesh_devops":"DevopsBase"},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"71879864032731085","search_type":0,"query":"' + query + '","page_num":1,"num_per_page":10}}}'
    sign = js_run.call("main", data)
    params = {
        '_': time_13,
        'sign': sign,
    }
    response = requests.post('https://u.y.qq.com/cgi-bin/musics.fcg', params=params, cookies=cookies, headers=headers,
                             data=data.encode()).json()
    print(response)
