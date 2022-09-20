if __name__ == '__main__':
    n = int(input())
    b = map(int, input().split())
    c = (sorted(list(set(b))))
    print(c[-2])
