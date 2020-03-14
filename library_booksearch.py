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

def searchBooks(bookname):
    url_main = 'http://www.lib.cdut.edu.cn/opac/search?tag=search&q={}'.format(bookname)
    # http: // www.lib.cdut.edu.cn / opac / search?tag = search & q = % E8 % BD % AF
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/77.0.3865.120 Safari/537.36'
    }
    # options = Options()  # 初始设置参数变量
    # options.add_argument('--headless')	 # 不输出图形
    # options.add_argument('--no-sandbox')
    # options.binary_location = r'E:\\tmp\\bin\\chrome.exe'
    # # driver = webdriver.Chrome(options=options,executable_path="/usr/local/share/chromedriver.exe")
    # # driver = webdriver.Chrome("E:\\tmp\\Application\\chrome.exe")
    # driver = webdriver.Chrome(options=options)
    # # driver = webdriver.Chrome()
    try:
        # driver.get(url)
        #
        # # 输入图书
        # driver.find_element_by_id('q').send_keys(bookname)
        # # 搜索
        # driver.find_element_by_id('su').click()
        # # 加载
        # time.sleep(0.5)
        resp = requests.get(url_main,headers=headers)
        resp.encoding = 'utf-8'
    except:
        print("图书名称错误或超时", time.ctime())
        # driver.quit()
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
    # get_url = driver.current_url
    # driver.get(get_url)
    # time.sleep(0.5)
    # res = driver.page_source
    # print(resp.text)

    # 搜索
    url_search = 'http://www.lib.cdut.edu.cn/opac/search?tag=search&q=%E8%BD%AF'
    url_resp = requests.get(url_search, headers=headers)
    url_resp.encoding = 'utf-8'
    # time.sleep(0.5)
    soup = BeautifulSoup(url_resp.text, 'lxml')
    div = str(soup.find('div', class_='jp-mainCenter'))

    # 尝试去除首行输入
    # soup = BeautifulSoup(url_resp.text, 'lxml')
    # res = ''
    # for div in soup.find_all('div', class_='http://www.lib.cdut.edu.cn/p-searchList'):
    #     res += div.text

    # print(div)
    # print(type(div))
    head_line = 'http://www.lib.cdut.edu.cn/'
    html_search = re.sub(r'(?<==").', head_line, div)
    # print(html_search)
    # exit()
    delete_info = '(<strong>出版信息：</strong>.*?</p>)(?:[/s/S]*?)(</li>)'
    new_html_search = re.sub(r'(<strong>出版信息：</strong>.*?</p>)(?:[\s\S]*?)(</li>)', r'\1\2', html_search)
    # new_html_search = re.findall(delete_info, html_search)
    return new_html_search
    # print(div)
    # exit()
    # result = {
    #     'status': 1,
    #     'description': 'success',
    #     # 'link': get_url
    # }
    # return result


if __name__ == "__main__":
    print(searchBooks('软件工程'))
    exit()
    # str = 'www.a/'
    str = '<strong>出版信息：</strong>四川文艺出版社  2018.09  成都</p><div id="http://www.lib.cdut.edu.cn/book2665025"></li>'
    str2 = '''<strong>出版信息：</strong>四川文艺出版社  2018.09  成都</p>
<div id="http://www.lib.cdut.edu.cn/book2665025">
</div>
<input name="http://www.lib.cdut.edu.cn/ourceId" type="http://www.lib.cdut.edu.cn/idden" value="http://www.lib.cdut.edu.cn/665025/图书"/>
<div class="http://www.lib.cdut.edu.cn/ollectBooks" id="http://www.lib.cdut.edu.cn/ollectBooks2665025" style="http://www.lib.cdut.edu.cn/isplay: none;">
<strong id="http://www.lib.cdut.edu.cn/howGcCollect"><a class="http://www.lib.cdut.edu.cn/ollectTip" href="http://www.lib.cdut.edu.cn/avascript:;" onmouseout="http://www.lib.cdut.edu.cn/ideGuancang('2665025')" onmouseover="http://www.lib.cdut.edu.cn/howGuancang('2665025')">馆藏预览</a>
</strong>
</div>
<p class="http://www.lib.cdut.edu.cn/ibraryCount">
<span id="http://www.lib.cdut.edu.cn/cinfo2665025">中文图书
</span>
</p>
<p class="http://www.lib.cdut.edu.cn/ollectButton">
<button class="http://www.lib.cdut.edu.cn/tn" id="http://www.lib.cdut.edu.cn/665025" onclick="http://www.lib.cdut.edu.cn/ollect('2665025','软刺','图书','(美) 艾米丽·福里德伦德著','四川文艺出版社','2018.09','I712.45/3622');" title="http://www.lib.cdut.edu.cn/藏">
<span class="http://www.lib.cdut.edu.cn/con-star">收藏</span>
</button>
</p>
<div class="http://www.lib.cdut.edu.cn/ibrary-prompt" id="http://www.lib.cdut.edu.cn/uancang2665025" onmouseout="http://www.lib.cdut.edu.cn/ideGuancang('2665025')" onmouseover="http://www.lib.cdut.edu.cn/howGuancang('2665025')" style="http://www.lib.cdut.edu.cn/isplay: none">
													加载中...
												</div>
<div class="http://www.lib.cdut.edu.cn/ibrary-prompt" id="http://www.lib.cdut.edu.cn/eriesArea2665025" onmouseout="http://www.lib.cdut.edu.cn/ideSeriesArea('2665025')" onmouseover="http://www.lib.cdut.edu.cn/howSeriesArea('2665025')" style="http://www.lib.cdut.edu.cn/isplay: none">
													加载中...
												</div>
</div>
</li>'''
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
