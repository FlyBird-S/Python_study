import socket
import re
import threading

PY_ROOT_DIR = "./wsgi_pydir/"


class HTTPServer(object):
    """"""

    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # SOL socket 选项级别
        self.server_socket.bind(('', port))

    def start_response(self, status, headers):
        # status = "200 OK"
        # headers = [
        #     ("Content-Type", "text/plain")
        # ]
        # start_response(status, headers)
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers

    def handle_client(self, client_socket):
        # """处理客户端请求"""
        # 获取客户端请求数据
        request_data = client_socket.recv(1024)
        request_data_lines = request_data.splitlines()
        print("request_data:")
        for line in request_data_lines:
            print(line)
        request_start_line = request_data_lines[0]

        # GET / HTTP/1.1
        file_name = re.match(r"\w+ +(/[^ ]*)*", request_start_line.decode('utf-8')).group(
            1)  # \w+ +(/[^ ]+) #[^ ]代表非空格 group(1)第一个括号匹配的
        # b'ddd'字符串不能直接通过str转换，需要通过decode('utf-8')转换
        # .py结尾 则执行py程序  run a program
        if file_name.endswith(".py"):
            py = __import__(file_name[1:-3])  # 导入对应模块
            env = {}
            response_body = py.application(env, self.start_response)  # WSGI协议  （env 传入参数 start_response 处理函数）
            response = self.response_headers + "\r\n" + response_body
        else:
            if file_name == r"/":
                file_name = "/index.html"
            file_name = file_name[1::]
            # 打开文件读取内容
            # 构造响应数据
            try:
                print(file_name)
                file = open(file_name, "rb")
            except IOError:
                file_data = "the file not found"
                response_start_line = "HTTP/1.11 404 Not Found\r\n"
                response_headers = "Server: My server\r\n"
            else:
                file_data = file.read()
                file_data = file_data.decode('utf-8')
                file.close()
                response_start_line = "HTTP/1.11 200 OK\r\n"
                response_headers = "Server: My server\r\n"
                # response_body = html_response
            response_body = file_data
            response = response_start_line + response_headers + "\r\n" + response_body
            print("response_data:\n", response)
            # 向客户端返回响应
        client_socket.send(bytes(response, "utf-8"))
        client_socket.close()

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_address = self.server_socket.accept()
            print("%s,%s 用户连接" % client_address)
            test = threading.Thread(target=self.handle_client, args=(client_socket,))
            test.start()
            test.join()
            client_socket.close()  # 子进程已经复制了一份资源


if __name__ == "__main__":
    http_server = HTTPServer(8012)
    http_server.start()
