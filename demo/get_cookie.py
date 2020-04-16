# !/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import json

from dataclasses import dataclass
from urllib import request
from urllib.parse import urljoin
from typing import List, Dict

envget = os.environ.get


@dataclass
class WSCookie:
    splash_url = envget("SPLASH_URL", "http://192.168.3.83:8050")

    def send_request(self, retry_num=0) -> List[Dict]:
        if retry_num > 3:
            print("尝试重新获取数据3次，还是未获取到cookie，请考虑增加代理")
            return []
        post_body = {
            "har": "1",
            "html5_media": "false",
            "http_method": "GET",
            "png": 1,
            "render_all": False,
            "request_body": False,
            "resource_timeout": 0,
            "response_body": False,
            "viewport": "1920x1080",
            "wait": 3,
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
        req = request.Request(url=urljoin(self.splash_url, "/execute"), data=json.dumps(post_body).encode('utf-8'),
                              headers={"content-type": "application/json"})
        resp = request.urlopen(req)

        if resp.status != 200:
            return self.send_request(retry_num+1)

        resp_json = json.loads(resp.read())

        if 'cookie' not in resp_json:
            return self.send_request(retry_num+1)
        return resp_json['cookie']

    @staticmethod
    def parse_cookie(cookies: List[Dict]):
        return {cookie['name']: cookie['value'] for cookie in cookies if cookie['name'] not in ['wzws_cid', 'SESSION']}

    def get_cookie(self) -> Dict[str, str]:
        return self.parse_cookie(self.send_request())


if __name__ == '__main__':
    ws_cookie = WSCookie()
    _cookie = ws_cookie.get_cookie()
    print(_cookie)