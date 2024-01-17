from random import shuffle
s = input('enter a string')
List = list(s)
shuffle(List)
word = ''.join(List)
print(List)
print(word)