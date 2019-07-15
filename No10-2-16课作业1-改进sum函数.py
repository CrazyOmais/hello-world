# 自动无视参数里的字符串并返回正确的累加结果

def sum(x):
    result = 0

    for each in x:
        if(type(each)) == int) or (type(each) == float):
            result += each
        else:
            continue
    return result
