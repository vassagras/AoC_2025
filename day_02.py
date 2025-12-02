import time
import os

def find_invalid_id(identifier) -> bool:
    l = len(str(identifier))
    if l % 2 == 0:
        if str(identifier)[0:l // 2] == str(identifier)[l // 2:]:
            return True
    return False

def find_invalid_id_v2(identifier) -> bool:
    num = str(identifier)
    l = len(num)
    half = l // 2
    for j in range(1,half+1,1):
        pattern = num[0:j]
        chunks = [num[k:k+j] for k in range(j, l, j)]
        if all(p == pattern for p in chunks): return True

    return False

start_p1 = time.time()
file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), r"data\Day 02"), 'r')

sum_1 = 0
sum_2 = 0
ranges = [i.strip() for i in file.read().split(",")]

for r in ranges:
    s = int(r.split("-")[0])
    e = int(r.split("-")[1])
    for i in range(s, e+1, 1):
        if find_invalid_id(i):
            sum_1 += i
        if find_invalid_id_v2(i):
            sum_2 += i

end_p1 = time.time()

print("Part 1 result: {}".format(sum_1))
print("Part 1 result: {}".format(sum_2))
print("The time of execution of above program is :", (end_p1 - start_p1) * 10**3, "ms")
print()
