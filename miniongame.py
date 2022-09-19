def minion_game(string):
    vowels = "AEIOU"
    stuart, kevin = 0, 0
    for i in range(len(string)):
        scores = len(string)-i #
        if string[i] in vowels:
            kevin = scores + kevin
        else:
            stuart = stuart + scores
    if kevin == stuart:
            print("Draw")
    elif(kevin>stuart):
        print("Kevin", kevin)
    elif(stuart>kevin):
        print("Stuart", stuart)
    # your code goes here

if __name__ == '__main__':
    s = input()
    minion_game(s)
