"""Find palindromes (letter palingrams) in a dictionary file recursively"""

import load_dictionary
word_list = load_dictionary.load('2of4brif.txt')

def palindrome_recursive(word):
    """Determine whether or not an input word is a palindrome
    
    Keyword arguements:
    word - any string
    """    
    word = word.lower()
    
    # Word is a palindrome if word length is less than 1
    if len(word) < 2:
        return True
    # If first and last letter from word are equal strip off and call
    # function recursively
    elif word[0:1] == word[-1:]:
        word = word[1:len(word)-1]
        return palindrome_recursive(word)
    # Any other condition does not meet criteria of a palindrome.
    else:
        return False

pali_list = []
for word in word_list:    
    if palindrome_recursive(word) == True:
        pali_list.append(word)
print(*pali_list, sep='\n')