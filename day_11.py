import time
import os

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 11"), 'r')

graph = {}
for line in file:
    # Split each line into node and its neighbors using ":" as separator
    parts = line.strip().split(":")
    node = parts[0]
    graph[node] = parts[1].split()

start_node = "you"
end_node = "out"
count_1 = 0

q = [start_node]
while q:
    current_node = q.pop(0)
    if current_node == end_node:
        count_1 += 1
    else:
        for neighbor in graph[current_node]:
            q.append(neighbor)

start_node = "srv"
q = [start_node]
path = ""


end_p1 = time.time()

print("Part 1 result: {}".format(count_1))
print("Part 2 result: {}".format(0))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()