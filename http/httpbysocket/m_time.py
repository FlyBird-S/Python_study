import time
time.ctime()
def application(env,handle_headers): # env 传入信息，  handle_headers是需要执行的函数
    env = {
        "PATH_INFO": file_name,
        "QUERY_STRING": param,
    }
    status_code = 200,500....
    handle_headers(status_code,["content-type":"text/...plain"])
    return body