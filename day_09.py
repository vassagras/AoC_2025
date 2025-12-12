import time
import os

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 09"), 'r')

def rectangle_area(c1, c2) -> int:
    x_1, y_1 = c1
    x_2, y_2 = c2

    return (abs(x_2 - x_1) + 1) * (abs(y_2 - y_1) + 1)

coordinates = [list(map(int, c.strip().split(","))) for c in file]

max_area = 0
max_corner_1 = None
max_corner_2 = None
n = len(coordinates)
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        # skip if the two corners are in the same line
        if x1 == x2 or y1 == y2:
            continue

        current_area = rectangle_area(coordinates[i], coordinates[j])
        if current_area > max_area:
            max_area = current_area
            max_corner_1 = coordinates[i]
            max_corner_2 = coordinates[j]

end = time.time()

print("Part 1 result: {}".format(max_area))
print("Part 2 result: {}".format(0))
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
print()
