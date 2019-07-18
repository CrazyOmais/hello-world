# 统计当前目录下每个文件类型的文件数

import os

all_files = os.listdir(os.curdir) # 使用os.curdir表示当前目录
type_dict = dict()

for each_file in all_files:
    if os.path.isdir(each_file):# 判断当前指向的是文件夹还是文件（isdir()判断当前路径是否为目录，如果是文件夹的话，没有拓展名，可以作为下一级目录）
        # 如果是文件夹，新建键'文件夹'，初值为0（第一次发现文件夹），然后累加
        type_dict.setdefault('文件夹', 0) 
        type_dict['文件夹'] += 1
        # 这么做有一个缺点，就是如果子文件夹下还有文件的话，就无法检测出来
    else:
        ext = os.path.splitext(each_file)[1]# splitext分割文件名和拓展名
                                            #如果用split()的话输出就没有'.'
        type_dict.setdefault(ext, 0)
        type_dict[ext] += 1

for each_type in type_dict.keys():
    print('该文件夹下共有类型为 %s 的文件 %d 个' % (each_type, type_dict[each_type]))

print(type_dict)

    
