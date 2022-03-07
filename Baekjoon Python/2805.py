import sys

'''
# Option 1 - Session Timeout
def reduce(left, N):
    for j in range(len(left)):
        left[j] = left[j] - 1
        if left[j]<0:
            N+=1
    return left, N

left = []
T, M = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))
for i in data:
    left.append(max(data)-i)

N = 0
height = max(data)
while(M>N):
    height -= 1
    left, N = reduce(left, N)
print(height)
'''

# Option 2
T, M = map(int, sys.stdin.readline().split())
data = list(map(int,sys.stdin.readline().split()))

total = 0
while(True)
    num = len(list(filter(lambda x : x<0, data)))
    total += num
    

'''
# 아래서부터는 불확실
H = height(max(sorted(students, key=lambda student:student[1]))))
a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
b = []    # 빈 리스트 생성
 
for i in a:      # 가로 크기를 저장한 리스트로 반복
    line = []    # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(i):    # 리스트 a에 저장된 가로 크기만큼 반복
        line.append(0)
    b.append(line)        # 리스트 b에 안쪽 리스트를 추가
 
print(b)

'''
