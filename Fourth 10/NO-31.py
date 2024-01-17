def words(str):
    count = 0
    str = str.split( )
    List = list(str)
    for i in range(len(List)):
        count = count + 1
    return count
text = input('enter text')
print(words(text))