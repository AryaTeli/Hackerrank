def print_rangoli(size):
    # your code goes here
    width = (size-1)*4+1
    for i in [abs(n) for n in range(-size+1, size)]: #absolute function to round the value or to make the input +ve
        line = chr(ord("a") + i)  #chr func to get the char of the ascii value and ord func to get the ascci value of the char
        for j in range(size-i-1):
            letter = chr(ord("a") + i + j + 1)
            line = letter + line + letter
            
        print("-".join(list(line)).center(width, "-"))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
