# @Author: Su
# @Date: 2018-10-02 20:32:42
# @Last Modified by:   Su
# @Last Modified time: 2018-10-02 20:32:42
# @Description: 爬取京东iPhone XR MAX

import requests

def getHTMLText(url):  #爬虫框架
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[:500]
    except:
        return '产生异常'
       
url = 'https://item.jd.com/100000287145.html'
print(getHTMLText(url))

