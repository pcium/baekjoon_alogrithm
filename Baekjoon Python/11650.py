import time
n = int(input())
grid=[]
for i in range(n):
    a, b = input().split()
    a = int(a)
    b = int(b)
    nw = (a,b)
    grid.append(nw)
grid.sort()
for i in grid:
    print(i[0],i[1])
