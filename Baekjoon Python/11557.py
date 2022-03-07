import sys

T = int(sys.stdin.readline())
for i in range(T):
    school = []
    N = int(sys.stdin.readline())
    for j in range(N):
        school.append(list(sys.stdin.readline().split()))
    school.sort(key=lambda x:-int(x[1]))
    print(school[0][0])
