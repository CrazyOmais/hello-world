'''
将文件(record.txt)中的数据进行分割，并按照一下规律保存起来：
- 小甲鱼的对话单独保存为boy_*.txt的文件(去掉"小甲鱼：")
- 小客服的对话单独保存为girl_*.txt的文件(去掉"小客服：")
- 文件中共有三短对话，分别保存为boy_1.txt, girl_1.txt, boy_2.txt, girl_2.txt, boy_3.txt, girl_3.txt
共六个文件(文中不同的对话已经使用'======')分割
'''
f = open('record.txt')

boy = []
girl = []
count = 1

for each_line in f:
    if each_line[:6] != '======':
        # 进行字符串分割操作
        (role, line_spoken) = each_line.split(':',1)
        if role == '小甲鱼':
            boy.append(line_spoken)
        if role == '小客服':
            girl.append(line_spoken)
    else:
        # 进行文件的分别保存操作
        file_name_boy = 'boy_' + str(count) + '.txt'
        file_name_girl = 'girl_' + str(count) + '.txt'

        boy_file = open(file_name_boy, 'w')
        girl_file = open(file_name_girl, 'w')

        boy_file.writelines(boy)
        girl_file.writelines(girl)

        boy_file.close()
        girl_file.close()
        
        boy = []
        girl = []
        count += 1
        
# 进行文件的分别保存操作
file_name_boy = 'boy_' + str(count) + '.txt'
file_name_girl = 'girl_' + str(count) + '.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)

boy_file.close()
girl_file.close()
