# @Author: Su
# @Date: 2018-10-02 21:15:29
# @Last Modified by:   Su
# @Last Modified time: 2018-10-02 21:15:29
# @Description:  py提交关键词搜索

import requests

def getHTMLText(url, keyword):  #爬虫框架
    try:
        kv = {'ie' : 'UTF-8', 'wd' : keyword}
        r = requests.get(url, params=kv)
        print(r.request.url)
        r.raise_for_status()
        #r.encoding = r.apparent_encoding    
        return r.text
    except:
        print(r.status_code)
        return '产生异常'
       
url = 'https://www.baidu.com/s'
print(getHTMLText(url, 'baidu'))
