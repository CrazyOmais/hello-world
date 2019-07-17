num1 = [1, 2, 3, 4, 5, 5, 3, 1, 0]
temp = []
for each in num1:
    if each not in temp:
        temp.append(each)

print(temp)
