#计算打印所有参数和乘以基数(base=3)的结果
#如果参数中最后一个参数为5,则设定基数为5，基数不参与求和计算
#参考答案的第二个条件是：如果参数中最后一个参数为(base=5),则设定基数为5，基数不参与求和计算
#故没有元组转列表这一操作

def Fun1(*Param, base = 3):
    result = 0
    param = list(Param)
    if param[len(param)-1] == 5:
        base = param.pop()
    for each in param:
        result += each

    result *= base

    print('result = ',result)

Fun1(1,2,3,5,4)
Fun1(1,2,3,4,5)

'''
参考答案
def mFun(*param, base=3):
    result = 0
    for each in param:
        result += each

    result *= base

    print('结果是：',result)

mFun(1,2,3,4,5, base=5)
'''
