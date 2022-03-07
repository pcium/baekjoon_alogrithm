import sys

ppl = ['SK','CY']
N  = int(sys.stdin.readline())
if N%2==0:
    print(ppl[1])
else:
    print(ppl[0])
