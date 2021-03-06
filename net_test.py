# -*- coding: utf-8 -*-
# @Time : 2020/3/15
# @Author : kiwi
# @File : net_test.py
# @Project : Spider

# coding=utf-8
from socket import *
import re
# from library_booksearch import *


def handle_client(client_socket, mainHtml):
    # 接收对方发送的数据
    recv_data = client_socket.recv(1024).decode("utf-8")  # 1024表示本次接收的最大字节数
    # 打印从客户端发送过来的数据内容
    # print("client_recv:",recv_data)
    request_header_lines = recv_data.splitlines()
    for line in request_header_lines:
        print(line)

    # 返回浏览器数据
    # 设置返回的头信息 header
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200 表示找到这个资源
    response_headers += "\r\n"  # 空一行与body隔开
    # 设置内容body
    # response_body = "<h1>fat boss<h1>\r\n"
    # response_body += "<h2>come on<h2>\r\n"
    # response_body += "<h3>binlang!!!<h3>\r\n"

    # 跳转链接获取
    mainPage = re.match('[^/]+(/ )*', request_header_lines[0])
    searchPage = re.match('[^/]+(/opac/search[^ ]*)', request_header_lines[0])
    iconPage = re.match('[^/]+(/[^.ico]*)', request_header_lines[0])
    newPage = re.match('[^/]+(/opac/book[^ ]*)', request_header_lines[0])
    head_line = 'http://www.lib.cdut.edu.cn'
    if(mainPage == '/'):
        response_body = mainHtml
    if(searchPage != None or iconPage != None):
        # print(re.match('[^/]+(/opac/[^ ]*)', request_header_lines[0]).group(1))
        # print()
        # html_file = 'C:\\Users\\kiwi\\Desktop\\test.html'
        # file = open(html_file, 'rb')
        # response_body = file.read()
        # file.close()
        if(searchPage != None):
            mainHtml = searchPages(head_line + searchPage)
            response_body = mainHtml
    if(newPage != None):
        # html_file = 'C:\\Users\\kiwi\\Desktop\\test2.html'
        # file = open(html_file, 'rb')
        # response_body = file.read()
        # file.close()
        newHtml = searchPages(head_line + newPage)
        response_body = newHtml


    # 合并返回的response数据
    # response = response_headers + response_body
    # response = response_headers + response_body

    # 返回数据给浏览器
    client_socket.send(response_headers.encode("utf-8"))  # 转码utf-8并send数据到浏览器
    client_socket.send(response_body)
    client_socket.close()


def mainFunc(mainHtml):
    # 创建套接字
    server_socket = socket(AF_INET, SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7788端口
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 设置服务端提供服务的端口号
    server_socket.bind(('', 7788))
    # 使用socket创建的套接字默认的属性是主动的，使用listen将其改为被动，用来监听连接
    server_socket.listen(128)  # 最多可以监听128个连接
    # 开启while循环处理访问过来的请求
    while True:
        # 如果有新的客户端来链接服务端，那么就产生一个新的套接字专门为这个客户端服务
        # client_socket用来为这个客户端服务
        # server_socket就可以省下来专门等待其他新的客户端连接while True:
        client_socket, clientAddr = server_socket.accept()
        handle_client(client_socket, mainHtml)


def getType(a, b, c):
    minInput = min(a, b, c)
    maxInput = max(a, b, c)
    # type = []
    if minInput == maxInput:
        type = 1
    else:
        type = 0
    for i in a, b, c:
        if i+minInput > maxInput:
            if i == minInput or i == maxInput:
                type += 1
                # if minInput == maxInput:
                #     type.append(3)
        else:
            type += 0
    typeName = {
        0: "非三角形",
        1: "非三角形",
        2: "等腰三角形",
        3: "等腰三角形",
        4: "等边三角形"
    }
    print(typeName.get(type))




if __name__ == "__main__":
    # mainFunc()
    # searchBooks('计算机')
    # handle_client()
    while 1:
        a = input("a:")
        if a == '#':
            exit()
        a = int(a)
        b = int(input("b:"))
        c = int(input("c:"))
        getType(a, b, c)


