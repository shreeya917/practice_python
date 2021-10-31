def check_vowel(word):
    word = word.lower()
    if(word == 'a' or word == 'e' or word == 'i' or word == 'u'):
        return 'Vowel'

    else:
        return 'Consonant'


word = input('Enter a word: ')

check = check_vowel(word)
print(check)
