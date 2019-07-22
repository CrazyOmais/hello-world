print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1：查询联系人资料  ---|')
print('|--- 2：插入新的联系人  ---|')
print('|--- 3：删除已有联系人  ---|')
print('|--- 4：退出通讯录程序  ---|')

contacts = dict()

while 1:
    try:
        instr = int(input('\n请输入相关的指令代码：'))
    except ValueError:
        instr = int(input('指令代码有误，请重新输入：'))

    if instr == 1:
        name = input('请输入联系人姓名：')
        try:
            print(name + '：'+ contacts[name])
        except KeyError:
            print('您输入的姓名不在通讯录中！')

    if instr == 2:
        name = input('请输入联系人姓名：')
        try:
            print('您输入的姓名在通讯录中已存在 -->> ', end='')
            print(name + '：' + contacts[name])
            if input('是否修改用户资料(Y/N)：') == 'Y':
                contacts[name] = input('请输入用户联系电话：')
        except KeyError:
            contacts[name] = input('请输入用户联系电话：')
    if instr == 3:
        name = input('请输入联系人姓名：')
        try:
            del(contacts[name]) # 也可以用dict.pop()
        except KeyError:
            print('您输入的联系人不存在。')
    if instr == 4:
        break

print('|--- 感谢使用通讯录程序  ---|')
