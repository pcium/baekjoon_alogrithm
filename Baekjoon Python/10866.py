q = []
put = []

def deq(k):
    a = k[0]
    if a=="empty":
        if len(q)==0:
            print(1)
        else:
            print(0)
    elif a=="front":
        if len(q)==0:
            print(-1)
        else:
            print(q[0])
    elif a=="back":
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])
    elif a== "size":
        print(len(q))
    elif a=="push_front":
        b = int(k[1])
        q.insert(0, b)
    elif a=="push_back":
        b = int(k[1])
        q.append(b)
    elif a=="pop_front":
        if len(q)==0:
            print(-1)
        else:
            print(q.pop(0))
    elif a=="pop_back":
        if len(q)==0:
            print(-1)
        else:
            print(q.pop())

n=int(input())
for i in range(n):
    put.append(tuple(map(str, input().strip().split())))
for k in put:
    deq(k)
