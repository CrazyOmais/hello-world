#判断回文联
def test(string):
    length = len(string)
    last = length - 1
    s = length // 2
    for each in range(s):
        if string[each] != string[last]:
            return 0
        last -= 1
    return 1

string = input("请输入一句话：")
if test(string) == 1:
    print('是回文联')
else:
    print("不是回文联")
