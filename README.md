# wenshu

> 文书网cookie获取 2020-04-16

获取cookie的demo请见[demo](./demo/get_cookie.py)


⚠️如果获取cookie的地址是 `https://wenshu.court.gov.cn/` 这是https，那么是不会返回 `80S` 和 `80T` 这两个cookie的，返回的是 `443S` 和 `443T`

⚠️获取cookie的地址是 `http://wenshu.court.gov.cn/` 这是http的，那么才会返回 `80S` 和 `80T` 这两个cookie的


获取的 cookie 是通过 http的链接获取，后面的爬取也用http

获取 cookie 是通过 https 获取的，后面的爬取也用https 即可



## 2019-10-24 再次更新

1. 这次如果按照以前的请求方式，会返回一个html页面

	这个页面如 [demo.html](https://github.com/nciefeiniu/wenshu/blob/master/demo.html)

2. 用浏览器打开这个文件，会发现会重定向到一个新的URL

	如：http://localhost:63342/WZWSREL3dlYnNpdGUvcGFyc2UvcmVzdC5xNHc=?wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDQxNjUyNzE=

	因为是本地打开的，所以域名是`localhost:63342`

3. 把这个本地地址换成 `http://wenshu.court.gov.cn`这个后

	神奇的事情发生了，可以获取到数据了。而且后面的请求也没返回这个 `html` 文件了。

### 所以这次反爬解决方案

1. 在请求返回的地方增加一个判断，如果是 `html` 文件，那么就解析这个文件，获取新的URL，并重试，发送 `post` 请求即可。

2. 这个html怎么解析？？

~这个可以看看 @songguoxiong 的项目下的 [decrypt.py文件](https://github.com/songguoxiong/wenshu_utils/blob/master/wenshu_utils/old/wzws/decrypt.py)~

请看 `decrypt.py` 文件

⚠️ 注意 splash返回的cookie中，需要去除 `wzws_cid` 这个cookie



### 获取教程

一. 安装splash
  
  推荐docker启动一个splash容器
  ```
  docker run -it -p 8050:8050 scrapinghub/splash
  ```
  
  [splash安装教程📖](https://splash.readthedocs.io/en/stable/install.html#linux-docker)

二. 通过splash获取这三个cookie，代码如下

[demo](./demo/get_cookie.py)