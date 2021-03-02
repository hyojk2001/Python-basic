# nums = [1,2,3,4]
# nums

# nums.remove(3)
# print(nums)

# nums.pop(1)
# print(nums)

# nums.extend([10,11])
# print(nums)

# nums.append([22,33])
# print(nums)

# nums.insert(0,1111)
# print(nums)

# a = [2,3,4,5]

# for i in range(4):
#     a.pop()

# 리스트를 복사할때는 연산자를 사용하는 것이 아니라 copy를 사용하는 것이 바람직하다

# saying = "Don't be panic!"
# letters = list(saying)
# letters[-1]

vowels = ['a','e','i','o','u']

word = input('Provide a word to search for vowels: ')
found = {}

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1

for k,v in sorted(found.items()):
    print(k, 'was found', v, 'time(s)')
