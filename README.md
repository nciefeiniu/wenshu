# wenshu
文书网cookie获取 2019-10-23


## 2019-10-24 再次更新

这次如果按照以前的请求方式，会返回一个html页面

这个页面如 [demo.html](https://github.com/nciefeiniu/wenshu/blob/master/demo.html)

用浏览器打开这个文件，会发现会重定向到一个新的URL

如：http://localhost:63342/WZWSREL3dlYnNpdGUvcGFyc2UvcmVzdC5xNHc=?wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDQxNjUyNzE=

因为是本地打开的，所以域名是`localhost:63342`

把这个本地地址换成 `http://wenshu.court.gov.cn`这个后

神奇的事情发生了，可以获取到数据了。而且后面的请求也没返回这个 `html` 文件了。

### 所以这次反爬解决方案

在请求返回的地方增加一个判断，如果是 `html` 文件，那么就解析这个文件，获取新的URL，并重试，发送 `post` 请求即可。

这个html怎么解析？？

这个可以看看 @songguoxiong 的项目下的 [decrypt.py文件](https://github.com/songguoxiong/wenshu_utils/blob/master/wenshu_utils/old/wzws/decrypt.py)


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
  
  [splash安装教程📖](https://splash.readthedocs.io/en/stable/install.html#linux-docker)

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
        # 这个cookie不能要，这个cookie会在 wzws解密的地方增加上去
        if "wzws_cid" in _temp_res:
            _temp_res.pop("wzws_cid")
        return _temp_res
    else:
        print res.status_code
        return {}


if __name__ == '__main__':
    os.environ['SPLASH_URL'] = "http://192.168.3.83:8050"
    print get_wenshu_cookie()

```
