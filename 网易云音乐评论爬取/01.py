import execjs
import requests
import json

headers = {
    'authority': 'music.163.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'NMTID=00Oj5kEwdkTtzNV30bQuxQpNsQAOZ0AAAGM8cA3_A; JSESSIONID-WYYY=NWoPtUvQYdRQfN2Qjx2QyGO2imTSk1WzGg6tPaJ1Z90%2Fj0YQSgXEAJk%2Bl%5C%5CfiCHdWMbH9FbQ%2B9vM1HbxisR07uKmaOyouf%2Ft9AlsGPcFi0%2BmkTJxss%5CsAhdNSJMM43pxbei6uzPDI1QNu1RCYJpSC4vJOhFSstMAsNH2T%5C5gdjUUuQcQ%3A1704864755498; _iuqxldmzr_=32; _ntes_nnid=b636563aa9bbda1d9844baa4f04aa788,1704862955513; _ntes_nuid=b636563aa9bbda1d9844baa4f04aa788; WEVNSM=1.0.0; WNMCID=znwgut.1704862956482.01.0; WM_NI=XkHI7n79wIdVlXxD3iLsREScXFrUSG%2FwQ3but6B1z3C8ieS6z9FXBbm69gabB2e2RqkrLF9sosAdxTv2YqQDOq%2BkwAG1sL4KU07zD8DjtIHj4XDTSGJjrxhvzZP34u6ZMUM%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8acd6ab5a78fa9d580a2ef8ab2c55e979a9b82c434a6ac9c94d85e90ed8ad5b72af0fea7c3b92a9cb588aab666f5e7b9aae75eb088b8a5b26390ad9ea6d2699c9abeb6d24deda99fd4e17fb8ea8ed2f93981e8a786d23ebae78ab9c16aafeaf788e46a82eeabd3d17ba9ae84a7bc79adad8f85fb60b6ee9792d4508dafe58cf64b85efbdadb74197f0f99bc73488b6bcaacb62f8888cb5d24d8ab6be99eb7eba86a0d4b77ff68683b6d037e2a3; WM_TID=6TWo7x8pHzBFUUQUBVLU9OoH4EBbyUst; sDeviceId=YD-YLYQ8cGBuRBAAwQUAVfE4foH8RF1VKzo; ntes_utid=tid._.T70ZkabkkidABlBFRUfRte5ToUV1VTsi._.0; __snaker__id=D0E5m5PJWVj2gEUQ; gdxidpyhxdE=mj3RQY896CBTP3%2BVELwP20EkfbvIbx2cc2JjGd7ZyxLHjgPtL91tjBfauCuGyWHVe1gpv%2BHlAKl7GOlbwVA7tK72%2FhG0VN0aUa7EX4Dix2JypG5NItTrIlUp3iWiP0wBvyXB48WsU2HcBQ7Wm3Y%2FqDmuNSAI0a2jrkDirONePJio%2FBcq%3A1704863878241',
    'dnt': '1',
    'nm-gcore-status': '1',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/song?id=436514312',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}

params = {
    'csrf_token': '',
}
while True:
    sid = input("请输入音乐id,链接最后面的一串数字就是：")
    with open("./01.js", 'r', encoding="utf-8") as f:
        js_code = f.read()
        JS_run = execjs.compile(js_code)
    data = JS_run.call('getCommentList', sid)
    # print(data)

    response = requests.post(
        'https://music.163.com/weapi/comment/resource/comments/get',
        params=params,
        headers=headers,
        data=data,
    )
    res = json.loads(response.text)
    for item in res['data']['hotComments']:
        print(item['user']['nickname'], item['timeStr']+':')
        print(item['content'], '\n'+str(item['likedCount'])+"人喜欢"+'\n====================================================')
