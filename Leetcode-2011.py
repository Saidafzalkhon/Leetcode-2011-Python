operations = input().split()
son = 0
for i in operations:
    if i[1] == '-' or i[-1] == '-':
        son-=1
    else: son+=1
print(son)