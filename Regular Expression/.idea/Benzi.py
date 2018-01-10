import re,urllib2
from bs4 import BeautifulSoup
import  time
#r'http://www.lifans.net/2780_1.html'
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
        }
ip_list = ["171.39.76.181:8123",
           "121.31.100.19:8123",
           "121.31.100.19:8123",
           "222.76.187.232:8118",
           "61.135.217.7:80",
           "122.114.31.177:808",
           "121.31.151.68:8123",
           "113.121.241.25:29054",
            "106.81.230.127:8118",
            "171.124.8.99:8118",
            "114.95.112.157:8118",
            "114.228.9.240:8118",
            "183.52.150.79:61234",
            "27.213.71.159:8118",
            "183.52.150.171:61234",
            "121.31.101.204:8123",
            "175.155.243.176:808",
            "115.171.69.108:8118",
            "223.241.78.253:8010",
            "121.31.101.176:8123",
            "121.31.194.144:8123",
            "220.166.240.181:8118",
            "222.85.39.5:808",
            "60.169.223.199:21623",
            "121.31.159.152:8123",
            "110.73.4.10:8123",
            "125.126.167.167:20023",
            "222.76.145.124:47820",
            "182.91.94.25:8118",
            "182.39.9.30:20693",
            "223.241.117.14:8010",
            "219.138.58.5:3128",
            "183.52.150.63:61234",
            "182.88.164.164:8123",
            "49.72.4.91:61234",
            "123.53.133.179:38583",
            "59.56.46.42:808",
            "121.31.158.40:8123",
            "183.52.150.129:61234",
            "110.72.36.159:8123",
            "121.31.148.127:8123",
            "110.73.54.53:8123",
            "121.31.162.200:8123",
            "219.138.58.134:3128",
            "222.182.53.242:8118",
            "58.57.75.142:63000",
            "115.194.170.27:8118",
            "222.134.169.210:61234",
            "183.52.150.96:61234",
            "219.138.58.33 :3128"]
def set_ip(ip):
    proxies={"http://":ip}   #设置你想要使用的代理
    proxy_s=urllib2.ProxyHandler(proxies)
    opener=urllib2.build_opener(proxy_s)
    urllib2.install_opener(opener)
    print ip
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1',
#         }
img_count = 1
listurl = []
name_conut = 0
set_ip(ip_list.pop())
def get_img(img_url):
    req = urllib2.Request(url =img_url,headers = headers)
    try:
        url_open = urllib2.urlopen(req)
    except:
        try:
            time.sleep(1)
            url_open = urllib2.urlopen(req)
        except:
            set_ip(ip_list.pop())
            time.sleep(1)
            url_open = urllib2.urlopen(req)
    html_cont = url_open.read()
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    link = soup.find('li',id = "imgshow").find('img')
    return link['src']
def get_page(img_url):
    req = urllib2.Request(url =img_url,headers = headers)
    try:
        url_open = urllib2.urlopen(req)
    except:
        try:
            time.sleep(1)
            url_open = urllib2.urlopen(req)
        except:
            set_ip(ip_list.pop())
            time.sleep(1)
            url_open = urllib2.urlopen(req)
    html_cont = url_open.read()
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    page = soup.find('a', text = re.compile(r"1 /.*?"))
    Num = int(page.get_text().replace("1 /",""))
    return Num

def img_url(x,img_count):
    return r'http://www.lifans.net/'+str(x)+'_'+str(img_count)+'.html'

for x in range(1009,1100):
    img_count = 1
    listurl = []
    page = get_page(img_url(x, 1))+1
    while True:
        print x,img_count
        test_url = get_img(img_url(x, img_count))
        listurl.append(test_url)
        img_count+=1
        if img_count == page:
            break
        print listurl.__len__()
    name_conut = x+name_conut+2000
    add = "C:\\Users\\aff\\Desktop\\benzi1\\"
    print "down_load"
    for url in listurl:
        f = open(add+str(name_conut)+'.jpg','wb')
        print name_conut
        req =urllib2.Request(url=url, headers=headers)
        try :
            print url
            open_img = urllib2.urlopen(req)
            print open_img.getcode()
            buf = open_img.read()
        except:
            try:
                time.sleep(1)
                open_img = urllib2.urlopen(req)
                buf = open_img.read()
            except:
                set_ip(ip_list.pop())
                time.sleep(1)
                open_img = urllib2.urlopen(req)
                buf = open_img.read()

                # req = urllib2.urlopen('url')
                # buf = req.read()
        f.write(buf)
        print name_conut
        name_conut += 1
    print "OK"