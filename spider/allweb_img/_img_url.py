import get_url
from bs4 import BeautifulSoup
import requests
import re
import threading
import img_down

lock = threading.Lock()
proxies = {
  "http": "http://116.242.232.21:808",
  "https": "http://195.133.220.18:42619",
}

def url_analyze(f_img_list):
    lock.acquire()
    web_url = f_img_list.readline()[:-1]
    lock.release()
    while True:
        try:
            url_response = requests.get(web_url, headers=get_url.headers,proxies=proxies,
                                        cookies=get_url.cookie_to_dict(get_url.cookie), timeout=2)
            break
        except:
            continue
    print(url_response.status_code)
    response_info = url_response.text
    soup = BeautifulSoup(response_info, 'html.parser', from_encoding='utf-8')
    img_div = soup.find('div', id='nr234img').find('img')
    page_div = soup.find('div', class_='fanye1').find('a')
    return img_div['src'], re.search('\d+', str(page_div)).group(0)


if __name__ == "__main__":
    #get_url.url_save()
    f_img_list = open('url_2.txt', 'r')
    for count in range(0, 25):
        p = url_analyze(f_img_list)
        p1 = url_analyze(f_img_list)
        p2 = url_analyze(f_img_list)
        p3 = url_analyze(f_img_list)
        t1 = threading.Thread(target=img_down.img_doun, args=(p[0], int(p[1]), 't1' + "-" + str(count)))
        t2 = threading.Thread(target=img_down.img_doun, args=(p1[0], int(p1[1]), 't2' + "-" + str(count)))
        t3 = threading.Thread(target=img_down.img_doun, args=(p2[0], int(p2[1]), 't3' + "-" + str(count)))
        t4 = threading.Thread(target=img_down.img_doun, args=(p3[0], int(p3[1]), 't4' + "-" + str(count)))
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t1.join()
        t2.join()
        t3.join()
        t4.join()

f_img_list.close()
