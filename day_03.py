import time
import os

def find_largest_joltage(b) -> int:
    max_val = -1
    # try every possible first digit
    for i in range(len(b) - 1):
        d1 = b[i]
        # best possible second digit after i
        d2 = max(b[i + 1:])
        max_val = max(max_val, d1 * 10 + d2)

    return max_val

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 03"), 'r')

sum_1 = 0
sum_2 = 0

for bank in file.readlines():
    batteries = [int(battery) for battery in bank.strip()]
    sum_1 += find_largest_joltage(batteries)


end_p1 = time.time()

print("Part 1 result: {}".format(sum_1))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()