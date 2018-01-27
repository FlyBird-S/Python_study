import requests

url = "http://www.baidu.com"
proxies = {
  "http": "http://116.242.232.21:808",
  "https": "http://195.133.220.18:42619",
}
response = requests.get(url,proxies=proxies)
print(response.content)