vowels = ['a','e','i','o','u']

word = 'justin timberake'
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)

# print(found)

for vowel in found:
    print(vowel)
