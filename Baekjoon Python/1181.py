w = int(input())
words = {}

def word_val(s):
    result = 0
    for i in range(len(s)):
        result += (ord(s[i])-96)*26**(len(s)-i-1)
    return result

for i in range(w):
    plus = input()
    words[plus] = word_val(plus)
good = sorted(words, key= lambda x: words[x])
for i in good:
    print(i)
