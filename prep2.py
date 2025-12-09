# STRINGS

# Reverse a String
# Input: "hello" → Output: "olleh"

# a = 'hello'
# print (a[::-1])

# Check Palindrome String
# Input: "madam" → Output: Palindrome

# b = 'madam' 
# if b == b[::-1]:
#     print("The string is palindrome")
# else:
#     print("The string is not palindrome")    

# Count Vowels and Consonants Output both counts.    
# s = 'hello'
# vowel = 'aeiouAEIOU'

# vowel_count = sum(1 for ch in s if ch in vowel)
# consonant_count = sum(1 for ch in s if ch.isalpha() and ch not in vowel)

# print ("Vowels:", vowel_count)
# print ("Consonants:", consonant_count)

# Count Words in a Sentence
# Input: "I love Python" → Output: 3

def count_words (sentence):
    words = sentence.split()
    print(len(words))

sentence = input().strip()
count_words(sentence)