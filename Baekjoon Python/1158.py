import sys

N, K = map(int, sys.stdin.readline().split())
a = [i+1 for i in range(N)]
order = []
idx=0

while a==True: # 이 부분에서만 순서 잘 넣으면 된다
    idx+=K
    if order==False:
        order.append(K)
    else:
        order.append(a[idx%len(a)-1].pop()) # 나머지와 관련해서
    continue

print(order)

'''

# 결과 출력 창

print('<',end='')
for i in range(len(order)-1):
    print('{}, '.format(order[i]), end=' ')
print('{}>'.format(order[-1]),end='')

'''
