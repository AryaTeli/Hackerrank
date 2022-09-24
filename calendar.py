import calendar
M,D,Y = map(int,(input().split(" ")))
dict = {0:"MONDAY", 1:"TUESDAY", 2:"WEDNESDAY", 3:"THURSDAY", 4:"FRIDAY", 5:"SATURDAY", 6:"SUNDAY"}
print(dict[calendar.weekday(Y,M,D)])
