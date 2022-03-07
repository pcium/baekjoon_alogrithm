import math  

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

case = int(input())
cses = []
for i in range(case):
    a = int(input())
    b = int(input())
    cses.append([a,b])

for i in cses:
    k = i[0] + 1
    n = i[0] + i[1]
    print(int(math.factorial(n)/(math.factorial(n-k)*math.factorial(k))))
