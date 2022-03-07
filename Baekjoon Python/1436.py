N = int(input())
num = 0
cnt = 666
while (num<N):
    string = str(cnt)
    if string.find('666') != -1:
        num += 1
    cnt += 1
print(cnt-1)
