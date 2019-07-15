'''
题目要求：
如果一个三位数等于齐各位数字的立方和，则这个数为水仙花数
编写一个程序，找出所有的水仙花数
'''

def Narcissus():
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp % 10) ** 3
            temp = temp // 10

        if sum == each:
            print(each, end='\t')

print("所有的水仙花数分别是：", end='')

Narcissus()
