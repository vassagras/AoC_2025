import time
import os

start_time = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 01"), 'r')

dial_position = 50
count_of_zero_dials = 0
count_zero_passes = 0

print("The dial starts by pointing at {}".format(dial_position))
for line in file:
    op = line[0]
    rotations = int(line[1:].strip())

    zero_passes = 0
    new_position = 0

    if op == "R":
        new_position = (dial_position + rotations) % 100
        zero_passes = (dial_position + rotations) // 100
    elif op == "L":
        new_position = (dial_position - rotations) % 100
        zero_passes = (rotations - dial_position - 1) // 100 + 1 if rotations >= dial_position else 0

    count_zero_passes += zero_passes
    dial_position = new_position

    if dial_position == 0: count_of_zero_dials += 1
    print("The dial is rotated {} to point at {}".format(line.strip(), dial_position))

end_time = time.time()

print("Part 1 result: {}".format(count_of_zero_dials))
print("Part 2 result: {}".format(count_zero_passes))
print("The time of execution of above program is :", (end_time - start_time) * 10**3, "ms")
print()