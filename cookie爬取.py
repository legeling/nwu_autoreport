#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：cookie爬取.py
@IDE     ：PyCharm 
@Author  ：lingxiaotian
@Date    ：2022/1/7 7:13 PM 
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def request_html(url):
    # 创建浏览器操作对象
    # 无界面模式
    # chrome_options = Options()
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    path = "../plug/chromedriver"
    # path = r'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    # ~/Applications/Google/Chrome.app/Contents/MacOS/Google/Chrome"
    # chrome_options.binary_location = path

    browser = webdriver.Chrome(path)
    # browser = webdriver.Chrome(chrome_options=chrome_options)

    # 模拟真实浏览器访问网站
    browser.get(url)
    # 获取网页源代码
    # html = browser.page_source
    return browser

def interactive(browser,username,password):
    # 获取文本框对象
    input_name = browser.find_element_by_id('username')
    # 在文本框中输入内容
    time.sleep(1)
    input_name.send_keys(username)
    time.sleep(1)
    # 输入密码
    input_password = browser.find_element_by_id('password')
    input_password.send_keys(password)
    time.sleep(1)
    # 获取按钮【一周内免登陆】，并点击
    button = browser.find_element_by_xpath("//div[@class='icheckbox_square-green']")
    button.click()
    time.sleep(1)
    # 登录
    button = browser.find_element_by_xpath('//button/..')
    button.click()
    time.sleep(1)
    # next = browser.find_element_by_xpath("//a[@class='n']")
    browser.get("https://app.nwu.edu.cn/site/ncov/dailyup")
    cookies_list = browser.get_cookies()
    cookies_dict = dict()
    for cookie in cookies_list:
        cookies_dict[cookie['name']] = cookie['value']
    # print(cookies_dict)
    cookie = 'eai-sess' + '=' + cookies_dict['eai-sess'] + ';' + 'UUkey' + '=' + cookies_dict['UUkey'] + ';' + 'iPlanetDirectoryPro' + '=' + cookies_dict['iPlanetDirectoryPro']
    print('cookie:'+cookie)
    browser.close()
    return cookie

if __name__ == '__main__':
    try:
        url = "https://app.nwu.edu.cn/site/ncov/dailyup"
        username = input("请输入用户名:")
        password = input("请输入密码:")
        browser = request_html(url)
        cookie = interactive(browser,username,password)
        result = {"name":"","cookie":cookie,"number":username,"password":password}
        print(result)
    except:
            print("用户名或密码错误")

