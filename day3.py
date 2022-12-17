from aocd import get_data
import string

input = get_data(year=2022, day=3).splitlines()

# input = '''vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw'''.splitlines()

sum_priority = 0

for i in range(0, len(input), 3):
    first = input[i]
    second = input[i + 1]
    third = input[i + 2]
    common = list(set(first).intersection(set(second)).intersection(set(third)))[0]
    sum_priority += string.ascii_letters.index(common) + 1

print(sum_priority)