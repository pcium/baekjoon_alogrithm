import sys

def swap(S, A, B):
    S[A], S[B] = S[B], S[A]
    
S = sys.stdin.readline().rstrip()
T = int(sys.stdin.readline())
for i in range(T):
    A, B = map(int, input().split())
    tmp = S[A]
    if (A) == 14:
        S = S[:A] + S[B]
        S = S[:B] + tmp + S[B+1:]
    elif (B) == 14:
        S = S[:A] + S[B] + S[A+1:]
        S = S[:B] + tmp
    elif (A) == 14 and (B) == 14:
        S = S[:A] + S[B]
        S = S[:B] + tmp
    else:
        S = S[:A] + S[B] + S[A+1:]
        S = S[:B] + tmp + S[B+1:]
print(S)
