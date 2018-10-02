# @Author: Su
# @Date: 2018-10-02 15:56:28
# @Last Modified by:   Su
# @Last Modified time: 2018-10-02 15:56:28
# @Description:  爬虫框架+ requests库的测试

import requests

def urlInfo(r):
    print('URL head:', r.headers)
    print('Coding:', r.encoding)
    
def myurl(r):
    if r.status_code == 200:
        urlInfo(r)
        print('---Successful connet!---')
        if r.encoding == 'ISO-8859-1':
            r.encoding = r.apparent_encoding
        print(r.text[:500])        
    else:
        print('Faile connet!')

def getHTMLText(url):  #爬虫框架
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'


url = "http://www.baidu.com"
r = requests.get(url)
myurl(r)
