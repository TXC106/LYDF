# -*- coding: utf-8 -*-
# @Time : 2020/2/11
# @Author : kiwi
# @File : library_booksearch.py
# @Project : spider
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import re
# from net_test import mainFunc
import chardet


def searchBooks(bookname):
    # http: // www.lib.cdut.edu.cn / opac / search?tag = search & q = % E8 % BD % AF
    url_main = 'http://www.lib.cdut.edu.cn/opac/search?tag=search&q={}'.format(bookname)

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    #                   ' Chrome/77.0.3865.120 Safari/537.36'
    # }
    # # options = Options()  # 初始设置参数变量
    # # options.add_argument('--headless')	 # 不输出图形
    # # options.add_argument('--no-sandbox')
    # # options.binary_location = r'E:\\tmp\\bin\\chrome.exe'
    # # # driver = webdriver.Chrome(options=options,executable_path="/usr/local/share/chromedriver.exe")
    # # # driver = webdriver.Chrome("E:\\tmp\\Application\\chrome.exe")
    # # driver = webdriver.Chrome(options=options)
    # # # driver = webdriver.Chrome()
    #
    # resp = requests.get(url_main, headers=headers)
    # resp.encoding = 'utf-8'
    #
    # # try:
    # #     # driver.get(url)
    # #     #
    # #     # # 输入图书
    # #     # driver.find_element_by_id('q').send_keys(bookname)
    # #     # # 搜索
    # #     # driver.find_element_by_id('su').click()
    # #     # # 加载
    # #     # time.sleep(0.5)
    # #     resp = requests.get(url_main, headers=headers)
    # #     resp.encoding = 'utf-8'
    # # except:
    # #     # print("图书名称错误或超时", time.ctime())
    # #     # driver.quit()
    # #     status = {
    # #         'status': -1,
    # #         'description': '页面不存在或超时'}
    # #     return status
    # # try:
    # #     # driver.find_element_by_xpath('//*[@id="form1"]/div[4]/div[3]/div[2]/div[2]/ul/li[1]/a').click()
    # #     get_url = driver.current_url
    # # except:
    # #     print("账户密码不正确或响应超时 ", time.ctime())
    # #     driver.quit()
    # #     return 0
    # # driver.switch_to_window(driver.window_handles[1])
    # # 获取url
    # # get_url = driver.current_url
    # # driver.get(get_url)
    # # time.sleep(0.5)
    # # res = driver.page_source
    # # print(resp.text)
    #
    # # 搜索
    # # url_search = 'http://www.lib.cdut.edu.cn/opac/search?tag=search&q=%E8%BD%AF'
    # # url_resp = requests.get(url_search, headers=headers)
    # # url_resp.encoding = 'utf-8'
    # # time.sleep(0.5)
    # soup = BeautifulSoup(resp.text, 'lxml')
    # div = str(soup.find('div', class_='jp-mainCenter'))
    #
    # # print(div)
    # # print(type(div))
    #
    # # 更换链接
    # head_line = 'http://www.lib.cdut.edu.cn/'
    # # html_search = re.sub(r'(?<==").', head_line, div)
    # html_search = re.sub(r'(?<=src=\").', head_line, div)
    # # print(html_search)
    # # exit()
    #
    # # 去除多余信息
    # delete_info = r'(<strong>出版信息：</strong>.*?</p>)(?:[\s\S]*?)(</li>)'
    # new_html_search = re.sub(delete_info, r'\1\2', html_search)
    # # new_html_search = re.findall(delete_info, html_search)
    #
    # # 去除输入框
    # html_text = re.sub(r'<input.*?/>', '', new_html_search)
    # return html_text
    # # print(div)
    # # exit()
    # # result = {
    # #     'status': 1,
    # #     'description': 'success',
    # #     # 'link': get_url
    # # }
    # # return result

    mainPage = searchPages(url_main)
    mainFunc(mainPage)


def searchPages(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/77.0.3865.120 Safari/537.36'
    }
    # try:
    #     resp = requests.get(url, headers=headers)
    #     resp.encoding = 'utf-8'
    # except:
    #     status = {
    #         'status': -1,
    #         'description': '页面不存在或超时'}
    #     return status
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'lxml')
    div = str(soup.find('div', class_='jp-mainCenter'))

    # # 更换链接
    head_line = 'http://www.lib.cdut.edu.cn/'
    html_search = re.sub(r'(?<=src=\").', head_line, div)

    # 去除多余信息
    delete_info = r'(<strong>出版信息：</strong>.*?</p>)(?:[\s\S]*?)(</li>)'
    new_html_search = re.sub(delete_info, r'\1\2', html_search)
    # new_html_search = re.sub(delete_info, r'\1\2', div)

    # 去除输入框
    html_text = re.sub(r'<input.*?/>', '', new_html_search)

    # 去除空白行 否则写入文件错误
    html_text_nos = re.sub('\s', ' ', html_text)

    return getCompleteHtml(html_text_nos)
    # html_file = 'C:\\Users\\kiwi\\Desktop\\test.html'
    # file = open(html_file, 'w')
    # file.write(getCompleteHtml(html_text_nos))
    # file.close()
    # return file


