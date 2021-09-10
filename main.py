# Convert non-minimal Roman Numeral to Decimal
def RomanToDecimal(input_roman = str):
    #word_array=input_roman.split('')
    decimal_number=0
    print(input_roman)
    for i in input_roman:
        if (i == 'I'):
            decimal_number = decimal_number + 1
        elif (i == 'V'):
            decimal_number = decimal_number + 5
        elif (i == 'X'):
            decimal_number = decimal_number + 10
        elif (i == 'L'):
            decimal_number = decimal_number + 50
        elif (i == 'C'):
            decimal_number = decimal_number + 100
        elif (i == 'D'):
            decimal_number = decimal_number + 500
        elif (i == 'M'):
            decimal_number = decimal_number + 1000

    print(decimal_number)



# Convert decimal to Minimal Roman Numeral

def ToRoman(input_decimal = int):
    next_decimal = input_decimal
    Count_M = int(next_decimal/1000)
    Print(Count_M)
    # if Count_M >= 1
    next_decimal = next_decimal%1000
    Count_D = int(next_decimal/500)
    Print(Count_D)
    # if Count_D >= 1:
    next_decimal = next_decimal%500
    Count_C = int(next_decimal/100)
    Print(Count_C)
    # if Count_C >= 1:
    next_decimal = next_decimal % 100
    Count_L = int(next_decimal / 50)
    Print(Count_L)
    # if Count_L >= 1:
    next_decimal = next_decimal % 50
    Count_X = int(next_decimal / 10)
    Print(Count_X)
    # if Count_X >= 1:
    next_decimal = next_decimal % 10
    Count_V = int(next_decimal / 5)
    Print(Count_V)
    # if Count_V >= 1:
    next_decimal = next_decimal % 5
    Count_I = int(next_decimal / 1)
    Print(Count_I)
    # if Count_I >= 1:
    next_decimal = input_decimal % 1000
    Min_String_normal = 'M'*Count_M + 'D'*Count_D + 'C'*Count_C+ 'L'*Count_L + 'X'*Count_X + 'V'*Count_V + 'I'*Count_I

    print('M'*Count_M + 'D'*Count_D + 'C'*Count_C+ 'L'*Count_L + 'X'*Count_X + 'V'*Count_V + 'I'*Count_I)

















import os

path = f'code{os.sep}files{os.sep}text{os.sep}'
filename = 'roman_number.txt'
input_file = open(path + filename, 'r')
print(input_file)
print(input_file.read())
input_file.close()

