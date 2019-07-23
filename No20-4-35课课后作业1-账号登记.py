import easygui as g

msg = '请填写以下联系方式'
title = '账号中心'
fieldNames = ['*用户名', '*真实姓名', ' 固定电话', '*手机号码',' QQ', '*E-mail']
fieldValued = []
fieldValues = g.multenterbox(msg, title, fieldNames)

while 1:
    if fieldValues == None:
        break
    errmsg = ''
    for i in range(len(fieldNames)):
        option = fieldNames[i].strip() #  strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
                            # 返回值是去除的值
        if fieldValues[i].strip() == '' and option[0] == '*':
            errmsg += ('【%s】为必填项。\n\n'% fieldNames[i])
    if errmsg == '':
        break
    fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)

print('用户资料如下：%s'% str(fieldValues))
