import sys

T = int(sys.stdin.readline())
for i in range(T):
    zero = 0
    start, end = map(int, sys.stdin.readline().split())
    test_case = [str(i) for i in range(start, end+1)]
    for j in test_case:
        zero += list(j).count('0')
    print(zero)
