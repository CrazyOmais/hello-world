# 输入关键字，查找当前文件夹内所有含有该关键字的文本文件(.txt)
# 要求显示该文件所在位置以及关键字在文件中的具体位置

import os

def print_pos(key_dict):
    keys = key_dict.keys()
    keys = sorted(keys) # 对行数进行排序（因为字典是无序的）
    for each_key in keys:
        print('关键字出现在 %s 行， 第 %s 个位置。' % (each_key, key_dict[each_key]))

def pos_in_line(line, key):
    pos = []
    begin = line.find(key) # 在当前行查找关键字
    while begin != -1:
        pos.append(begin + 1) #从1计数
        begin = line.find(key, begin+1) # 从下一个位置继续查找，如果没有关键字啧返回-1，结束循环

    return pos

def search_in_file(file_name, key):
    f = open(file_name)
    count = 0 # 行数
    key_dict = dict() # 存放key所在具体行数对应具体位置

    for each_line in f:
        count += 1
        if key in each_line:
            pos = pos_in_line(each_line, key) # 查找key在每行对应的位置
            key_dict[count] = pos

    f.close()
    return key_dict

def search_files(key, detail):
    all_files = os.walk(os.getcwd()) # 记录目录中的文件名
    txt_files = [] # 存放所有.txt文件的路径

    for i in all_files:
        for each_file in i[2]:# 读出每一个文件的拓展名
            if os.path.splitext(each_file)[1] == '.txt':
                each_file = os.path.join(i[0],each_file) # 将多个路径组合后返回
                txt_files.append(each_file)

    for each_txt_file in txt_files:
        key_dict = search_in_file(each_txt_file, key) #查找关键字所在位置
        if key_dict:
            print('=======================================================')
            print('在文件 %s 中找到关键字 %s '% (each_txt_file, key))
            if detail in ['Y','y']:
                print_pos(key_dict)

key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
detail = input('请问是否需要打印关键字 %s 在文件中的具体位置(Y/N)'% key)

search_files(key,detail)

print('程序结束')
