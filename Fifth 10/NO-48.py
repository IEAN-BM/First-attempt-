def longest_words(sentence):
    words = sentence.split()
    max_length = max(len(word) for word in words)
    longest = [word for word in words if len(word) == max_length]
    return longest
s = input('enter a text')
print (longest_words(s))