import time
import os
import math
import networkx as nx
from networkx.classes import Graph


def straight_line_distance(p1, p2) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def prod_of_circuit_sizes(g) -> int:
    # Get connected components (as sets of nodes)
    components = list(nx.connected_components(g))

    # Size of each component
    component_sizes_sorted = sorted((len(c) for c in components), reverse=True)
    return math.prod(component_sizes_sorted[0:3])


start_time = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 08"), 'r')

junction_boxes = [tuple(map(int, line.strip().split(","))) for line in file]
nbr_of_junction_boxes = len(junction_boxes)

# Calculate the distances between each pair of points
distances = {}
for i in range(0, nbr_of_junction_boxes):
    point_1 = junction_boxes[i]

    for j in range(i + 1, nbr_of_junction_boxes):
        point_2 = junction_boxes[j]
        distances[(point_1, point_2)] = straight_line_distance(point_1, point_2)

# Sort the distances in ascending order
sorted_distances_dict = sorted(distances.items(), key=lambda item: item[1])

# Create a graph
graph = Graph()
# Add all nodes to the graph
graph.add_nodes_from(junction_boxes)
# Add the first 1000 edges i.e., the pair of coordinates with the smallest distance
for key, dist in sorted_distances_dict[:1000]:
    graph.add_edge(key[0], key[1], weight=dist)

result_1 = prod_of_circuit_sizes(graph)

print("Part 1 result: {}".format(result_1))


result_2 = 1
# Continue creating edges until the graph is fully connected
for key, dist in sorted_distances_dict[1000:]:
    graph.add_edge(key[0], key[1], weight=dist)
    if nx.is_connected(graph):
        result_2 *= key[0][0] * key[1][0]
        break

end_time = time.time()

print("Part 2 result: {}".format(result_2))
print("The time of execution of above program is :", (end_time - start_time) * 10**3, "ms")
print()