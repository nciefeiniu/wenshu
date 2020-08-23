# 文书网cookie获取两种方式

> 本项目只做技术探讨，请勿用于违法用途。

## 第一种获取方式

> 文书网cookie获取 2020-04-16（通过splash获取cookie）

获取cookie的demo请见[demo](./demo/get_cookie.py)


⚠️如果获取cookie的地址是 `https://wenshu.court.gov.cn/` 这是https，那么是不会返回 `80S` 和 `80T` 这两个cookie的，返回的是 `443S` 和 `443T`

⚠️获取cookie的地址是 `http://wenshu.court.gov.cn/` 这是http的，那么才会返回 `80S` 和 `80T` 这两个cookie的


获取的 cookie 是通过 http的链接获取，后面的爬取也用http

获取 cookie 是通过 https 获取的，后面的爬取也用https 即可


⚠️注意：请替换为 `https` ， `http` 已阵亡！！！！！！！！！！！！！！！！！！


### 获取教程

一. 安装splash
  
  推荐docker启动一个splash容器
  ```
  docker run -it -p 8050:8050 scrapinghub/splash
  ```
  
  [splash安装教程📖](https://splash.readthedocs.io/en/stable/install.html#linux-docker)

二. 通过splash获取这三个cookie，代码如下

[demo](./demo/get_cookie.py)


## 第二种获取方式

> 通过 PyQtWebEngine 获取cookie

示例代码如  [demo2](./demo2/get_cookie.py)



# 反爬应对措施，2019-10-24 再次更新

> 返回响应代码 202 的解决方式(这个更新了，需要重新逆向这个js，最近没太多时间)

1. 这次如果按照以前的请求方式，会返回一个html页面


这个页面如 [demo.html](https://github.com/nciefeiniu/wenshu/blob/master/demo.html)


```html
   <html>
<head>
</head>
<body>
<noscript>
<h1><strong>请开启JavaScript并刷新该页.</strong></h1>
</noscript>
<script type="text/javascript">
eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0 1="2";0 3="4";0 5="6";0 7="8";0 9="a";',11,11,'var|dynamicurl|/WZWSREL3dlYnNpdGUvcGFyc2UvcmVzdC5xNHc=|wzwsquestion|*5TLni-b([!,-t$B|wzwsfactor|3740|wzwsmethod|post|wzwsparams|__RequestVerificationToken=IcSXIWWM6HSc4Mp6wXAgWxLd&ciphertext=1001000+1101011+1010100+110001+1011000+1000111+110011+1001011+1100100+1110010+1111010+1101000+1100010+1011000+1101000+1010101+1001111+1000100+1110010+1001000+1010000+1011000+1010101+1110111+110010+110000+110001+111001+110001+110010+110010+110100+1001001+1110111+1111010+1001011+1110011+1110110+1111000+1000101+1101011+1000101+1001000+1010001+1001010+1111000+1110110+1100110+1100111+1100101+1110010+1110111+1001000+1000001+111101+111101&pageId=y83l99c8jdhgfb1y9ja4hh7hkfi1l7ci&queryCondition=%5B%7B%22key%22%3A+%22s15%22%2C+%22value%22%3A+%229727%22%7D%5D&pageSize=5&cfg=com.lawyee.judge.dc.parse.dto.SearchDataDsoDTO%40queryDoc&sortFields=s50%3Adesc&pageNum=1'.split('|'),0,{}));

var encode_version = 'sojson.v5', jezoh = '__0x3fb5e',  __0x3fb5e=['dcK9wotew5nCu2wvw6nCmsOvQcOONsOk','K8Kow4fDhzDDqwdh','UAATJSU=','wr8gw5HCqWw=','G8KzKhLDkA==','wrLDisOUw4HDiTTCnsKnwqHCg8O2w7XClg==','LmrDog4=','e8Ora13Dow==','wodfacKQw5o=','w74Sw5FreA==','wr94w6LDhMOgw4E=','wpkHw53DgsKKwrHDhcKbQ8Kpwp8=','dWPDons=','w7kbw7vDgMKb','w6DDkFFwwp/Cq3jCjUXDsW8=','TBIbBAfDtw==','wok5w7/ChDZV','wq3CvlzCtw==','wrHDsgzClQ==','IcORUmfDlcOPDsOSwr06fMKgBMKcTQ==','CgjDpSkw','w5oWw5vDhMKk','CcK4wpLDlEnCjnXClg==','w7zDhsKwTMOW','w7jDpFXCvcKm','wrTDlsOUw6rDtA==','w4bDn8KcXsOQVVHDkw==','bMOAwr3CsVzDksKTcAc=','wodAb8KKw4HCrDBoaA==','wrDDlMOUw5LDiQ==','5Lm26ICj5Yu/6ZmGw5zDgxHCnMOywpZDM8KD','VQPChSVsbsOvWMODRMOlwqBAWMKz','U8K8TsOnHsKOWMOpb11CwpjDkcOJZTTChAbCixvDtcO0wplFwoZdwrswWcOiwq1sJsOnw50VHhfDgwXDoMKmDBTClsOkJ1RBKkc3YzQYw4zDuEUgY0xEX8KXwrU=','wpZYQsKjw7Y=','wqLDiMOdw4nDiQ==','wpLCqMO8wpPCiQ==','w54Aw5bDqsKD','K23DsRErcg==','eETDt1Nj','w7XDhsOhwpfCrg==','LBMPdFk=','woXDmQ3Cu8Kl','eGrDrmxAdA==','bcKBwpPDmz3Clw==','KmzDghcL','w6vDu8K7MQY=','wr4+w6fCph0=','WsKSWMO7EQ==','WMKNwp7Dojg=','wosyw6rCnxhP','w7LDhcK8FTI=','wqDCuVPCoFbCgcOgbm3Dkw==','wq4Hw6HCoTDDlg==','TgxLwqPDtg==','wqXCoVfClmY=','wptsw7vDj8OB','wqVow4bDt8O5','QcOma8O2w4U=','D8Ohwo/DvjRK','wpZLX8Kyw5o=','NcKjDgPDjw==','E8K1RcO1w4U1','XA8YGy3DrMKqw49/w5A=','woctw4bChj0=','CMKXw6jDoA7Dmi1Ow4xUGMK4YMKwacO4SMKKc3ldwrQDw4RG'];(function(_0x5bc68b,_0x259158){var _0x102152=function(_0x1797a6){while(--_0x1797a6){_0x5bc68b['push'](_0x5bc68b['shift']());}};_0x102152(++_0x259158);}(__0x3fb5e,0x123));var _0x56ae=function(_0xca96c7,_0x241ea9){_0xca96c7=_0xca96c7-0x0;var _0x57cca1=__0x3fb5e[_0xca96c7];if(_0x56ae['initialized']===undefined){(function(){var _0x228394=typeof window!=='undefined'?window:typeof process==='object'&&typeof require==='function'&&typeof global==='object'?global:this;var _0x356c10='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';_0x228394['atob']||(_0x228394['atob']=function(_0x16460d){var _0x4e207e=String(_0x16460d)['replace'](/=+$/,'');for(var _0x15f638=0x0,_0x2abf93,_0x3df9f8,_0x479e2a=0x0,_0x411a0f='';_0x3df9f8=_0x4e207e['charAt'](_0x479e2a++);~_0x3df9f8&&(_0x2abf93=_0x15f638%0x4?_0x2abf93*0x40+_0x3df9f8:_0x3df9f8,_0x15f638++%0x4)?_0x411a0f+=String['fromCharCode'](0xff&_0x2abf93>>(-0x2*_0x15f638&0x6)):0x0){_0x3df9f8=_0x356c10['indexOf'](_0x3df9f8);}return _0x411a0f;});}());var _0x172d34=function(_0xa28d48,_0x346449){var _0x55c23f=[],_0x3809ab=0x0,_0x5298ee,_0x3c825f='',_0x8b8e9a='';_0xa28d48=atob(_0xa28d48);for(var _0xee1bef=0x0,_0x3023b5=_0xa28d48['length'];_0xee1bef<_0x3023b5;_0xee1bef++){_0x8b8e9a+='%'+('00'+_0xa28d48['charCodeAt'](_0xee1bef)['toString'](0x10))['slice'](-0x2);}_0xa28d48=decodeURIComponent(_0x8b8e9a);for(var _0x308939=0x0;_0x308939<0x100;_0x308939++){_0x55c23f[_0x308939]=_0x308939;}for(_0x308939=0x0;_0x308939<0x100;_0x308939++){_0x3809ab=(_0x3809ab+_0x55c23f[_0x308939]+_0x346449['charCodeAt'](_0x308939%_0x346449['length']))%0x100;_0x5298ee=_0x55c23f[_0x308939];_0x55c23f[_0x308939]=_0x55c23f[_0x3809ab];_0x55c23f[_0x3809ab]=_0x5298ee;}_0x308939=0x0;_0x3809ab=0x0;for(var _0x66c563=0x0;_0x66c563<_0xa28d48['length'];_0x66c563++){_0x308939=(_0x308939+0x1)%0x100;_0x3809ab=(_0x3809ab+_0x55c23f[_0x308939])%0x100;_0x5298ee=_0x55c23f[_0x308939];_0x55c23f[_0x308939]=_0x55c23f[_0x3809ab];_0x55c23f[_0x3809ab]=_0x5298ee;_0x3c825f+=String['fromCharCode'](_0xa28d48['charCodeAt'](_0x66c563)^_0x55c23f[(_0x55c23f[_0x308939]+_0x55c23f[_0x3809ab])%0x100]);}return _0x3c825f;};_0x56ae['rc4']=_0x172d34;_0x56ae['data']={};_0x56ae['initialized']=!![];}var _0x190c72=_0x56ae['data'][_0xca96c7];if(_0x190c72===undefined){if(_0x56ae['once']===undefined){_0x56ae['once']=!![];}_0x57cca1=_0x56ae['rc4'](_0x57cca1,_0x241ea9);_0x56ae['data'][_0xca96c7]=_0x57cca1;}else{_0x57cca1=_0x190c72;}return _0x57cca1;};function _0x412a72(_0x2a28c0){var _0x4257c9={'bwGZX':_0x56ae('0x0','jo5I'),'mGirf':function _0x2eb028(_0x5ab0bc,_0x5505f4){return _0x5ab0bc<_0x5505f4;},'hOkXt':function _0x16449b(_0x22286c,_0x41c8cd){return _0x22286c&_0x41c8cd;},'RJeYY':function _0x24beb6(_0x59303b,_0x576d3b){return _0x59303b==_0x576d3b;},'cFxMb':function _0x45b03c(_0xadce3d,_0x5416a9){return _0xadce3d>>_0x5416a9;},'spzgJ':function _0x3c313d(_0x19fd11,_0xcacabb){return _0x19fd11<<_0xcacabb;},'VdlKD':function _0x2427d5(_0x23b25b,_0x23b39e){return _0x23b25b&_0x23b39e;},'VDeWo':function _0x1ef1b0(_0x476993,_0x40dd2a){return _0x476993==_0x40dd2a;},'gHLRp':function _0x16afb3(_0x4bdebb,_0x1065a7){return _0x4bdebb>>_0x1065a7;},'biRta':function _0x301047(_0x2ada60,_0x1c4232){return _0x2ada60|_0x1c4232;},'oKMpY':function _0x1d0b02(_0x547e37,_0x500868){return _0x547e37<<_0x500868;},'HlUXJ':function _0x21902c(_0x16ae1a,_0x466bbf){return _0x16ae1a>>_0x466bbf;},'vuJTm':function _0x2fea95(_0x34f7b5,_0x59e46f){return _0x34f7b5<<_0x59e46f;},'lHuwG':function _0x1339d0(_0x3c775a,_0x3450ae){return _0x3c775a>>_0x3450ae;},'fpeDs':function _0x52b661(_0x318fc3,_0x59aa7b){return _0x318fc3&_0x59aa7b;},'HqwlU':function _0x2144ca(_0x4799d4,_0x25b745){return _0x4799d4|_0x25b745;},'nPBKx':function _0x42b833(_0xe339b1,_0x5c500c){return _0xe339b1&_0x5c500c;},'ZRhVT':function _0xc9529d(_0x5ed560,_0x4383da){return _0x5ed560&_0x4383da;},'bdZKt':_0x56ae('0x1','5jBa')};var _0x6c47cd=_0x4257c9[_0x56ae('0x2','LFWf')][_0x56ae('0x3','Q@8l')]('|'),_0x3a5836=0x0;while(!![]){switch(_0x6c47cd[_0x3a5836++]){case'0':_0x27d1f5='';continue;case'1':var _0x27d1f5,_0x4262d0,_0xc876d4;continue;case'2':_0x4262d0=0x0;continue;case'3':while(_0x4257c9[_0x56ae('0x4','*h#g')](_0x4262d0,_0xc876d4)){_0x5526a7=_0x4257c9[_0x56ae('0x5','a6w(')](_0x2a28c0['charCodeAt'](_0x4262d0++),0xff);if(_0x4257c9['RJeYY'](_0x4262d0,_0xc876d4)){_0x27d1f5+=_0x2097d8[_0x56ae('0x6',')Z%%')](_0x4257c9[_0x56ae('0x7','iAGA')](_0x5526a7,0x2));_0x27d1f5+=_0x2097d8['charAt'](_0x4257c9[_0x56ae('0x8','IM$w')](_0x4257c9[_0x56ae('0x9','Dk(l')](_0x5526a7,0x3),0x4));_0x27d1f5+='==';break;}_0x138cf5=_0x2a28c0['charCodeAt'](_0x4262d0++);if(_0x4257c9[_0x56ae('0xa','HLR(')](_0x4262d0,_0xc876d4)){_0x27d1f5+=_0x2097d8[_0x56ae('0xb','iAGA')](_0x4257c9['gHLRp'](_0x5526a7,0x2));_0x27d1f5+=_0x2097d8[_0x56ae('0xc','j%QO')](_0x4257c9[_0x56ae('0xd',')Z%%')](_0x4257c9[_0x56ae('0xe','L6ge')](_0x4257c9[_0x56ae('0xf','02EH')](_0x5526a7,0x3),0x4),_0x4257c9[_0x56ae('0x10','5jBa')](_0x4257c9[_0x56ae('0x11','j%QO')](_0x138cf5,0xf0),0x4)));_0x27d1f5+=_0x2097d8[_0x56ae('0x12','02EH')](_0x4257c9[_0x56ae('0x13','L6ge')](_0x4257c9['VdlKD'](_0x138cf5,0xf),0x2));_0x27d1f5+='=';break;}_0x4093e6=_0x2a28c0[_0x56ae('0x14','%FZJ')](_0x4262d0++);_0x27d1f5+=_0x2097d8[_0x56ae('0x15','d2rH')](_0x4257c9['lHuwG'](_0x5526a7,0x2));_0x27d1f5+=_0x2097d8['charAt'](_0x4257c9[_0x56ae('0x16','Zp5!')](_0x4257c9['VdlKD'](_0x5526a7,0x3)<<0x4,_0x4257c9[_0x56ae('0x17','%FZJ')](_0x138cf5,0xf0)>>0x4));_0x27d1f5+=_0x2097d8[_0x56ae('0x12','02EH')](_0x4257c9[_0x56ae('0x18','*FHt')](_0x4257c9[_0x56ae('0x19','*FHt')](_0x4257c9['nPBKx'](_0x138cf5,0xf),0x2),_0x4257c9[_0x56ae('0x1a','scqQ')](_0x4093e6,0xc0)>>0x6));_0x27d1f5+=_0x2097d8[_0x56ae('0x1b','eygr')](_0x4257c9['ZRhVT'](_0x4093e6,0x3f));}continue;case'4':return _0x27d1f5;case'5':_0xc876d4=_0x2a28c0['length'];continue;case'6':var _0x5526a7,_0x138cf5,_0x4093e6;continue;case'7':var _0x2097d8=_0x4257c9[_0x56ae('0x1c','LFWf')];continue;}break;}}function _0x344cd4(){var _0x53d9fc={'GjCbS':function _0x1a0314(_0x33da81,_0xe25eb5){return _0x33da81<_0xe25eb5;},'JBFUL':function _0x1af799(_0x51aa2f,_0x2e4887){return _0x51aa2f+_0x2e4887;}};var _0x3c9135=0x0;var _0x43beea=0x0;for(_0x43beea=0x0;_0x53d9fc[_0x56ae('0x1d','uGC9')](_0x43beea,wzwsquestion[_0x56ae('0x1e','V2r4')]);_0x43beea++){_0x3c9135+=wzwsquestion[_0x56ae('0x1f','!2cw')](_0x43beea);}_0x3c9135*=wzwsfactor;_0x3c9135+=0x1b207;return _0x53d9fc[_0x56ae('0x20','d2rH')](_0x56ae('0x21','Rau%'),_0x3c9135);}function _0x2ff265(_0x26b826,_0xea8bd1){var _0x253f74={'ogjLK':_0x56ae('0x22','Qy14'),'izgsL':'post','eMCME':function _0x3b581c(_0xd2391,_0x1a9ef1){return _0xd2391!=_0x1a9ef1;},'aCWaI':function _0x5c65fc(_0x1402c7,_0x41e446){return _0x1402c7<_0x41e446;},'OTFrl':_0x56ae('0x23','Rau%')};var _0x370b5e=_0x253f74[_0x56ae('0x24','!2cw')][_0x56ae('0x25','i[Ts')]('|'),_0x1ba457=0x0;while(!![]){switch(_0x370b5e[_0x1ba457++]){case'0':_0x15a9ed['method']=_0x253f74[_0x56ae('0x26','uGC9')];continue;case'1':return _0x15a9ed;case'2':var _0x15a9ed=document[_0x56ae('0x27','Q@8l')](_0x56ae('0x28',')Z%%'));continue;case'3':if(_0x253f74[_0x56ae('0x29','YXCs')](_0xea8bd1['search']('='),-0x1)){var _0x573df6=_0xea8bd1[_0x56ae('0x2a','LFWf')]('&');for(var _0x426cb4=0x0;_0x253f74[_0x56ae('0x2b','57vf')](_0x426cb4,_0x573df6[_0x56ae('0x2c','*FHt')]);_0x426cb4++){var _0x3ddbc7=_0x56ae('0x2d','V]Be')['split']('|'),_0x1fdb10=0x0;while(!![]){switch(_0x3ddbc7[_0x1fdb10++]){case'0':_0x2a293f[_0x56ae('0x2e','iAGA')]=_0x422f0a[0x0];continue;case'1':var _0x2a293f=document['createElement'](_0x253f74[_0x56ae('0x2f','a6w(')]);continue;case'2':var _0x422f0a=_0x8ad1c0['split']('=');continue;case'3':var _0x8ad1c0=_0x573df6[_0x426cb4];continue;case'4':_0x15a9ed[_0x56ae('0x30','WuNj')](_0x2a293f);continue;case'5':_0x2a293f['value']=_0x422f0a[0x1];continue;}break;}}}continue;case'4':_0x15a9ed[_0x56ae('0x31','!2cw')]();continue;case'5':_0x15a9ed[_0x56ae('0x32','02EH')]=_0x26b826;continue;case'6':_0x15a9ed['style']['display']=_0x56ae('0x33','%FZJ');continue;case'7':document[_0x56ae('0x34','HLR(')]['appendChild'](_0x15a9ed);continue;}break;}}function _0x33f22a(){var _0x532424={'hwQpj':function _0x3b4af9(_0x2ff2ab){return _0x2ff2ab();},'lYfvS':function _0x242f23(_0x57f673,_0x33b4b3){return _0x57f673(_0x33b4b3);},'VvOsr':function _0x33a26c(_0xb8a476,_0x580dd6){return _0xb8a476+_0x580dd6;},'vOmWg':_0x56ae('0x35','YXCs'),'LaaBO':function _0x1b637c(_0x5c57e1,_0x41b90a){return _0x5c57e1==_0x41b90a;},'eneJI':'post'};var _0xb14971=_0x532424[_0x56ae('0x36','jo5I')](_0x344cd4);var _0x10ace8=_0x532424[_0x56ae('0x37','a6w(')](_0x412a72,_0xb14971[_0x56ae('0x38','*8t[')]());var _0x35ace3=_0x532424[_0x56ae('0x39',')9A&')](dynamicurl,_0x532424[_0x56ae('0x3a','N&Yh')])+_0x10ace8;if(_0x532424['LaaBO'](wzwsmethod,_0x532424[_0x56ae('0x3b','Q@8l')])){_0x2ff265(_0x35ace3,wzwsparams);}else{window[_0x56ae('0x3c',')9A&')]=_0x35ace3;}}_0x33f22a();;if(!(typeof encode_version!==_0x56ae('0x3d','QE(m')&&encode_version===_0x56ae('0x3e','LFWf'))){window[_0x56ae('0x3f','Q@8l')](_0x56ae('0x40','YtnB'));};encode_version = 'sojson.v5';
</script>

</body>
</html>

```


2. 用浏览器打开这个文件，会发现会重定向到一个新的URL

如：http://localhost:63342/WZWSREL3dlYnNpdGUvcGFyc2UvcmVzdC5xNHc=?wzwschallenge=V1pXU19DT05GSVJNX1BSRUZJWF9MQUJFTDQxNjUyNzE=

因为是本地打开的，所以域名是`localhost:63342`

3. 把这个本地地址换成 `http://wenshu.court.gov.cn`这个后

神奇的事情发生了，可以获取到数据了。而且后面的请求也没返回这个 `html` 文件了。


#### 所以这次反爬解决方案

1. 在请求返回的地方增加一个判断，如果是 `html` 文件，那么就解析这个文件，获取新的URL，并重试，发送 `post` 请求即可。

2. 这个html怎么解析？？

~这个可以看看 @songguoxiong 的项目下的 [decrypt.py文件](https://github.com/songguoxiong/wenshu_utils/blob/master/wenshu_utils/old/wzws/decrypt.py)~

请看 `decrypt.py` 文件

⚠️ 注意 splash返回的cookie中，需要去除 `wzws_cid` 这个cookie