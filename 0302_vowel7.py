vowels = set('aeiou')
word = input('Poride a word to search foro vowels: ')
found = vowels.intersection(set(word))
for vowel in found :
    print(vowel)
