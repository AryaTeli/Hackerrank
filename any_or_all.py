N = int(input()) 
l = list(map(int,input().split()))
print(all([i>0 for i in l]) and any([(i==int(str(i)[::-1])) for i in l]))
