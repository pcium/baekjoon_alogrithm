import sys
import heapq

'''
# Heap Sort

h = []
N = int(sys.stdin.readline())
for i in range(N):
    heapq.heappush(h, int(sys.stdin.readline().strip()))
for i in range(N):
    print(heapq.heappop(h))
'''

def BubbleSort(h, size):
    for i in range(size-1, 0, -1):
        for j in range(0, i):
            if (h[j] > h[j+1]):
                temp = h[j]
                h[j] = h[j+1]
                h[j+1] = temp
    return h

h = []
N = int(sys.stdin.readline())
for i in range(N):
    h.append(int(sys.stdin.readline().strip()))
h = BubbleSort(h, N)
for i in h:
    print(i)
