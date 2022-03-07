import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(N)]
data.sort()

def common(data):
    dic = {}
    many = []
    for i in data:
        if dic.get(i) is None:
            dic[i] = 1
        else:
            dic[i] += 1
    common = max(dic.values())
    for key, value in dic.items():
        if value == common:
            many.append(key)
    many.sort()
    try:
        return many[1]
    except IndexError:
        return many[0]
        
print(round(sum(data)/N))
print(data[int(N/2)])
print(common(data))
print(max(data)-min(data))
