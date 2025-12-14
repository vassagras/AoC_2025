import time
import os

start_time = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 01"), 'r')

dial_position = 50
count_zeros = 0

print("The dial starts by pointing at {}".format(dial_position))
for line in file:
    op = line[:1]
    rotations = int(line[1:].strip())

    if op == "L":
        dial_position = (dial_position - rotations) % 100
    elif op == "R":
        dial_position = (dial_position + rotations) % 100

    if dial_position == 0: count_zeros += 1
    print("The dial is rotated {} to point at {}".format(line.strip(), dial_position))

end_time = time.time()

print("Part 1 result: {}".format(count_zeros))
print("Part 2 result: {}".format(0))
print("The time of execution of above program is :", (end_time - start_time) * 10**3, "ms")
print()