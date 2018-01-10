import re,urllib2
from bs4 import BeautifulSoup
import  time
#r'http://www.lifans.net/2780_1.html'
headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
        }
img_count = 1
listurl = []

def get_img(img_url):
    req = urllib2.Request(url =img_url,headers = headers)
    try:
        url_open = urllib2.urlopen(req)
    except:
        try:
            time.sleep(1)
            url_open = urllib2.urlopen(req)
        except:
            return -1
    html_cont = url_open.read()
    soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    link = soup.find('li',id = "imgshow").find('img')
    return link['src']

def img_url(x,img_count):
    return r'http://www.lifans.net/'+str(x)+'_'+str(img_count)+'.html'
def test_1000(x):
    while(True):
        try:
            ret=get_img(img_url(x,img_count))
            if ret == -1:
                break
            print ret
            listurl.append(ret)
            img_count += 1
        except:
            try:
                ret = get_img(img_url(img_count))
                if ret == -1:
                    break
                print ret
                listurl.append(ret)
                img_count += 1
            except:
                pass
    print listurl
for x in range(1,1000):
    print img_url(2727,img_count)
    test_1000(2727)
    i=0+x*100
    add ="C:\\Users\\aff\\Desktop\\benzi1\\"
    for url in listurl:
        f = open(add+"nalid"+str(i)+'.jpg','wb')
        req =urllib2.Request(url=url, headers=headers)
        try :
            buf = urllib2.urlopen(req).read()
        except:
            time.sleep(1)
            buf = urllib2.urlopen(req).read()
        # req = urllib2.urlopen('url')
        # buf = req.read()
        f.write(buf)
        i+=1
    print "OK"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1',
#         }