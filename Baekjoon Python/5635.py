import sys

student = []
T = int(sys.stdin.readline())
for i in range(T):
    student.append(list(sys.stdin.readline().split()))
    for j in range(1,4):
        student[i][j] = int(student[i][j])
student.sort(key = lambda x:(x[3],x[2],x[1]))

print(student[-1][0])
print(student[0][0])
