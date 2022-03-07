import sys

A1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m']
A2 = ['n','o','p','q','r','s','t','u','v','w','x','y','z']

N = list(sys.stdin.readline().rstrip())
for i in range(len(N)):
    asc = ord(N[i])
    if 97<=asc<=109:
        N[i] = A2[asc-97]
    elif 110<=asc<=122:
        N[i] = A1[asc-110]
    elif 65<=asc<=77:
        N[i] = A2[asc-65].upper()
    elif 78<=asc<=90:
        N[i] = A1[asc-78].upper()
for i in N:
    print(i, end='')
