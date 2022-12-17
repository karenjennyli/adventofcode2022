from aocd import get_data

input = get_data(year=2022, day=5).splitlines()

# input = '''    [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2'''.splitlines()

STACKS = 0
EMPTY = 1
MOVES = 2
status = STACKS

num_stacks = (len(input[0]) + 1) // 4
stacks = [[] for _ in range(num_stacks)]

for line in input:
    if status == STACKS and '[' not in line:
        status = EMPTY
        stacks = [stack[::-1] for stack in stacks]
    elif status == EMPTY and line and line[0] == 'm':
        status = MOVES
    
    if status == STACKS:
        index = 0
        for i in range(1, len(line), 4):
            if line[i] != ' ':
                if index >= len(stacks):
                    stacks.append([])
                stacks[index].append(line[i])
            index += 1
    elif status == MOVES:
        count = int(line.split()[1])
        from_stack = int(line.split()[3]) - 1
        to_stack = int(line.split()[5]) - 1
        stacks[to_stack].extend(stacks[from_stack][-count:])
        stacks[from_stack] = stacks[from_stack][:-count]
        # for _ in range(count):
        #     stacks[to_stack].append(stacks[from_stack].pop())

for stack in stacks:
    print(stack[-1], end='')
print()