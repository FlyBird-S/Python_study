import re
from bs4 import BeautifulSoup
import requests
import time

cookie = "CKTH_IN20180127=1; hmruser=20180106180043061728; UM_distinctid=160caea8f6451-07cbb5bed46e29-28792744-238c0-160caea8f65a1; CNZZDATA1271372768=1485705405-1515228502-null%7C1515228502; Hm_lvt_9ddeed30b0a35b858ffca3e7fcd258ad=1515232858; Hm_lvt_ba220f7fa24a365a0c07e809f0bbb2a6=1515232858; CNZZDATA1271374104=1978463683-1515230212-null%7C1515230212; Hm_lvt_6d5e86213b07ede18ec639f1da3bc86b=1515232864,1516172041; ttgg_ucc_26=5c74687e196b4347b88eb2bd64cdec0e; UBGLAI63GV=SmZsc.1517017993; ttgg_ucc_27=39c8156c43eb4738a37d03d2bab381e4; CNZZDATA1271485227=390596817-1515232313-http%253A%252F%252Fm.511wa.com%252F%7C1517018831; myTest=1517022107459; CNZZDATA5773564=cnzz_eid%3D1734276848-1516976903-null%26ntime%3D1517029771; is_show_dsn=1; img_has_show=5331%7C1108%2C5801%7C397%2C5033%7C1065%2C5791%7C396%2C3515%7C732%2C5716%7C1153%2C5498%7C1121%2C5083%7C1070%2C3618%7C747%2C3621%7C748%2C5045%7C1066%2C3398%7C398%2C5641%7C1144%2C5315%7C1108%2C5069%7C1069%2C5652%7C1145%2C5555%7C1128%2C5975%7C1179%2C5220%7C1089%2C5400%7C1114; _s_v_5640=1089%2C1114%2C; Hm_lvt_69d8bdcf4fd5fca32adcd3fb89dca3d0=1515232885,1516172042,1516965345; Hm_lpvt_69d8bdcf4fd5fca32adcd3fb89dca3d0=1517030857"


def cookie_to_dict(cookie_str):
    dict_cookie = {}
    buf_one = cookie_str.split(';')
    for buf_two in buf_one:
        buf_three = buf_two.split("=")
        dict_cookie[buf_three[0]] = buf_three[1]
    return dict_cookie


web_url = "http://m.369107.com/manhua"
proxies = {
  "http": "http://116.242.232.21:808",
  "https": "http://195.133.220.18:42619",
}
headers = {
    "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
}


def url_save():
    f = open("url_2.txt", 'a')
    for page in range(1, 101):
        while True:
            try:
                url_response = requests.get(web_url + '/list_1_' + str(page) + '.html', headers=headers,
                                            cookies=cookie_to_dict(cookie), timeout=2)
                break
            except:
                time.sleep(0.5)
                continue
        print(url_response.status_code)
        soup = BeautifulSoup(url_response.text, 'html.parser', from_encoding='utf-8')
        urls = soup.find_all('a', class_='pic')
        print(urls)
        print(page)
        for url in urls:
            # print('http://m.369107.com' + url['href'])
            f.write('http://m.369107.com' + url['href'] + '\n')
            # print(url.img['src'])
        time.sleep(0.1)
    f.close()
