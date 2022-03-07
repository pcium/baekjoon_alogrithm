import sys

M, n = map(int, sys.stdin.readline().split())
moves = ([1,0], [0, 1], [-1, 0], [0, -1]) # 모듈로 구현
move = 0
current = [0,0]

for i in range(n):
    direction, distance = map(str, sys.stdin.readline().split())
    distance = int(distance)
    if direction == 'MOVE':
        current[0] = current[0] + distance * moves[move][0]
        current[1] = current[1] + distance * moves[move][1]
    else:
        if distance==0:
            move+=1
        else:
            move-=1
    if (0<=current[0]<=M) and (0<=current[1]<=M):
        continue
    else:
        print(-1)
        sys.exit()
print(current[0], current[1])
