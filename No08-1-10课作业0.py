member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
#方法一
member.insert(1, 88)
member.insert(3, 90)
member.insert(5, 85)
member.insert(7, 90)
member.append(88)
print(member)



member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']
#方法二
member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]
print(member)
