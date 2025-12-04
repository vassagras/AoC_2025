import time
import os

def find_largest_joltage(b) -> int:
    # Stores the best (largest) two-digit number found so far
    max_val = -1

    # For each position i, treat b[i] as the first digit
    for i in range(len(b) - 1):
        d1 = b[i]
        d2 = max(b[i + 1:])
        max_val = max(max_val, d1 * 10 + d2)

    return max_val

def find_largest_joltage_v2(b, j, digits) -> str:
    """
    b: list of digits (ints 0–9)
    j: list of selected digits
    digits: how many digits we want to keep
    """

    # If the remaining list has exactly the number of digits we need, take everything.
    if len(b) == digits:
       return "".join(str(i) for i in j + b)
    # If we don't need any more digits, return what we have.
    if digits == 0:
        return "".join(str(i) for i in j)

    # Search limit: only the prefix where selecting still allows enough digits
    search_limit = len(b) - digits + 1
    max_val = -1
    max_index = -1

    # Find the max element in the allowed prefix range
    for i in range(search_limit):
        if max_val < b[i]:
            max_val = b[i]
            max_index = i

    # append max_digit
    return find_largest_joltage_v2(b[max_index + 1:], j + [max_val], digits - 1)


start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 03"), 'r')

sum_1 = 0
sum_2 = 0

for bank in file.readlines():
    batteries = [int(battery) for battery in bank.strip()]
    sum_1 += find_largest_joltage(batteries)
    sum_2 += int(find_largest_joltage_v2([int(e) for e in batteries], [], 12))

end_p1 = time.time()

print("Part 1 result: {}".format(sum_1))
print("Part 1 result: {}".format(sum_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()