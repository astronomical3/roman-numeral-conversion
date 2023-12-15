thousands_letters = {0:'', 1:'M', 2:'MM', 3:'MMM'}
hundreds_letters = {0:'', 1:'C', 2:'CC', 3:'CCC', 4:'CD', 5:'D', 6:'DC', 7:'DCC', 8:'DCCC', 9:'CM'}
tens_letters = {0:'', 1:'X', 2:'XX', 3:'XXX', 4:'XL', 5:'L', 6:'LX', 7:'LXX', 8:'LXXX', 9:'XC'}
ones_letters = {0:'', 1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}

try:
    number = int(input("Enter a number from 1 to 3999: "))
    thousands_digit = number // 1000
    thousands_rem = number % 1000
    hundreds_digit = thousands_rem // 100
    hundreds_rem = thousands_rem % 100
    tens_digit = hundreds_rem // 10
    tens_rem = hundreds_rem % 10
    ones_digit = tens_rem
    print("Here is the number in Roman Numerals:", end=" ")
    print(thousands_letters[thousands_digit] + hundreds_letters[hundreds_digit] + tens_letters[tens_digit] + ones_letters[ones_digit])
except: 
    print("<ERROR: entered a number 4000 or above, or entered a negative number>")
