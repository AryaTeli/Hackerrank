N,M = map(int,input().split(' '))
char = ".|."
count = 0
for i in range(N):
    if i == N // 2:
        print('WELCOME'.center(M, '-'))
    elif i < N // 2:
        print((char * (i * 2 + 1)).center(M, '-'))
        count=i*2+1
    elif i > N // 2:
        print((char * count).center(M, '-'))
        count = count-2         
