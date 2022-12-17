import heapq

f = open("day1_input.txt", "r")
lines = f.readlines()

curr_cal = 0
max_cal = 0
max_heap = []
for line in lines:
    if line == "\n":
        if curr_cal > max_cal:
            max_cal = curr_cal
        max_heap.append(-curr_cal)
        curr_cal = 0
    else:
        curr_cal += int(line)

print(max_cal)

heapq.heapify(max_heap)
first_cal = heapq.heappop(max_heap)
second_cal = heapq.heappop(max_heap)
third_cal = heapq.heappop(max_heap)
total_three = -first_cal + -second_cal + -third_cal
print(total_three)

f.close()