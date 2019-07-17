# 编写一个程序，当用户输入文件名和行数(N)后，将该文件的前N行内容打印到屏幕上

def file_view(file_name, line_num):
    print('\n文件%s的前%d行内同如下：\n' % (file_name, line_num))
    f = open(file_name)
    for i in range(line_num):
        print(f.readline(),end='')

    f.close

# 主程序
file_name = input('请输入要打开的文件(工程目录下): ')
line_num = int(input('请输入需要显示前几行: '))
file_view(file_name, line_num)
