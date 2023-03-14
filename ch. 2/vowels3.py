
vowels = ['a', 'e', 'u', 'o', 'i']
word = input('Provide a word to search for vowels: ')
found_list = []

for letter in word:
    if letter in vowels:
        if letter not in found_list:
            found_list.append(letter)
for vowel in found_list:
    print(vowel)
