import random

secret = random.randint(1, 10)

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
