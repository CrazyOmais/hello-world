try:
    with open ('data.txt', 'w') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦：'+ str(reason))

# 如果采用 f = open('data.txt', 'w')语句的话，后面还需要加上finally语句：
'''
finally:
    f.close
'''
