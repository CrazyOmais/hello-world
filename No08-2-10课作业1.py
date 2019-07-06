member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
for i in member:
    print(i)
#方法1
count = 0
length = len(member)
while count < length:
    print(member[count],member[count + 1])
    count += 2

#方法2
length = len(member)
for each in member:
   if member.index(each) % 2 == 0 and member.index(each) < length:
       print(member[member.index(each)], member[member.index(each)+1])
        #print(member.index(each), member.index(each + 1))
#在语句 print(member.index[each], member[member.index(each)+1])中
#member.index(each)可以写成member.index[each)]
#但是！
#member[member.index(each)]不可以写成member(member.index(each))
