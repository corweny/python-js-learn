import json
import time

from curl_cffi import requests as curlreq

time_13 = time.time() * 1000
doc_id = 'caabfaa646f7ba0d4a7302768e9951e79b8969d0'
set_res = curlreq.get(
    url='https://appyd.baidu.com/nabook/chapter?fr=9&uid=&boxnovelTimeStampNow=' + str(
        time_13) + '&data={"doc_id":"' + str(doc_id) + '","fromsource":"wise"}',
    impersonate="chrome110"
)
str1 = set_res.content
str1 = json.loads(str1)
# print(str['data']['items'])
for item in str1['data']['items']:
    print(item['title'], item['cid'])
    cid = item['cid']
    # 获取文章hash
    first_url = ('https://appyd.baidu.com/nabook/content?fr=9&uid=&boxnovelTimeStampNow=1705117514597&data='
                 '{"doc_id":"') + str(doc_id) + '","cid":"' + str(cid) + '","fromsource":"wise"}'
    first_res = curlreq.get(
        url=first_url,
        impersonate="chrome110"
    )
    str2 = first_res.text
    str2 = json.loads(str2)
    print(str2['data']['items']['book_id'], str2['data']['items']['cdn_url'])
    # exit()
