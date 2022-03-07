import sys
N = int(sys.stdin.readline())
org = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
bag = list(map(int, sys.stdin.readline().split()))
org.sort()

def bin_search(L,x):
    front=0
    rear=len(L)-1
    while front <= rear:
        mid = (front+rear)//2
        if L[mid]==x:
            return mid
        elif L[mid]<x:
            front=mid+1
        elif L[mid]>x:
            rear=mid-1
    return -1

for i in bag:
    if (bin_search(org, i)==-1):
        sys.stdout.write("0\n")
    else:
        sys.stdout.write("1\n")
