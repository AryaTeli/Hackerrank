def merge_the_tools(string, k):
    for i in range(0,len(string),k):
        a = string[i:i+k]
        b = list(dict.fromkeys(a))
        print("".join(b))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
