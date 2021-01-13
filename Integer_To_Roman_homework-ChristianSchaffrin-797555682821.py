#Convert an integer value to its roman number.

def int_to_rome(x):
    numbers = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    roman = ['I','IV','V','IX', 'X','XL', 'L','XC', 'C','CD', 'D','CM','M']
    i = 12  
    roman_numeral = ''
    while x != 0:
        if numbers[i] <= x:    
            roman_numeral += roman[i] 
            x = x - numbers[i]
        else:
            i -= 1 # i = i - 1
    return roman_numeral 

print(int_to_rome(34))
print(int_to_rome(777))
print(int_to_rome(334))
print(int_to_rome(4312)) 
print(int_to_rome(4999))
print(int_to_rome(5312))