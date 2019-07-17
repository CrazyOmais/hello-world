print('|---欢迎进入通讯录程序---|\n|---1: 查询联系人资料 ---|\n|---2: 插入新的联系人 ---|\n|---3: 删除已有联系人 ---|\n|---4: 退出通讯录程序 ---|')

contacts = dict()
while 1:
    temp = input('\n请输入相关指令代码: ')

    if temp == '1':
        print('\n|---1: 查询联系人资料 ---|')
        name = input('请输入联系人姓名:')
        if name in contacts:
            print(name + ': '+ contacts[name])
        else:
            print('该联系人不在通讯录中！')

    elif temp == '2':
        print('\n|---2: 插入新的联系人 ---|')
        name = input('请输入联系人姓名: ')
        if name in contacts:
            print('该联系人已存在 -->> ',end='')
            print(name + ': ' + contacts[name])
        else:
            contacts[name] = input('请输入该联系人电话: ')
    elif temp == '3':
        print('\n|---3: 删除已有联系人 ---|')
        name == input('请输入联系人姓名: ')
        if name in contacts:
            del(contacts[name])
            print("联系人%s已删除！"% name)
        else:
            print('该联系人不存在！')
    elif temp == '4':
        break
    else:
        print('输入指令有误！')

print('\n|---感谢使用通讯录程序 ---|')
