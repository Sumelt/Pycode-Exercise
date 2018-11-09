# @Author: Su
# @Date: 2018-11-09 17:13:24
# @Last Modified by:   Su
# @Last Modified time: 2018-11-09 17:13:24
# @Description: 打印PAT需要刷的题目，暂刷前两题

start = 1001
end = 1151
# 打印前两题


def printf(start, end):
    for inx in range(start, end+1, 4):
        print(inx, inx+1)


printf(start,  end)
