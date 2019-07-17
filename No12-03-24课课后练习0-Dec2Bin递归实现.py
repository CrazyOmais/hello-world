def Dec2Bin(dec):
    result = ''

    if dec: # 当被除数不为0时，记录除以2的余数，并将商再一次计算
        result = Dec2Bin(dec//2)
        return result + str(dec%2)
    else:   # 当被除数为0时，返回字符串（二进制结果）
        return result

print(Dec2Bin(62))
