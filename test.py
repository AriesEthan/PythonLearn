!#/usr/local/bin/python3
import platform
import requests
print(platform.platform())

"""response = requests.get("https://www.zhihu.com")
print(type(response))
print(response.status_code)
print(type(response.text))
print(response.text)
print(response.cookies)
print(response.content)
print(response.content.decode("utf-8"))

response.encoding="utf-8"
print(response.text)
"""
import requests
import json
response = requests.get("https://httpbin.org/get")
print(type(response.text))
print(response.json())
print(json.loads(response.text))
print(type(response.json()))