import time
import os
import math

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 06"), 'r')

# Part 1
sum_1 = 0
operands = []
lines = file.readlines()
for i in range(0, len(lines) - 1):
    operands.append([int(op) for op in lines[i].strip().split()])

operands_rows = len(lines) - 1
operators = lines[operands_rows].strip().split()

for j in range(len(operands[0])):
    op = operators[j]
    result = 0
    if op == "+":
        result = sum([operands[i][j] for i in range(len(operands))])
    elif op == "*":
        result = math.prod([operands[i][j] for i in range(len(operands))])

    sum_1 += result
print("Part 1 result: {}".format(sum_1))


# Part 2
char_matrix = []
sum_2 = 0
# Convert each line of input into a list of characters
for line in lines:
    char_matrix.append([c for c in line])

# Identify the positions (indexes) of operators in the last row of the matrix
operators_indexes = []
operator_row = len(char_matrix) - 1
for i, c in enumerate(char_matrix[operator_row]):
    if c != " " and c != "\n":
        operators_indexes.append(i)

# Process each operator column-wise
for index, val in enumerate(operators_indexes):

    op = char_matrix[operator_row][val] # the operator character: '+' or '*'
    op_start_index = val # starting column index for this operator

    # Determine the end column index: either the next operator - 1, or the end of the row
    if index < len(operators_indexes) - 1:
        op_end_index = operators_indexes[index + 1] - 1
    else:
        op_end_index = len(char_matrix[0])

    # Collect operands for this operator
    operands_2 = []
    for j in range(op_start_index, op_end_index):
        current_number_str = ""
        # iterate over the rows containing numbers
        for i in range(operands_rows):
            if j < len(char_matrix[i]) and char_matrix[i][j] not in (" ", "\n"):
                current_number_str += char_matrix[i][j]  # concatenate digits vertically
        if current_number_str != "":
            operands_2.append(int(current_number_str))

    # Apply the operator to the collected operands
    if op == "+":
        sum_2 += sum(operands_2)
    elif op == "*":
        sum_2 += math.prod(operands_2)

end_p1 = time.time()

print("Part 2 result: {}".format(sum_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()