import requests
import re

'''
从http://www.xicidaili.com/中获取http代理ip10000条
'''
url = "http://www.xicidaili.com/wt/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}


def get_ip(count):
    response = requests.get(url + str(count), headers=headers)
    ips = re.findall("\d+\.\d+\.\d+\.\d+\D+\d+", response.text) #122.114.31.177</td>      <td>808
    ips = [re.sub("\D{2,}", ":", ip) for ip in ips]
    for ip in ips:
        f.write(ip + "\n")


f = open("ip.txt", 'a')
for count in range(1,101):
    get_ip(count)
    print(count)
f.close()
