#进制转换程序

while 1:
    num = input("请输入一个整数：")
    num = int(num)
    print(' 十进制 -> 十六进制 : %d -> 0x%x' % (num, num)) 
    print(' 十进制 -> 八进制 : %d -> 0o%o' % (num, num))
    print(' 十进制 -> 二进制 : %d -> ' % num, bin(num))
    
