word = input('Enter a word: ')

word = word.lower()

if(word == 'a' or word == 'e' or word == 'i' or word == 'u'):
    print(f'{word} is Vowel')
else:
    print(f'{word} is Consonant')
