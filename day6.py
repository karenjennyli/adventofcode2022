from aocd import get_data

input = get_data(year=2022, day=6)
# input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'

for i in range(len(input) - 4):
    curr_set = set(input[i:i+4])
    if len(curr_set) == 4:
        print(i + 4)
        break

for i in range(len(input) - 14):
    curr_set = set(input[i:i+14])
    if len(curr_set) == 14:
        print(i + 14)
        break