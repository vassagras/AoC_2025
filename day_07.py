import time
import os
from ManifoldDay07 import ManifoldDay07

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 07"), 'r')

count_2 = 0

manifold_diagram = []
lines = file.readlines()
for i in range(0, len(lines) - 1):
    manifold_diagram.append(list(lines[i].strip()))

# Adding the start position
beams = [(1, 70)]
manifold = ManifoldDay07(manifold_diagram, beams)
manifold.propagate()

end_p1 = time.time()

print("Part 1 result: {}".format(manifold.splitter_count))
print("Part 2 result: {}".format(count_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()