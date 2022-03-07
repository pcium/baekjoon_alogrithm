import sys

N, M = map(int, sys.stdin.readline().split())
grid = [[0 for j in range(100)] for i in range(100)]
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    grid[temp[0]:temp[2]+1][temp[1]:temp[3]+1] += 1
    grid=[row[j:j+m] for row in grid[i:i+n]]



