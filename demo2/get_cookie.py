# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from typing import Dict

from PyQt5.QtCore import QEventLoop, QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile


def callback(html):
    print(html)


def get_cookie(url: str) -> Dict[str, str]:

    class Render(QWebEngineView):
        cookies = {}
        html = None

        def __init__(self, url):
            self.app = QApplication(sys.argv)
            super(Render, self). __init__()
            self.page().profile().setHttpUserAgent(
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
            )
            self.resize(1920, 1080)
            self.loadFinished.connect(self._loadFinished)
            self.load(QUrl(url))

            QWebEngineProfile.defaultProfile().cookieStore().cookieAdded.connect(self._onCookieAdd)

            while self.html is None:
                self.app.processEvents(QEventLoop.ExcludeUserInputEvents | QEventLoop.ExcludeSocketNotifiers | QEventLoop.WaitForMoreEvents)

        def _onCookieAdd(self, cookie):
            print(cookie.domain())
            if cookie.domain() != 'wenshu.court.gov.cn':
                return
            name = cookie.name().data().decode('utf-8')
            value = cookie.value().data().decode('utf-8')
            self.cookies[name] = value

        def _callable(self, data):
            self.html = data

        def _loadFinished(self):
            self.page().toHtml(self._callable)

        def __del__(self):
            self.app.quit()

    return Render(url).cookies


if __name__ == '__main__':
    urll = "http://wenshu.court.gov.cn/"
    print(get_cookie(urll))