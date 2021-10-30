#instructions 

# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
#  The first word within the output should be capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case).

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

import re



def to_camel_case(text):
    new_string = (re.split('[^a-zA-Z]', text.title()))
    print(text[0])
    return ''.join(new_string).replace(new_string[0][0], text[0])


print(to_camel_case("the_Stealth_Warrior"))