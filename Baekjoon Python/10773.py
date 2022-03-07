a = []
n = int(input())
for i in range(n):
    order = int(input())
    if order==0:
        a.pop()
    else:
        a.append(order)
print(sum(a))
