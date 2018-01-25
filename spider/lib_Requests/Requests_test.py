import requests

URL_IP = "http://localhost:8000/ip"
URL_GET = "http://localhost:8000/get"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}


def use_simple_requests():
    response = requests.get(URL_IP, headers=headers)  # get/post/options/put/delete
    print(">>>>>>>Response Header:")
    print(response.headers)
    print(">>>>>>>Response Body:")
    print(response.text)
    print(">>>>>>>Response content:")
    print(response.content)


def use_params_request():
    params = {"param1": "hello", "param2": "world"}

    response = requests.get(URL_GET, params, headers=headers)
    print(">>>>>>>Response Header:")
    print(response.headers)
    print(">>>>>>>Response status:")
    print(response.status_code, response.reason)
    print(">>>>>>>Response Body:")
    print(response.json())  # response.text


if __name__ == "__main__":
    print("---------------")
    use_simple_requests()
    print("+++++++++++++++")
    use_params_request()
