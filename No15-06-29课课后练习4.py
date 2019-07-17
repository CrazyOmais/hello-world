# 实现文本"全部替换"功能

def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read:
        if rep_word in eachline:
            count += eachline.count(rep_word)
            eachline = eachline.replace(rep_word, new_word)# 这里没有改变原本的文本
        content.append(eachline)

    decide = input('\n文件 %s 中共有 %s 个"%s"\n确定把所有的"%s"替换为"%s"吗？\n【Yes/No】：'\
                   %(file_name, count, rep_word, rep_word, new_word))
    if decide in ['YES','Yes', 'yes']:
        f_write = open(file_name, 'w') # 区分只读和可写程序，保护数据
        f_write.writelines(content) # 这里才改写了文本
        f_write.close()

    f_read.close()

# main
file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)
