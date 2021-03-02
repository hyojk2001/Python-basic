def search4vowels(word):
    '''Display any vowels found in an asked-for word.'''
    vowels = set('aeiou')
    # word = input('Poride a word to search foro vowels: ')
    # found = vowels.intersection(set(word))
    # for vowel in found :
    #     print(vowel)
    # return bool(found)
    return vowels.intersection(set(word))

search4vowels('austin')
search4vowels('kkk')