#水仙花数
for i in range(100, 1000):
    num = i
    add = 0
    j = 3
    while j:
        add += (num % 10)**3
        num //= 10
        j -= 1
    if add == i:
        print(i)
        
