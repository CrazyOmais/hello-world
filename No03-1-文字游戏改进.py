import random
secret = random.randint( 1 , 10 )
print('---------------python学习 程序1-------------------\n')
print('-------------------文字游戏-----------------------\n')
temp = input("不妨猜一下我在想哪个数字？")
guess=int(temp)
i = 0
if guess == secret:
    print("牛逼，第一次就猜中了！")
    print("哼，猜中了也没有奖励！")
else:
    if guess > secret:
        print("哥，大了大了~~~")
    else:
         print("嘿，小了小了！！")
while guess!=secret and i < 2 :
    temp = input("哎呀，猜错了，请重新输入吧：")
    guess=int(temp)
    if guess==secret:
        print("你是我肚子里的蛔虫嘛？！")
        print("哼，猜中了也没有奖励！")
    else:
        if guess>secret:
            print("哥，大了大了~~~")
        else:
            print("嘿，小了小了！！")
    i = i + 1 
print("游戏结束，不玩啦")
