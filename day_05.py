import time
import os

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 05"), 'r')

count_1 = 0
count_2 = 0
ingredients_ids = set()
ranges = []

flag = False
for l in file.readlines():
    if l == "\n":
        flag = True
        continue

    if flag:
        ingredients_ids.add(int(l.strip()))
    else:
        ranges.append([int(e) for e in l.strip().split("-")])

for ingredient in ingredients_ids:
    for r in ranges:
        if r[0] <= ingredient <= r[1]:
            count_1 += 1
            break

end_p1 = time.time()

print("Part 1 result: {}".format(count_1))
print("Part 2 result: {}".format(count_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()