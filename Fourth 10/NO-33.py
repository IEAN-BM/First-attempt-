word = input ('enter a string seperated by commas')
List = []
X = []
sum = 0
s = word.replace(',','0')
List = list(s)
print(List)
for i in List:
    sum = sum + i
#sum = sum(List)
print(sum)