# 写一个函数get_digits(n), 将参数n分解出每个位的数字并按照顺序放到列表中

result = []

def get_digits(n):
    if n > 0:
        result.insert(0, n%10)
        get_digits(n//10)

get_digits(12345)
print(result)
