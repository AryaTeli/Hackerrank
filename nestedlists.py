list=[]
scores = set()
lowest_names = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])
        scores.add(score)
second_lowest = sorted(scores)[1]

for name,score in list:
    if score == second_lowest:
        lowest_names.append(name)
    
for name in sorted(lowest_names):
    print(name, end='\n')
