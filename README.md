# wenshu
文书网cookie获取 2019-10-23


## 2019-10-23 可行方案

现在比较难的就是获取 cookie

一个为 xx80T 另一个为 xx80S  还有一个是SESSION


其实这个可以在首页获取到的


### 获取教程

一. 安装splash
  
  推荐docker启动一个splash容器
  ```
  docker run -it -p 8050:8050 scrapinghub/splash
  ```

二. 通过splash获取这三个cookie，代码如下

```python
# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""

2019-10-22

文书网再次改版，需要一个cookie，不知道这个cookie怎么获取的，没找到破解方法，所以采用splash请求首页去获取这个cookie

这个cookie是 "HM4hUBT0dDOn80T"

"""

import os
import json
import requests

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv('.env'))
envget = os.environ.get

SPLASH_URL = envget("SPLASH_URL", "http://192.168.3.83:8050")


def get_wenshu_cookie():
    """
    获取请求必须携带的cookie
    :return:
    """

    _params = {
        "har": "1",
        "html5_media": "false",
        "http_method": "GET",
        "png": 1,
        "render_all": False,
        "request_body": False,
        "resource_timeout": 0,
        "response_body": False,
        "viewport": "1024x768",
        "wait": 0.5,
        "images": 1,
        "html": 1,
        "expand": 1,
        "timeout": 90,
        "url": "http://wenshu.court.gov.cn/",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "lua_source": """function main(splash, args)
                          assert(splash:go(args.url))
                          assert(splash:wait(0.5))
                            splash.images_enabled = false
                          return {
                            cookie = splash:get_cookies()
                          }
                        end
                       """
    }

    res = requests.post(url=SPLASH_URL + '/execute', data=json.dumps(_params),
                        headers={"content-type": "application/json"})

    _temp_res = {}
    if res.status_code == 200:
        res_json = res.json()
        for cookie in res_json['cookie'] if res_json else []:
            _temp_res[str(cookie['name'])] = str(cookie['value'])
        return _temp_res
    else:
        print res.status_code
        return {}


if __name__ == '__main__':
    os.environ['SPLASH_URL'] = "http://192.168.3.83:8050"
    print get_wenshu_cookie()

```
