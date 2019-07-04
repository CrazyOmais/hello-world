#判断平年闰年程序
year = input("请输入年份：")
if not year.isdigit():
    year = input("输入格式不合法，请重新输入：")
num = int(year)
if (num % 400 == 0) or (num % 100 != 0 and num % 4 == 0 ):
    print(year+"是平闰年！")
else:
    print(year+"是平年！")
