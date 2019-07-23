import random
import easygui as g

g.msgbox('欢迎进入猜数字小游戏！')
secret = random.randint(1, 10)

msg = '不妨猜一下我现在心里想的是哪个数字？'
title = '猜数字小游戏'
guess = g.integerbox(msg, title, lowerbound = 1, upperbound = 10)

while True:
    if guess == secret:
        g.msgbox('卧槽，你是我肚子里的蛔虫吗！')
        g.msgbox('哼，猜中了也没有奖励！')
        break
    elif guess > secret:
        g.msgbox('哥，大了大了~~~')
    else:
        g.msgbox('嘿，小了小了~~~')
    guess = g.integerbox(msg, title, lowerbound = 1, upperbound = 10)

g.msgbox = ('游戏结束，不玩啦！')

# 以下是上一版本的代码
'''
try:
    temp = input('猜猜我现在心里想的是哪个数字？')
    guess = int(temp)
except(ValueError, EOFError, KeyboardInterrupt):
    print('输入错误！')
    guess = secret
while guess != secret:
    temp = input('猜错了，请重新输入吧：')
    try:
        guess = int(temp)
    except(ValueError, EOFError, KeyboardInterrupt):
        print('输入错误！')
        break
    if guess == secret:
        print('哼，猜中了也没有奖励！')
    else:
        if guess > secret:
            print('大了大了~')
        else:
            print('小了小了！')
print('游戏结束，不玩啦')
'''
