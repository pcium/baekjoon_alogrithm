N = int(input())
line = 2**N
for i in range(line):
    if i==0:
        print('*')
        break
    elif i==1:
        print('**\n*')
        break
    
    if i%4==1:
        print('*', end='')
        print(' '*(line-2), end=' ')
        print('*')
    elif i%4==2:
        print('**')
    elif i%4==3:
        print('* *')
    else:
        print('****'*(i//4))