def searchBookPages(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/77.0.3865.120 Safari/537.36'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'lxml')
    table = str(soup.find('table', id='detailsTable'))
    # print(table)
    location_table = str(soup.find('table', id='gctable'))
    print(soup.find('table', id='gctable'))

    return getCompleteDetailHtml(table + location_table)



def getCompleteHtml(res):
    headHtml = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    </head>
    <body>
    <input id="search" type="text"/>
    <button id="search_btn" type="submit" onclick="window.location.href='/opac/search?&q='+document.getElementById('search').value">搜索</button>'''

    endHtml = '''</body>
    </html>'''

    return headHtml+res+endHtml


def getCompleteDetailHtml(res):
    headHtml = '''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml">
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    </head>
    <body>'''

    endHtml = '''</body>
    </html>'''

    return headHtml+res+endHtml


from socket import *
import re
# from library_booksearch import *

global mainHtmlText
# html_file = 'C:/Users/kiwi/Desktop/test.html'
# html_file_new = 'C:/Users/kiwi/Desktop/test2.html'


def RecvN(socket, n):
    totalContent = b''
    totalRecved = 0
    while totalRecved < n:
        onceContent = socket.recv(n - totalRecved)
        print("onceContent", onceContent)
        totalContent += onceContent
        totalRecved = len(totalContent)

    return totalContent


def handle_client(client_socket, mainHtml):
    # 接收对方发送的数据
    recv_data = client_socket.recv(1024).decode("utf-8")  # 1024表示本次接收的最大字节数
    # recv_data = RecvN(client_socket, 1024).decode('utf-8')
    # 打印从客户端发送过来的数据内容
    # print("client_recv:",recv_data)
    request_header_lines = recv_data.splitlines()
    print("recv_ok")
    for line in request_header_lines:
        print(line)
    # if request_header_lines == []:
    #     # time.sleep(2)
    #     response_body = mainHtml
        # handle_client(client_socket, mainHtml)

    # 返回浏览器数据
    # 设置返回的头信息 header
    response_headers = "HTTP/1.1 200 OK\r\n"  # 200 表示找到这个资源
    response_headers += "\r\n"  # 空一行与body隔开
    # 设置内容bodys
    # response_body = "<h1>fat boss<h1>\r\n"
    # response_body += "<h2>come on<h2>\r\n"
    # response_body += "<h3>binlang!!!<h3>\r\n"

    # 跳转链接获取
    # if request_header_lines != []:
    mainPage = re.match('[^/]+(/[^ ]*)', request_header_lines[0])
    # print(mainPage.group(1) == '/')
    searchPage = re.match('[^/]+(/opac/search[^ ]*)', request_header_lines[0])
    iconPage = re.match('[^/]+(/[^.ico]*)', request_header_lines[0])
    newPage = re.match('[^/]+(/opac/book[^ ]*)', request_header_lines[0])
    head_line = 'http://www.lib.cdut.edu.cn'
    if(mainPage.group(1) == '/'):
        response_body = mainHtml
        # # html_file = 'C:\\Users\\kiwi\\Desktop\\test.html'
        # file = open(html_file, 'w')
        # file.write(mainHtml)
        # file.close()
        # # html_file = mainFile
        # # response_body = bytes(mainHtml, encoding='utf-8')
        # file = open(html_file, 'rb')
        # htmlText = file.read().decode('gbk')
        # # print(htmlText.decode('gbk'))
        # # type = chardet.detect(htmlText)
        # response_body = htmlText
        # # print(response_body)
        # file.close()
    if(searchPage != None or iconPage != None):
        # print(re.match('[^/]+(/opac/[^ ]*)', request_header_lines[0]).group(1))
        # print()
        # html_file = 'C:\\Users\\kiwi\\Desktop\\test.html'
        # file = open(html_file, 'rb')
        # response_body = file.read()
        # file.close()
        if(searchPage != None):
            mainHtml = searchPages(head_line + searchPage.group(1))
            # file = open(html_file, 'rb')
            # response_body = file.read()
            # file.close()
            # print(mainHtml)
            response_body = mainHtml
        else:
            # file = open(html_file, 'rb')
            # response_body = file.read()
            # file.close()
            # print("2\n"+mainHtml)
            response_body = mainHtml
    if(newPage != None):
        # html_file = 'C:\\Users\\kiwi\\Desktop\\test2.html'
        newHtml = searchBookPages(head_line + newPage.group(1))
        # file = open(html_file_new, 'rb')
        # response_body = file.read()
        # file.close()
        response_body = newHtml
    # else:
    #     # response_body = mainHtml
    #     time.sleep(2)


    # 合并返回的response数据
    # response = response_headers + response_body
    # response = response_headers + response_body

    # 返回数据给浏览器
    # print(response_body)
    client_socket.send(response_headers.encode("utf-8"))  # 转码utf-8并send数据到浏览器
    client_socket.send(response_body.encode("utf-8"))
    client_socket.close()
    # print("closeok")


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
        # print("circle")
        client_socket, clientAddr = server_socket.accept()
        handle_client(client_socket, mainHtml)
        # print("circle_end")


if __name__ == "__main__":
    searchBooks('软件工程')
    exit()
    # str = 'www.a/'
    str = '<strong>出版信息：</strong>四川文艺出版社  2018.09  成都</p><div id="http://www.lib.cdut.edu.cn/book2665025"></li>'
    str2 = ''
    # # str2.replace(re.compile(str,'=\"/(.*)\"'))
    a = re.sub(r'(<strong>出版信息：</strong>.*?</p>)(?:[\s\S]*?)(</li>)', r'\1\2', str2)
    # a = re.findall(r'<strong>出版信息：</strong>.*?</p>(.*?)</li>', str2)
    # # # a = re.sub('\D', '1', str2)
    # # p1 = re.compile(r'<strong>出版信息：</strong>.*?</p>(.*?)</li>')
    # # print(p1)
    # # # s2 = p1.sub('',str2)
    # str2.replace(r'<strong>出版信息：</strong>.*?</p>(.*?)</li>', '')
    print(a)
    # print("ceshi\nceshi2")
