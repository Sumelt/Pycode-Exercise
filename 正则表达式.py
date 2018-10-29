# @Author: Su
# @Date: 2018-10-29 19:38:37
# @Last Modified by:   Su
# @Last Modified time: 2018-10-29 19:38:37
# @Description: 练习邮箱正则表达式

""" 
测试用例
bill.gates@microsoft.com
bob#example.com
mr-bob@example.com
"""

import re

def JudgeEmailDress(text):
    m = re.match(r'^([a-zA-Z/./-]+)(\@|\#)(\w+)\.com$', text)
    if m:
        print('EmailDress: OK')
        print("UserName: ", m.group(1))
    else:
        print("EmailDress: NO")

text = 'bob#example.com'
JudgeEmailDress(text)

