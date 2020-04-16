import re
import base64

from urllib.parse import urljoin


_pattern = re.compile(r"dynamicurl\|(?P<path>.+?)\|wzwsquestion\|(?P<question>.+?)\|wzwsfactor\|(?P<factor>\d+)")


def decrypt_wzws(text: str) -> str:
    # noinspection PyBroadException
    try:
        return _decrypt_by_python(text)
    except Exception:
        print("解析html错误")


def _decrypt_by_python(text: str) -> str:
    base_url = "http://wenshu.court.gov.cn"

    group_dict = _pattern.search(text).groupdict()
    question = group_dict["question"]
    factor = int(group_dict["factor"])
    path = group_dict["path"]

    label = "WZWS_CONFIRM_PREFIX_LABEL{}".format(sum(ord(i) for i in question) * factor + 111111)
    challenge = base64.b64encode(label.encode()).decode()

    dynamic_url = urljoin(base_url, path)
    dynamic_url = "{url}?{query}".format(url=dynamic_url, query="wzwschallenge={}".format(challenge))
    return dynamic_url
    
   
if __name__ == "__main__":
    with open("demo.html") as f:
        _content = f.read()
    _resp = decrypt_wzws(_content)
    print(_resp)
