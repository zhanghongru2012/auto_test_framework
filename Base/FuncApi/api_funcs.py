import requests
from requests import Request, Session
import json
import time


def login_get_token_highway_mobile():
    url = 'http://192.168.0.50:7082/security/entry-ctl/mobile-login'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'admin_name': 'admin',
        'admin_pwd': '123456'
    }
    r = requests.post(url=url, headers=headers, data=data)

    for k, v in r.json().items():
        if k == 'token':
            return v


def login_highway_web():
    url = 'http://192.168.0.50:7082/security/entry-ctl/login'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'admin_name': 'admin',
        'admin_pwd': '123456'
    }
    r = requests.post(url=url, headers=headers, data=data)
    for k, v in r.json().items():
        if k == 'token':
            return v


def get_user_info():
    url = 'http://192.168.0.50:7082/mobile/memberMobileApiController/getMyInfo'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'accept': 'application/json',
        'authorization': 'JGPSESSIONID={token_value}'.format(token_value=login_get_token_highway_mobile()),
        # 'Referer': 'https://servicewechat.com/wx0a7d9636bba4fb50/0/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN'
    }
    data = {
        'state': '4',
        'userId': 'dfeae1fd83014e988bd90b3a69a896bc'
    }
    r = requests.post(url=url, headers=headers, data=data)
    order_list = r.json()['data']['resultMap']['orderList']
    print(order_list, type(order_list))
    orderNumbers = []
    for i in order_list:
        for k,v in i['order'].items():
            if k == 'orderNumber':
                orderNumbers.append(v)
    # print(orderNumbers)
    return orderNumbers[0]


def submit_order():
    now = time.strftime('%Y-%m-%d', time.localtime())
    # print(now)
    date = now.replace(now[-1], str(int(now[-1]) + 1))
    url = 'http://192.168.0.50:7082/mobile/commodityMobileApiController/submitOrder'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'accept': 'application/json',
        'authorization': 'JGPSESSIONID={token_value}'.format(token_value=login_get_token_highway_mobile()),
        # 'Referer': 'https://servicewechat.com/wx0a7d9636bba4fb50/0/page-frame.html',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/7.0.14(0x17000e2e) NetType/WIFI Language/zh_CN'
    }
    data = {
        'addressId': '35053e6db1d643d1b15ab6b8de9738d2',
        'goodId': '90e6537eb17d4b2f9d6dd5e14b0ed69d',
        'modelId': '8662b1fed1fd426d9f91543e2cc2388b',
        'num': '30',
        'invoice': '{"invoiceType":1,"invoiceTop":1,"title":"","taxpayerNumber":"","registerAddress":"","registerTel":"","bank":"","bankNumber":"","ticketTel":"","ticketMail":"","ticketName":"","ticketAddress":""}',
        'date': date,
        'remarks': 'autotest-api',
        'whetherHave': 'N',
        'whetherInvoice': 'N',
        'userId': 'dfeae1fd83014e988bd90b3a69a896bc'
    }
    r = requests.post(url=url, headers=headers, data=data)
    print(r.json())
    return r.status_code

# submit_order()
get_user_info()
