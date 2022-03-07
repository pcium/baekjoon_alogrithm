import sys

added_candy = []
guess = []
N = int(sys.stdin.readline())
for i in range(N):
    added_candy.append(int(sys.stdin.readline()))

guess_0 = 0
guess.append(guess_0)
while guess_0 <= guess[0]:
    for i in range(N-1):
       guess.append(added_candy[i]-guess[-1])
    if added_candy[-1]==(guess[0]+guess[-1]):
        break
    else:
        guess = []
        guess_0 += 1
        guess.append(guess_0)
for i in guess:
    print(i)
