import time
import os

def is_weak_spot(g, x, y) -> bool:
    if g[x][y] == ".":
        return False

    rows, cols = len(g), len(g[0])
    paper_roll_count = 0

    # Check all 8 neighbors and ignore the cell itself
    for k in range(x-1, x+2):
        for t in range(y - 1, y + 2):
            # Skip out-of-bounds positions early
            if not (0 <= k < rows and 0 <= t < cols):
                continue

            # Skip the current cell
            if k == x and t == y:
                continue

            if g[k][t] == "@":
                paper_roll_count += 1
            # Exit as soon as too many paper rolls are detected
            if paper_roll_count > 3: return False
    return True

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 04"), 'r')

count_1 = 0
count_2 = 0
grid = [list(line.strip()) for line in file]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if is_weak_spot(grid, i, j):
            count_1 += 1

print("Part 1 result: {}".format(count_1))


count_2 = 0
while True:
    weak_spots = [(i, j) for i in range(len(grid)) for j in range(len(grid[0]))
                  if is_weak_spot(grid, i, j)]
    if not weak_spots:
        break

    count_2 += len(weak_spots)

    for x, y in weak_spots:
        grid[x][y] = "."


end_p1 = time.time()

print("Part 2 result: {}".format(count_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()