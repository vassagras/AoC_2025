import time
import os

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 05"), 'r')

count_1 = 0
count_2 = 0
ingredients_ids = set()
ranges = []

# Read input data
flag = False
for l in file.readlines():
    if l == "\n":
        flag = True
        continue

    if flag:
        ingredients_ids.add(int(l.strip()))
    else:
        ranges.append([int(e) for e in l.strip().split("-")])

# for each ingredient check if it is contained within the existing ranges, if so stop further search
for ingredient in ingredients_ids:
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            count_1 += 1
            break

# Sort ranges by start value
ranges = sorted(ranges, key=lambda x: x[0])

merged_ranges = []
current_start, current_end = ranges[0]
for start, end in ranges[1:]:
    if start > current_end:
        merged_ranges.append([current_start, current_end])
        current_start, current_end = start, end
    else:
        # In case of overlap, then extend the end
        current_end = max(current_end, end)

# Add final range and count
merged_ranges.append([current_start, current_end])
count_2 = sum(end - start + 1 for start, end in merged_ranges)

end_p1 = time.time()

print("Part 1 result: {}".format(count_1))
print("Part 2 result: {}".format(count_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()