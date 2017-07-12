#!/usr/bin/env python
import sys


# Checks if number of arguments is equal to one
if (len(sys.argv) != 3):
    print("function allows only two positive integer arguments")
    sys.exit(1)


num1 = sys.argv[1]
num2 = sys.argv[2]
sumofnumber = 0


#Checks if argument is less than 0 or isn't integer
try:
    if (int(num1) < 0) or (int(num2) < 0):
        print("Bus ticket has to have positive value")
        sys.exit(1)
except ValueError:
    print("Enter positive integer numbers")
    sys.exit(1)


#Checks if the first argument isn't bigger than the second one
if int(num2) < int(num1):
    print("The second number has to be larger than the first one")
    sys.exit(1)


#Checks if arguments contain right number of digits
if (len(num1) > 6) or (len(num2) > 6):
    print("The number has to contain no more than 6 digits to be a bus ticket")
    sys.exit(1)


#Calculates the quantity of lucky numbers
for i in range(int(num1), int(num2)+1):
    if len(str(i)) < 6:
        i = str(i).zfill(6)
    else:
        i = str(i)
    sum1 = sum(map(int,i[0:3]))
    sum2 = sum(map(int,i[-3:]))
    if sum1 == sum2:
        sumofnumber += 1


print("##################")
print("# Sum of numbers #")
print("##################")
Str = "# "+str(sumofnumber)
for n in range(0,14-len(str(sumofnumber))):
    Str+=" "
Str+=" #"
print(Str)
print("##################")
