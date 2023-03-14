
vowels = ['a', 'e', 'u', 'o', 'i']
word = "Milliways"
found_list = []

for letter in word:
    if letter in vowels:
        if letter not in found_list:
            found_list.append(letter)
for vowel in found_list:
    print(vowel)
