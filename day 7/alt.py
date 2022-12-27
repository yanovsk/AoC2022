from collections import defaultdict
class Dir:
    def __init__(self, name):
        self.name = name
        self.size = 0
        self.parent = None

    def set_size(self, size):
        self.size += size
    def set_parent(self, parent):
        self.parent = parent    
    def get_parent(self):
        return self.parent
    def get_size(self):
        return self.size
    def get_name(self):
        return self.name


class FileSys:
    def __init__(self):
        self.dirs = []

    def add_directory(self, dir_obj):
        self.dirs.append(dir_obj)

    def get_directory(self, dir_name):
        for d in self.dirs:
            if dir_name == d.get_name():
                return d
        return None

    def add_dir_parent(self, dir_obj, dir_parent):
        dir_obj.set_parent(dir_parent)

    def get_dir_parent(self, dir_obj):
        return dir_obj.get_parent()

    def size(self):
        tot = []
        for i in self.dirs:
            if i.get_size() <= 100000:
                tot.append(i.get_size())
        return tot

file = open('input.txt','r')
sys = FileSys()
root = Dir('/')
sys.add_directory(root)

j=0
for line in file:
    j+=1
    line = line.strip()
    code = line.split(' ')

    if code[0] != '$' and write_mode:
        if code[0] == 'dir':
            new_dir = Dir(code[1])
            new_dir.set_parent(curr_dir)
            sys.add_directory(new_dir)

        elif code[0] != 'dir':
            curr_dir.set_size(int(code[0]))
            if curr_dir.get_parent():
                parent = curr_dir.get_parent()
                parent.set_size(int(code[0]))

    if code[0] == '$':
        write_mode = False

        if code[1] == 'ls':
            write_mode = True
        elif code[1]=='cd' and code[2] != '..':
            curr_dir = sys.get_directory(code[2])
        elif code[1] == 'cd' and code[2] == '/':
            curr_dir = root
        elif code[1]=='cd' and code[2] == '..':
            if curr_dir.get_parent():
                curr_dir = curr_dir.get_parent()


print(sum(sys.size()))