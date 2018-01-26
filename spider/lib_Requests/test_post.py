import requests
url = "http://iqianyue.com/mypost"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 '
                  'Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400 '
}
post_data = {"name": "宋鹏飞", "pass": "123"}
response = requests.post(url, post_data)
print(response.text)
