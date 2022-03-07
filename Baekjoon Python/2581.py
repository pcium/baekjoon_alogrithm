import sys
import math


M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
prime = [i for i in range(M, N+1)]

for i in range(2, int(math.sqrt(M))+1):
    for j in range(len(prime)):
        if j%i==0:
            prime.remove(prime[j])
print(prime)
