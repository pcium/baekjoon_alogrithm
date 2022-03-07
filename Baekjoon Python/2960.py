import sys
import math

N, K = int()
numbers = [True for i in range(N+1)]
cnt = 1
P = 2
popped = 0

for i in range(2, int(math.sqrt(N))+1):
    if numbers[i] == True:
        j = 2
        while i*j <= N:
            array[i*j] = False
            j+=1
