import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36'
}
# http://pm.weakcn.com/lifanacgup/lifanacg/20161222/4/052.jpg
img_url = "http://pm.weakcn.com/lifanacgup/lifanacg/20161222/4/"
i = 233
while True:
    img = requests.get(img_url + str(i).zfill(3) + ".jpg", headers=headers)
    if img.status_code != 200:
        break
    f = open(str(i) + ".jpg", 'wb')
    f.write(img.content)
    f.close()
    print(i)
    i += 1
    time.sleep(0.01)
