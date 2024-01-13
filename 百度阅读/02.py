import base64
import json
import time
from curl_cffi import requests as curlreq
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

import requests

# ASCII字符到Base64索引的映射，用于编码过程
_BASE64_ALPHABET = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
_BASE64_INDEX = {val: idx for idx, val in enumerate(_BASE64_ALPHABET)}


def custom_b64encode(data):
    """
    自定义的Base64编码函数，与JavaScript版本的 encode 功能相同。
    """
    enc = []

    for i in range(0, len(data), 3):
        triple = data[i:i + 3]
        b = bytearray(triple)

        enc.append(_BASE64_ALPHABET[b[0] >> 2])
        enc.append(_BASE64_ALPHABET[((b[0] & 0x03) << 4) | (b[1] >> 4 if len(b) > 1 else 0)])
        enc.append(_BASE64_ALPHABET[((b[1] & 0x0F) << 2) | (b[2] >> 6 if len(b) > 2 else 0)])
        enc.append(_BASE64_ALPHABET[(b[2] & 0x3F) if len(b) > 2 else 64])

    result = bytes(enc)
    # 修正结尾的'='（padding）根据实际编码长度
    if len(data) % 3 == 1:
        result = result[:-2] + b'=='
    elif len(data) % 3 == 2:
        result = result[:-1] + b'='

    return result.decode()


def aes_decrypt(encrypted_data, key, iv):
    """
    AES解密函数，使用Crypto库的AES算法实现。
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 假定在JavaScript代码中Crypto.AES.decrypt使用了相同模式的Padding
    plaintext = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    return plaintext.decode('utf-8')


def getDetail(url):
    # 发送请求获取二进制数据
    response = requests.get(url)
    response.raise_for_status()  # 确保请求成功

    # 解密请求得到的数据
    key = b'D0CD8B760CE07BC3'
    iv = b'2011121211143000'
    decrypted_data = aes_decrypt(response.content, key, iv)

    # HTML字符过滤
    sanitized_data = decrypted_data.replace('<', '&lt;').replace('>', '&gt;')

    return sanitized_data


def getList(doc_id):
    time_13 = time.time() * 1000
    set_res = curlreq.get(
        url='https://appyd.baidu.com/nabook/chapter?fr=9&uid=&boxnovelTimeStampNow=' + str(
            time_13) + '&data={"doc_id":"' + str(doc_id) + '","fromsource":"wise"}',
        impersonate="chrome110"
    )
    str1 = set_res.content
    str1 = json.loads(str1)
    # print(str['data']['items'])
    dic_url = []
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
        # print(str2['data']['items']['book_id'], str2['data']['items']['cdn_url'])
        # exit()
        dic_url.append([item['title'], str2['data']['items']['cdn_url']])

    return dic_url


if __name__ == '__main__':
    # 获取书id
    doc_id = 'caabfaa646f7ba0d4a7302768e9951e79b8969d0'
    items = getList(doc_id)
    for item in items:
        content = getDetail(item[1])
        # item=["第一回",'https://novel-content-new.cdn.bcebos.com/6742163404127555724?md5hash=ed38fd2ad931ce08087e4b796cb404d3&timestamp=1705121443']
        # content = getDetail(item[1])
        text_name = item[0] + '.txt'
        print(text_name)
        with open("./a/" + text_name, "w+", encoding="utf-8") as f:
            f.write(content)
