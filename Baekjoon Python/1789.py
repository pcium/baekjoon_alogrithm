import sys
target = int(sys.stdin.readline())
accum = 1
count = 0
while accum <= target:
    accum += count
    count += 1
print(count-2)
