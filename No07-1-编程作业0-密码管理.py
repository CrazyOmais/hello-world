#密码管理

password = input("请设置密码(不含*)：")
while "*" in password:
    password = input("格式错误，请重输：")

count = 3
while count:
    count -= 1
    word = input("请输入密码：")
    if word == password:
        print("密码正确")
        break
    else:
        print("密码错误(剩余次数",count,"次)")
    
