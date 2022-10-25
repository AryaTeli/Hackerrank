M=int(input())
a=set(map(int, input().split()))
N=int(input())
b=set(map(int, input().split()))

diff_in_a=a.difference(b)
diff_in_b=b.difference(a)
print('\n'.join(map(str,sorted(diff_in_a.union(diff_in_b)))))
