n = int(input())
lst=[]
for i in range(n):
    a, b = input().split()
    a = int(a)
    nw = (a,b)
    lst.append(nw)
lst.sort(key = lambda x:x[0])
for i in lst:
    print(i[0],i[1])
