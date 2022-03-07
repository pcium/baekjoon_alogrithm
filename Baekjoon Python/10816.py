from bisect import bisect_left, bisect_right
import sys

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a,right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
M = int(sys.stdin.readline())
require = list(map(int, sys.stdin.readline().split()))
ans = []
for i in require:
    ans.append(count_by_range(data, i, i))
for j in ans:
    print(j,end=' ')
