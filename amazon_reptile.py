# @Author: Su
# @Date: 2018-10-02 21:01:17
# @Last Modified by:   Su
# @Last Modified time: 2018-10-02 21:01:17
# @Description: 爬取亚马逊

import requests

def getHTMLText(url):
    try:
        kv = {'user - agent':'chrome/10'} 
        r = requests.get(url, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.headers.get('Date')
    except:
        print(r.status_code)
        return '产生异常'

url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
print(getHTMLText(url))