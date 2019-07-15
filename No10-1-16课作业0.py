def min(x):
    least = x[0]

    for each in x:
        if each < least:
            least = each

    return least

print(min('123456789'))

# 该函数的作用是遍历数组x并返回数组中的最小值
