def Dec2Bin(dec):
    m = dec
    temp = []
    while m:
        r = m%2
        m = m//2
        temp.append(r)

    result = ''
    while temp:
        result += str(temp.pop())
    return result

print(Dec2Bin(11))
