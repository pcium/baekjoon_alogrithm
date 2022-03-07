import sys

def create_sample(y):
    l = []
    lin = ''
    if (y%2==0):
        l.append('WB'*int(y/2))
        l.append('BW'*int(y/2))
    else:
        l.append('W'+'BW'*int((y-1)/2))
        l.append('B'+'WB'*int((y-1)/2))
    return l # Sample 완성

x, y = map(int, sys.stdin.readline().split()) # 크기 입력
data = [list(sys.stdin.readline().strip()) for i in range(x)] # 데이터 2차원 리스트 완성

sample = create_sample(y) # 필더 만들기 위한 두 가지 Sample 생성
# print(sample)

error1 = [[0 for j in range(y)] for i in range(x)]
error2 = [[0 for j in range(y)] for i in range(x)] # 전부 0으로 초기화

def error_set(data, sample, error1, error2):
    if data[0][0]=='B':
        sample[0], sample[1] = sample[1], sample[0] # SWAP

    for i in range(x):
        for j in range(y):
            if data[i][j] != sample[i%2][j]:
                error1[i][j] = 1
            else:
                error2[i][j] = 1

# 일부 구역에 있는 것들만 더한다
def error_count(a, b, err1, err2): # a = data , b = sample
    plus1, plus2 = 0, 0
    for i in range(a, a+8): # 여기서 오류 난다
        for j in range(b, b+8): # 입력이 데이터 / 샘플이 아닌, 특정 숫자에 관한 것이어야한다.
            plus1 += error1[i][j]
            plus2 += error2[i][j] 
    return min(plus1, plus2)

error_set(data, sample, error1, error2)
minimum = x * y # 우선 최소값
# 이것을 더 작은 값들로 갱신해야한다

for g1 in range(x-7):
    for g2 in range(y-7):
         minimum = min(error_count(g1, g2, error1, error2), minimum)
print(minimum)
