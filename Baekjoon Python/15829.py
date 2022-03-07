import sys
N = int(sys.stdin.readline())
mj = list(sys.stdin.readline())
mj.pop()
mj = [ord(i)-96 for i in mj]
result = [mj[i]*31**i for i in range(N)]
print(sum(result)%1234567891)
