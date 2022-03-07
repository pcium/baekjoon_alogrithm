import sys
for line in sys.stdin:
    if line == "0\n":
        break
    else:
        a = list(line)
        a.pop()
        b = a[:]
        b.reverse()
        if (a==b):
            print("yes")
        else:
            print("no")

