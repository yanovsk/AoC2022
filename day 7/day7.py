#part a
lines = []
dir_sizes = {}

#only add cd commands and files
for i in open("input.txt", 'r').read().split('\n'):
    i = i.replace("$ ", "")
    if i[0:2] != "ls" and i[0:3] != "dir":
        lines.append(i)
    
s=[]

for i in range(len(lines)):
    line = lines[i]
    if line[0:2] == "cd" and ".." in line:
        s.pop()
    elif line[0:2] == "cd":
        s.append(i)
        dir_sizes[i] =0
    else:
        size = int(line.split(" ")[0])
        for s in s:
            dir_sizes[s] += size

#part b
total_sizes = [dir_sizes[i] for i in dir_sizes if dir_sizes[i]]
space_needed = 70000000 - total_sizes[0] 

dir_to_delete = [i for i in total_sizes if i >= 30000000-space_needed]
print(min(dir_to_delete))