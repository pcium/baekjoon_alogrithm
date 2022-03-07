import sys
N = int(sys.stdin.readline())
collection = []
for line in sys.stdin:
    collection.append(tuple(map(int, line.strip().split())))
collection.sort(key=lambda x:(x[1],x[0]))
for i in collection:
    print(i[0], i[1])
