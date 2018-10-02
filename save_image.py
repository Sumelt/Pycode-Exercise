# @Author: Su
# @Date: 2018-10-02 21:58:34
# @Last Modified by:   Su
# @Last Modified time: 2018-10-02 21:58:34
# @Description: 保存图片

import requests

url = 'https://pic1.zhimg.com/v2-5c6b2b8603fd593b0cc3db5735a4b88b_b.jpg'
r = requests.get(url)
if r.status_code ==200:
    with open('e:/MOOC/Python网络爬虫/beatiful.jpg', 'wb') as f:
        f.write(r.content)
    f.close()

