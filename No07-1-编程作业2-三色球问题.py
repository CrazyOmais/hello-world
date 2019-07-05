#三色球问题
red = 3
yellow = 3
green = 6

print("red\tyellow\tgreen")
while red:
    yellow = 3
    while yellow:
        green = 6
        while green:
            if red + yellow + green == 8:
                print(red,'\t',yellow,'\t',green)
            green -= 1
        yellow -= 1
    red -= 1
