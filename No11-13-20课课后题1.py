str1 = '''字符串
QWFlDWE
23d23
OIUoDNU
xs3ed3dDWd
WDJvOKL0
EIJeNJL'''
countA = 0 # 记录遍历到的小写字母之前的大写字母数量
countB = 0 # 记录当前位置是在待定密码之前还是之后，之前B == 0，之后B == 1
countC = 0 # 记录遍历到的小写字母之后的大写字母数量
length = len(str1)

for i in range(length):
    if str1[i] == '\n' and countC != 3: # 考虑到换行前后的判断
        countA = 0
        countB = 0
        countC = 0
        continue
    if str1[i].isupper():
        if countB == 1:
            countC += 1
            countA = 0
        else:
            countA += 1
        continue
    if str1[i].islower() and countA == 3:
        countB = 1
        countA = 0
        target = i
        continue
    if (not str1[i].isupper()) and countC == 3: # 考虑到密码之后的三位大写字母再往后不是字母
        print(str1[target],end = '')
    counrA = 0
    countB = 0
    countC = 0
if countC == 3:# 防止密码出现在倒数第四位
    print(str1[target],end = '')
