
def new_account():
    while 1:
        name = input('请输入用户名: ')
        if name in user_data:
            print('用户名已被使用，请重新输入! ')
            continue
        else:
            passwd = input('请输入密码: ')
            user_data[name] = passwd
            print('注册成功！')
            break

def old_account():
    while 1:
        name = input('请输入用户名: ')
        if name not in user_data:
            print('用户名不存在，请重试')
            continue
        else:
            passwd = input('请输入密码: ')
            if passwd == user_data.get(name):
                print('登陆成功！')
                break
            else:
                print('密码错误！')

def show_menu():
    while 1:
        print('|--- 新建用户: N/n ---|\n|--- 登陆账号: E/e ---|\n|--- 退出程序: Q/q ---|')
        temp = input('\n|--- 请输入指令代码: ')
        if temp == 'q' or temp == 'Q':
            break
        elif temp == 'n' or temp == 'N':
            new_account()
        elif temp == 'e' or temp == 'E':
            old_account()
        else:
            print('指令有误，请重新输入！')

# main function:
user_data = dict()
show_menu()

print('|--- 欢迎使用本程序 ---|')
    
