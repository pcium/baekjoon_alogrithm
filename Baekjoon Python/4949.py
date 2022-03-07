import sys

stack = []
stack2 = []
case1 = ['(','[',']', ')']
case2 = ['(', '[']
case3 = [')', ']']
jjak1 = ['(', ')']
jjak2 = ['[',']']
linear = ['[ first in ] ( first out ).', 'A rope may form )( a trail in a maze.', '([ (([( [ ] ) ( ) (( ))] )) ]).', ' .']
'''
# 입력부 구현 완료

for line in sys.stdin:
    linear.append(line.strip())
    print(linear)
'''
n = len(linear)
for i in range(n):
    pandan = list(linear[i])
    choochool = [word for word in pandan if word in case1] # 이제 우리와 관련 있는 것만 보인다
    stack.append(choochool)
    print(choochool) # 보는 용도


for i in range(n):
    while stack[i]==True:
        
    
