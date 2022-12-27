file = open("input.txt", "r")

string = ''
for l in file:
    string = l

left = 0
right   =14

curr =[string[i] for i in range(0,4)]

for i in range(right, len(string)):
    if len(set(string[left:i]))  == 14: 
        print(set(string[left:i]))
        print(i)
        break
    left +=1


print(len(string))