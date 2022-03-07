import sys

data=[]

N = int(sys.stdin.readline())
for i in range(N):
    data.append(list(map(int, sys.stdin.readline().split())))
data.sort(key=lambda x:-x[2])
# print(data)
print(data[0][0], data[0][1])
print(data[1][0], data[1][1])
if(data[0][0]==data[1][0]):
    new = list(filter(lambda x: x[0] != data[0][0], data))
    print(new[0][0], new[0][1])
else:
    print(data[2][0], data[2][1])
