import time
import os

def find_invalid_id(identifier) -> bool:
    l = len(str(identifier))
    if l % 2 == 0:
        if str(identifier)[0:l // 2] == str(identifier)[l // 2:]:
            return True
    return False

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"inputs\Day 02"), 'r')

sum_1 = 0
ranges = [i.strip() for i in file.read().split(",")]

for r in ranges:
    s = int(r.split("-")[0])
    e = int(r.split("-")[1])
    # print("Range from {} to {}".format(s, e))
    for i in range(s, e+1, 1):
        if find_invalid_id(i):
            sum_1 += i
            # print(i)

end_p1 = time.time()

print("Part 1 result: {}".format(sum_1))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()

