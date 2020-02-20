import base64
import re
import urlparse as parse


_pattern = re.compile(r"dynamicurl\|(?P<path>.+?)\|wzwsquestion\|(?P<question>.+?)\|wzwsfactor\|(?P<factor>\d+)")


def decrypt_wzws(text):
    # noinspection PyBroadException
    try:
        return _decrypt_by_python(text)
    except Exception:
        pass
        # return _decrypt_by_nodejs(text)
        

def _decrypt_by_python(text):
    base_url = "http://wenshu.court.gov.cn"

    group_dict = _pattern.search(text).groupdict()
    question = group_dict["question"]
    factor = int(group_dict["factor"])
    path = group_dict["path"]

    label = "WZWS_CONFIRM_PREFIX_LABEL{}".format(sum(ord(i) for i in question) * factor + 111111)
    challenge = base64.b64encode(label.encode()).decode()

    dynamic_url = parse.urljoin(base_url, path)
    dynamic_url = "{url}?{query}".format(url=dynamic_url, query="wzwschallenge={}".format(challenge))
    return dynamic_url
    
   
if __name__ == "__main__":
    with open("test.html") as f:
    _content = f.read()

    _resp = decrypt_wzws(_content)

    print _resp
