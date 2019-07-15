def palindrome(string):
    list1 = list(string)
    list2 = reversed(list1)
    if list1 == list(list2):# 注意这里如果不加list()转换的话会出错，因为list2是一个“列表”类型，一定和list1不相等
        return '是回文联！'
    else:
        return '不是回文联！'
print(palindrome('上海自来水来自海上'))
