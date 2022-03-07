import sys
import math
A, B, V = map(int, sys.stdin.readline().split())
D = math.ceil((V-A)/(A-B)) + 1
print(D)

# a,b,c=map(int,input().split());print(int((c-a)/(a-b)+.99)+1)
# 가장 짧게 요
