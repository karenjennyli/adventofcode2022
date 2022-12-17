from aocd import get_data

input = get_data(year=2022, day=4).splitlines()

# input = '''2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8'''.splitlines()

count = 0
some_overlap = 0

for line in input:
    start0, end0 = line.split(",")[0].split("-")
    start1, end1 = line.split(",")[1].split("-")
    start0 = int(start0)
    end0 = int(end0)
    start1 = int(start1)
    end1 = int(end1)
    if start0 <= start1 <= end0 and start0 <= end1 <= end0:
        count += 1
    elif start1 <= start0 <= end1 and start1 <= end0 <= end1:
        count += 1
    
    if start0 <= start1 <= end0 or start0 <= end1 <= end0 or start1 <= start0 <= end1 or start1 <= end0 <= end1:
        some_overlap += 1

print(count)
print(some_overlap)