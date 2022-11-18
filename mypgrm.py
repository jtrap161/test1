#this program will sort strings provided by user, alphabetically
my_str = input('Enter a string: ')

#breakdown string into list of words
words = [word.lower() for word in my_str.split()]

#sort list
words.sort()

#display th sorted words
print("The sorted words are: ")

for words in words:
    print(words)