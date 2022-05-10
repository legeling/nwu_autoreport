#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject 
@File    ：autoreport_1.1.py
@IDE     ：PyCharm 
@Author  ：lingxiaotian
@Date    ：2022/1/4 8:17 PM 
'''

import requests
import time
import json
import jsonpath
import logging
logging.basicConfig(level=logging.INFO,
        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
        datefmt='%Y-%m-%d %a %H:%M:%S',
        filename='resoult.log',
        filemode='w')
# 从json文件中读取数据
# 文件格式："0006":{"name": "","cookie": "","number": ""}
def user_info():
    cookie_obj = json.load(open("cookielist.json",'r',encoding='utf-8'))
    cookie_list = jsonpath.jsonpath(cookie_obj,'$..cookie')
    name_list = jsonpath.jsonpath(cookie_obj,'$..name')
    return cookie_list,name_list


# 提交上报请求，并查看结果
def PostHtml(Cookie, Name,i):
    post_url = "https://app.nwu.edu.cn/ncov/wap/open-report/save"
    # url ="https://app.nwu.edu.cn/site/ncov/dailyup"
    headers = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '1933',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': Cookie,
        'Host': 'app.nwu.edu.cn',
        'Origin': 'https://app.nwu.edu.cn',
        'Referer': 'https://app.nwu.edu.cn/site/ncov/dailyup',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # 提交地址
    data = {
        'sfzx': '1',
        'tw': '1',
        'area': '陕西省 西安市 长安区',
        'city': '西安市',
        'province': '陕西省',
        'address': '陕西省西安市长安区郭杜街道居安路万科城润园',
        'geo_api_info': '{"type":"complete","info":"SUCCESS","status":1,"fEa":"jsonp_818723_","position":{"Q":34.14713,"R":108.88432,"lng":108.88432,"lat":34.14713},"message":"Get ipLocation success.Get address success.","location_type":"ip","accuracy":null,"isConverted":true,"addressComponent":{"citycode":"029","adcode":"610116","businessAreas":[{"name":"郭杜","id":"610116","location":{"Q":34.160655,"R":108.86978899999997,"lng":108.869789,"lat":34.160655}}],"neighborhoodType":"","neighborhood":"","building":"","buildingType":"","street":"学府大街","streetNumber":"242号","country":"中国","province":"陕西省","city":"西安市","district":"长安区","towncode":"610116002000","township":"郭杜街道"},"formattedAddress":"陕西省西安市长安区郭杜街道居安路万科城润园","roads":[],"crosses":[],"pois":[]}',
        'sfcyglq': '0',
        'sfyzz': '0',
        'qtqk': '',
        'ymtys': ''
    }

    response = requests.post(url=post_url, data=data, headers=headers)
    content = response.text
    # logging.info()(content[12:16])
    logging.info("上报队列：" + str(i + 1) + "，用户名：" + Name + "，上报结果：" + content)


# 循环遍历，读取每一个用户信息
def PostAll():
    # logging.info()(len(Cookie_list))
    Cookie_list = user_info()[0]
    Name_list = user_info()[1]
    for i in range(len(Cookie_list)):
        Cookie = Cookie_list[i]
        Name = Name_list[i]
        PostHtml(Cookie, Name,i)

def mission():
    for a in range(999):
        logging.info("开始上报")
        PostAll()
        logging.info("上报结束")
        logging.info("为防止上报失败，五分钟后将再次上报")
        time.sleep(300)
        PostAll()
        logging.info("再次上报结束，程序将于12小时后再次上报")
        time.sleep(42900)


if __name__ == '__main__':
    try:
        mission()
    except:
        logging.warning("运行出错，我也不知道哪里出错了，反正就是报错了~")
