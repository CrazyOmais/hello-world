# 成绩统计

while 1:

    temp = input("请输入成绩：")
    while not temp.isdigit():
        temp = input("输入不合法，请重新输入：")

    grade = int(temp)
    while not 0 <= grade <= 100:
        temp = input("成绩有误，请重新输入：")
        grade = int(temp)
    if 60 < grade <= 80:
        print("C")
    else :
        if 90 < grade <= 80:
            print("B")
        else :
            if 90 <= grade <= 100:
                print("A")
            else:
                print("D")
        
