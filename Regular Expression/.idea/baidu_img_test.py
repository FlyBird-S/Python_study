import re,urllib2
headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
req = urllib2.Request(url = r'https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=火影忍者污&hs=0&oriquery=火影忍者&ofr=火影忍者&sensitive=0',headers = headers)
print urllib2.urlopen(req).getcode()
buf = urllib2.urlopen(req).read()
#req = urllib2.urlopen('https://www.041dd.com/htm/downlist1/')
#buf = req.read()
listurl = re.findall(r"https://.+?.jpg",buf)
# listurl = [i.replace('src="','http:') for i in listurl]
listurl = set(listurl)
print listurl
i=0
add ="C:\\Users\\aff\\Desktop\\naliduo\\"
for url in listurl:
    f = open(add+"nalid"+str(i)+'.jpg','wb')
    req =urllib2.Request(url=url, headers=headers)
    buf = urllib2.urlopen(req).read()
    # req = urllib2.urlopen('url')
    # buf = req.read()
    f.write(buf)
    i+=1
print "OK"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_2 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A456 Safari/602.1',
#         }