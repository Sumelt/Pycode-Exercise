# @Author: Su
# @Date: 2018-10-02 22:32:42
# @Last Modified by:   Su
# @Last Modified time: 2018-10-02 22:32:42
# @Description: 地址查询

import requests

url = 'http://m.ip138.com/ip.asp'
key = 'www.baidu.com'
addres = {'ip':key}
r = requests.get(url, params=addres)
if r.status_code==200:
    print(r.request.url)
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
else:
    print('产生异常，查询失败')