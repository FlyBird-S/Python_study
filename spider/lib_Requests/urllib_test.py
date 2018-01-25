import urllib
import urllib.request

URL_IP = "http://localhost:8000/ip"
URL_GET = "http://localhost:8000/get"


def use_simple_urllib():
    req = urllib.request.Request(URL_IP)
    req.add_header("User-Agent", "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)")
    response = urllib.request.urlopen(req)
    print(">>>>>>>Response Header:")
    print(response.info())
    print(">>>>>>>Response Body:")
    print("".join([line.decode("utf-8") for line in response.readlines()]))


def use_params_urllib():
    params = urllib.parse.urlencode({"param1": "hello", "param2": "world"})  # "param1=hello&param2=world"
    print("Request Params")
    print(params)
    response = urllib.request.urlopen("?".join([URL_GET, params]))
    print(">>>>>>>Response Header:")
    print(response.info())
    print(">>>>>>>Response Body:")
    print("".join([line.decode("utf-8") for line in response.readlines()]))


if __name__ == "__main__":
    # print("use python3_urllib")
    # use_simple_urllib()
    use_params_urllib()
