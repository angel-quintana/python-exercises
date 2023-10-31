'''
returns true if 2
'''

def is_two(n):
    if int(n) ==2 or str(n) == 2:
        return True
    else:
        return False



'''
returns true if vowel
'''

def is_vowel(str1):
    if type(str1) == str:
        vowels = ["a","e","i","o","u"]    #,"A","E","I","O","U"]
        return str1.lower() in vowels
    else: return f" {str1} is not a string"


'''
returns true if consonant
'''

def is_consonant(str):
    
    vowels = ["a","e","i","o","u"]   
    return str.lower() not in vowels



'''
returns first letter capitolized if consonant
'''

def capitolize_consonant(str):
    result = str[0]
    vowels = ["a","e","i","o","u"]   
    if result not in vowels:
        return f'{result.upper()}{str[1:]}'
    else:
        return str


'''
returns tip when supplied tip percentage and bill
'''

def calculate_tip(tip_percent, bill):
    tip = tip_percent * bill    
    return tip



'''
returns discounted cost when given original price and discount 
'''

def apply_discount(og_price, discount_percent):
    disc_price = og_price - (og_price * discount_percent)
    return disc_price



'''
returns inputed number without commmas
'''

def handle_commas(input_number):
    no_comma= input_number.replace(',','')
    return no_comma

'''
returns letter grade according to input grade number
'''

def get_letter_grade(grade_number):
    
    if grade_number > 90:
        return "A"
    elif grade_number > 80:
        return "B"
    elif grade_number > 70:
        return "C"
    elif grade_number > 60:
        return "D"
    else:
        return "F"

'''
returns string without vowels
'''

def remove_vowels(str):
    new_str= ""
    vowels = ["a","e","i","o","u"]
    for letter in str:
       
        if letter.lower() not in vowels:
            new_str = new_str + letter
            
    return new_str  

'''
returns input string as valid python identifier
'''

def normalize_name(str1):
    numbers = [(number) for number in range(0,10)]
    alphabet = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]
    alpha_numeric= numbers + alphabet + ['_']  + [" "]
    new_str = ""
    
    
    for char in str1:
        if char.lower() in alpha_numeric:
            new_str= new_str + char #creating new string with valid alpha-numerics and spaces only
            
    new_str_trimmed= new_str.strip() #removing leading and following white space
    new_str_scored= new_str_trimmed.replace(' ','_') #replacing spaces with underscores
    new_str_lowered = new_str_scored.lower() #lowercasing the string
    final_str = new_str_lowered
    
    return final_str
