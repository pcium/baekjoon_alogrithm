import sys

data = sys.stdin.readline()
n = len(data)
for i in range(int(n/10)):
    print(data[i*10:(i+1)*10])
print(data[int(n/10)*10:n], end='')
