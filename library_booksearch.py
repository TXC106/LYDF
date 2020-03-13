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

def searchBooks(bookname):
    url = 'http://www.lib.cdut.edu.cn/opac/search/simsearch?subtag=simsearch&tag=search'

    options = Options()  # 初始设置参数变量
    options.add_argument('--headless')	 # 不输出图形
    options.add_argument('--no-sandbox')
    options.binary_location = r'E:\\tmp\\bin\\chrome.exe'
    # driver = webdriver.Chrome(options=options,executable_path="/usr/local/share/chromedriver.exe")
    # driver = webdriver.Chrome("E:\\tmp\\Application\\chrome.exe")
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome()
    try:
        driver.get(url)

        # 输入图书
        driver.find_element_by_id('q').send_keys(bookname)
        # 搜索
        driver.find_element_by_id('su').click()
        # 加载
        time.sleep(0.5)
    except:
        print("图书名称错误或超时", time.ctime())
        driver.quit()
        status = {
            'status': -1,
            'description': '页面不存在或超时'}
        return status
    # try:
    #     # driver.find_element_by_xpath('//*[@id="form1"]/div[4]/div[3]/div[2]/div[2]/ul/li[1]/a').click()
    #     get_url = driver.current_url
    # except:
    #     print("账户密码不正确或响应超时 ", time.ctime())
    #     driver.quit()
    #     return 0
    # driver.switch_to_window(driver.window_handles[1])
    # 获取url
    get_url = driver.current_url
    # driver.get(get_url)
    # res = driver.page_source
    # soup = BeautifulSoup(res, 'lxml')
    # div = soup.findAll('div', class_='jp-mainCenter')
    # print(div)
    result = {
        'status': 1,
        'description': 'success',
        'link': get_url
    }
    return result


if __name__ == "__main__":
    print(searchBooks('软件工程'))
