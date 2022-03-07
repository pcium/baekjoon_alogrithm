import sys

past = 0
x, y = map(int, input().split())
days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
length = [0,31,28,31,30,31,30,31,31,30,31,30]
past = sum(length[0:x]) + y
print(days[past%7-1])
