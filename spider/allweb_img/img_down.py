import get_url
import requests
import os
import time

proxies = {
  "http": "http://116.242.232.21:808",
  "https": "http://195.133.220.18:42619",
}
def img_doun(url,page,dir_name):
    f = open("ip.txt",'r')
    dir = "./"+dir_name
    os.mkdir(dir)
    img_url = url[:-7]
    i = 1
    while True:
        while True:
            try:
                img = requests.get(img_url + str(i).zfill(3) + ".jpg", headers= get_url.headers,proxies=proxies,timeout=2)
                break
            except:
                time.sleep(0.2)
                # print("o")
#                proxies['http']= "http://"+f.readline()[:-1]
                # print("k")
                # print(proxies)
                continue
        f = open(dir+'/'+str(i) + ".jpg", 'wb')
        f.write(img.content)
        f.close()
        print(i)
        i += 1
        if i > page:
            f.close()
            return

if __name__ == "__main__":
    img_doun('http://pm.weakcn.com/lifanacgup/lifanacg/20180123/3/000.jpg',49,"ww")