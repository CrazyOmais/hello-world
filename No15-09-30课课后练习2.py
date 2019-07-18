# 用户输入文件名以及开始搜索的路径，搜索该文件是否存在。
# 如果遇到文件夹，则进入文件夹继续搜索。
import os

def search_file(start_dir, target):
    os.chdir(start_dir)# 改变当前工作目录到指定目录

    for each_file in os.listdir(os.curdir):
        if each_file == target:
            print(os.getcwd() + os.sep + each_file) # os.sep其实就是'/'

        if os.path.isdir(each_file):# 如果当前指向文件夹(是目录)
            search_file(each_file, target) # 递归调用
            os.chdir(os.pardir) # 递归调用后返回上一级目录

start_dir = input('请输入要查找的初始目录：')
target = input('请输入要查找的目标文件：')
search_file(start_dir, target)

print('程序结束')
# 如果查找不到的话，没有任何提示，可以考虑采用字典或者字符串存储路径，如果程序结束字符串为空，打印未查找到文件
