"""
 Q5. Vowel or Consonant  
 EASY Hint: Convert to lowercase first,
then check against a, e, i, o, u. Handle non-alphabet characters separately.
"""

    

Char= input("Enter the character ")
if len(Char) == 1 and Char.isalpha() == True:
    char =Char.lower()
    if char in "aeiou":
        print("Vowel")
    else:
        print("Consonant") 

else: print("not an alphabet")


#same but better 
def check_character(char):
    if len(char) != 1 or not char.isalpha():
        return "Not an alphabet"

    if char.lower() in "aeiou":
        return "Vowel"

    return "Consonant"


char = input("Enter a character: ")
print(check_character(char))
