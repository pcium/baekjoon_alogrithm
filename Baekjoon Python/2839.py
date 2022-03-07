import sys
N = int(sys.stdin.readline())
current_min = 5001
x,y = 0,0
while(N-5*y>=0):
    x = (N-5*y)/3
    if (x) == int(x):
        current_min = int(x+y)
    y+=1

if current_min == 5001:
    print(-1)
else:
    print(current_min)
