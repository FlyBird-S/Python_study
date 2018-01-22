import socket

from multiprocessing import Process

HTML_ROOT_DIR = r""
html_response = """
    <html>
    <body>
    <h1>Hello</h1>
    </body>
    </html>"""


def handle_client(client_socket):
    # """处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request_data:\n", request_data)
    # 构造响应数据
    response_start_line = "HTTP/1.11 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = html_response
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response_data:\n", response)
    # 向客户端返回响应
    client_socket.send(bytes(response, "utf-8"))
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('', 9988))
    server_socket.listen(128)

while True:
    client_socket, client_address = server_socket.accept()
    print("%s,%s 用户连接" % client_address)
    handle_client_process = Process(target=handle_client, args=(client_socket,))  # 多进程
    handle_client_process.start()
    client_socket.close()  # 子进程已经复制了一份资源
