from aocd import get_data
input = get_data(year=2022, day=7).splitlines()
# input = '''$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k'''.splitlines()

total_size = 0
stack = []
cd_tree = {}
sizes = {}

for line in input:
    if line == '$ cd ..':
        curr_path = '/'.join(stack)
        cd_size = sizes.get(curr_path, 0)
        stack.pop()
        new_path = '/'.join(stack)
        sizes[new_path] += cd_size
    elif line.startswith('$ cd '):
        stack.append(line[5:])
        path = '/'.join(stack)
        if path not in sizes:
            sizes[path] = 0
    elif line[0].isnumeric():
        size = int(line.split()[0])
        path = '/'.join(stack)
        sizes[path] += size

while len(stack) > 1:
    path = '/'.join(stack)
    cd_size = sizes.get(path)
    stack.pop()
    path = '/'.join(stack)
    sizes[path] += cd_size

for path in sizes:
    if sizes[path] <= 100000:
        total_size += sizes[path]

print(total_size)

unused = 70000000 - sizes['/']
must_delete = 30000000 - unused

potential_deletes = []
for dir in sizes:
    if sizes[dir] >= must_delete:
        potential_deletes.append(sizes[dir])

print(min(potential_deletes))