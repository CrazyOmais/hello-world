# 编写一个程序，接受用户的输入并保存为新的文件

'''
print('==================== RESTART ====================')
file_name = input("请输入文件名: ")
print('请输入内容(单独输入":w"保存退出)')
f = open(file_name, 'w')
while 1:
    write_some = input()
    if write_some != ':w':
        f.write('%s\n' % write_some)
    else:
        break

f.close()
'''

# 优化之后：
def file_write(file_name):
    f = open(file_name, 'w')
    print('请输入内容(单独输入":w"保存退出)')
    
    while 1:
        write_some = input()
        if write_some != ':w':
            f.write('%s\n' % write_some)
        else:
            break

    f.close()

file_name = input('请输入文件名: ')
file_write(file_name)

