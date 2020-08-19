import sys

try:
    x = int(input('x: '))
    y = int(input('y: '))
except ValueError:
    print('Error: Ivalid input')
    sys.exit(1)

try:
    result = x/y
except ZeroDivisionError:
    print('Error: Cannot divide by 0')
    sys.exit(1)
# how to exiting the program after a Error, use  the module in Python call sys. You need import 
# the model ate the beginning of the code.   
print(f'{x} / {y} = {result}')