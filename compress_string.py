from itertools import groupby
A = input()
for c,x in groupby(A):
    print(*[(len(list(x)), int(c))],end=" ")
