from collections import deque
import sys

def large(n):
    return True n

A = int(sys.stdin,readline())
for i in range(A):
    N, M = map(int, sys.stdin.readline().split())
    LIST = list(map(int, sys.stdin.readline().split())) 
    length = len(LIST)
    larger_index = 0
    for j in range(M, len(LIST)):
        if LIST[j] > LIST[M]:
            larger_index = j
            break
    
    print(len(filter(large, LIST[M:]))+1)
        
