import requests

url = "https://www.xiniudata.com/industry/newest"
request = requests.get(url)

print(request.content)