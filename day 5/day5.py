from collections import deque

# import re

file = open('input.txt','r')


l =[]

#idea 1; read it like 2d array where each col is the stack

for num in file:
    if num[0] == " ":
        break
    num = num.strip('\n')
    num = num.replace("    ", " ")

    l.append(num.split(" "))

li = []
for i in range(len(l[0])):
    li.append(list())

#add colum by column starting from the edn
for c in range(len(l[0])):
    for r in range(len(l)):
        if l[r][c] != '':
            li[c].append(l[r][c])
    li[c].reverse() 



for line in file:
    if line[0] != 'm':
        continue
    line = line.strip('\n')
    code = line.split(' ')

    temp = []
    for j in range(int(code[1])):
        curr = li[int(code[3])-1].pop()
        temp.append(curr)

    
    
    temp.reverse()
    li[int(code[5])-1].extend(temp)


for l in li:
    print(l[-1])

print(li)




