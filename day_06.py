import time
import os
import math

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 06"), 'r')

sum_1 = 0
sum_2 = 0
operands = []
lines = file.readlines()
for i in range(0, len(lines) - 1):
    operands.append([int(op) for op in lines[i].strip().split()])

operators = lines[len(lines) - 1].strip().split()
for j in range(len(operands[0])):
    op = operators[j]
    result = 0
    if op == "+":
        result = sum([operands[i][j] for i in range(len(operands))])
    elif op == "*":
        result = math.prod([operands[i][j] for i in range(len(operands))])

    sum_1 += result

end_p1 = time.time()

print("Part 1 result: {}".format(sum_1))
print("Part 2 result: {}".format(sum_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()