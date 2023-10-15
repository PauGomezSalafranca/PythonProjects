from collections import Counter
checkText = input("Insert your first text: ")
checkText2 = input("Insert your second text: ")

def isPalindromic(text):
    
    reversedText = text[::-1]
    if text == reversedText:
        return print("Your text is a palindrome text")
    else:
        return print("Your text is not a palindrome text")
    
isPalindromic(checkText)

def isAnagrama(text1, text2):

    c1 = Counter(text1)
    c2 = Counter(text2)

    if c1 == c2:
        return print("Your two texts are anagrams")
    else:
        return print("Your two texts are not anagrams")
    
isAnagrama(checkText, checkText2)


def isTitle(text):
    if text.istitle():
        return print("Tu texto ya está en formato título: " + text)
    else:
        return print("Tu texto no estaba en formato título, aquí tienes una muestra de como sería en formato título: " + text.title())
    

isTitle(checkText)