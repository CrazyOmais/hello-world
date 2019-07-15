# 编写一个函数findstr()，该函数统计一个长度为2的子字符串在另一个字符串中出现的次数。

def findstr(desStr, subStr):
    count = 0
    length = len(desStr)
    if subStr not in desStr:
        print('目标字符串中未找到字符串！')
    else:
        for each1 in range(length - 1):
            if desStr[each1] == subStr[0]:
                if desStr[each1+1] == subStr[1]:
                    count += 1

        print('子字符串在目标字符串中出现 %d 次'% count)

desStr = input('请输入目标字符串')
subStr = input('请输入子字符串（两个字符）：')

findstr(desStr,subStr)
