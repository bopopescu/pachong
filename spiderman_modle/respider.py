# -*- coding: utf-8 -*-

import urllib.request
from http import cookiejar
from urllib import parse


datas = ""
dbid = 1
while True:
    print("正在读取" + str(dbid))
    modle_data = {
        'modelid': '7720',
        'modelversion': '1',
        'dbids': str(dbid)
    }
    try:
        login_url = 'http://www.tylinbim.com/login/VerifyLogin.jsp'

        # 1.2 登录的参数
        login_form_data = {
            'loginfile': '/wui/theme/ecology8/page/login.jsp?templateId=5&logintype=1&gopage=',
            'logintype': '1',
            'fontName': '微软雅黑',
            'message': '',
            'gopage': '',
            'formmethod': 'post',
            'rnd': '',
            'serial': '',
            'username': '',
            'isie': 'false',
            'islanguid': '7',
            'loginid': 'ltyzy',
            'userpassword': 'lty1234',
            'submit': '立即登录'
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }

        # 发送post登录请求

        # 定义保存cookie的cookiejar
        cookie_jar = cookiejar.CookieJar()

        # 定义有添加cookie功能的处理器
        cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)

        # 生成opener
        opener = urllib.request.build_opener(cookie_handler)

        # 转译     1.参数需要转译   2.post请求的data要求是bytes
        str_data = urllib.parse.urlencode(login_form_data).encode('utf-8')

        # 带着参数发送post请求
        login_request = urllib.request.Request(login_url, headers=headers, data=str_data)

        target_url = 'http://www.tylinbim.com/4DAnalog/ModelAttributeExpand_getCustomAttrList.action'
        target_request = urllib.request.Request(target_url, headers=headers, data=modle_data)
        response = opener.open(target_url)
        data = response.read().decode('utf-8')
        datas += ","
        datas += data
        dbid += 1

        if dbid == 11:
            print("读取完成,正在写入")
            print(dbid)
            with open('modle_data.csv', 'w', encoding='utf-8') as f:
                f.write(datas)
            print("写入完成")
            break
    except:
        print("未响应,重新读取" + str(dbid))

