from socket import *

def main():
    sock = socket(AF_INET, SOCK_STREAM)
    # sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 8000))
    sock.listen(5)

    while True:
        # 等待浏览器访问
        conn, addr = sock.accept()
        # 接收浏览器发送来的请求内容
        data = conn.recv(1024)
        print(data)

        # 给浏览器返回内容
        conn.send(b'HTTP/1.1 200 OK\r\nContent-Type:text/html; charset=utf-8\r\n\r\n')
        conn.send('<h1 style="color:red">电脑前的你长得真好看!</h1>'.encode('utf-8'))

        # 关闭连接
        conn.close()

if __name__ == '__main__':
    main()