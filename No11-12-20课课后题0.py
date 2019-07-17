
str1 = ''' ygvv bi i iu
hi iu uyg98y7 hbiujh vrxetwzt43rs
h9hb879767r8c6'''
list1 = []

for each in str1:
    if each not in list1:
        if each == '\n':
            print('\\n', str1.count(each))
        else:
            print(each, str1.count(each))
        list1.append (each)
