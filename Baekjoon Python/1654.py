import sys

# Timeout

wire = []
N, K = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    tmp = int(sys.stdin.readline())
    wire.append(tmp)
std = sum(wire)//K
num = 0
while True:
    piece = 0
    for i in wire:
        tmp =  i // std
        piece += tmp
    if piece == K:
        print(std)
        break
    else:
        std -= 1
        
