# 查找输入路径下所有的视频格式文件，并创建一个文件（vedioList.txt）存放所有找到的文件路径

import os

def search_file(start_dir, target):
    os.chdir(start_dir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd() + os.sep + each_file + os.linesep)

        if os.path.isdir(each_file):
            search_file(each_file,target) # 递归
            os.chdir(os.pardir)

start_dir = input('请输入待查找的初始目录：')
program_dir = os.getcwd()

target = ['.mp4', '.avi', '.rmvb', '.mkv']
vedio_list = []
search_file(start_dir, target)

f = open(program_dir + os.sep + 'vedioList.txt', 'w')

for each in vedio_list:
    f.write(each)

# f.write(vedio_list)
f.close()

print('程序结束')
