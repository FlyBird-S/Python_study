import re,urllib2
req = urllib2.urlopen(r'https://image.baidu.com/search/index?ct=201326592&cl=2&st=-1&lm=-1&nc=1&ie=utf-8&tn=baiduimage&ipn=r&rps=1&pv=&fm=rs1&word=火影忍者污&hs=0&oriquery=火影忍者&ofr=火影忍者&sensitive=0')
print req.getcode()
buf = req.read()
listurl = re.findall(r'https://.+?.jpg',buf)
listurl = [i.replace('src="','http:') for i in listurl] #lsit exchange
listurl = set(listurl)# remove repeat
print listurl
i=0
for url in listurl:
    f = open("C:\\Users\\aff\\Desktop\\python\\" +"test"+ str(i)+'.jpg','wb')
    req = urllib2.urlopen(url)
    buf = req.read()
    f.write(buf)
    i+=1
print "OK"

