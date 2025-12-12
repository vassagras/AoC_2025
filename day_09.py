import time
import os
from shapely.geometry import Polygon, box

start = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 09"), 'r')

def rectangle_area(c1, c2) -> int:
    x_1, y_1 = c1
    x_2, y_2 = c2

    return (abs(x_2 - x_1) + 1) * (abs(y_2 - y_1) + 1)

def is_rectangle_inside_polygon(vertices, c1, c2):
    poly = Polygon(vertices)
    rect = box(min(c1[0], c2[0]), min(c1[1], c2[1]),
               max(c1[0], c2[0]), max(c1[1], c2[1]))
    return rect.within(poly)

coordinates = [list(map(int, c.strip().split(","))) for c in file]

max_area = 0
max_area_b = 0

n = len(coordinates)
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        # skip if the two corners are in the same line
        if x1 == x2 or y1 == y2:
            continue

        current_area = rectangle_area((x1, y1), (x2, y2))
        if current_area > max_area:
            max_area = current_area

        if is_rectangle_inside_polygon(coordinates, (x1, y1), (x2, y2)) and current_area > max_area_b:
            max_area_b = current_area

end = time.time()

print("Part 1 result: {}".format(max_area))
print("Part 2 result: {}".format(max_area_b))
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
print()
