import time


def application(env, start_response):  # env 传入信息，  handle_headers是需要执行的函数
    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()
