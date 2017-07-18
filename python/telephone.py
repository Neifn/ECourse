#!/usr/bin/env python
def function(number):
    import itertools


    # Deleting all characters used only once by comparing them to the nearby characters
    deleted_single = []
    for n in range(len(number)):
        if (n == 0):
            if (number[n] == number[n+1]):
                deleted_single.append(number[n])
        elif (n == (len(number)-1)):
            if (number[n] == number[n-1]):
                deleted_single.append(number[n])
        else:
            if (number[n] == number[n-1]) or (number[n] == number[n+1]):
                deleted_single.append(number[n])
    
    # Joining the list we got from previous operations and removing repeated characters
    new_string = ''.join(deleted_single)
    new_string = ''.join(ch for ch, _ in itertools.groupby(new_string))

    # Replacing '#' with the number prior to it 
    phone_number = []
    for i in range(len(new_string)):
        value= ""
        if (i == 0) and (new_string[0] == "#"):
            pass
        else:
            if new_string[i] == "#":
                value = new_string[i-1]
                phone_number.append(value)
            else:
                phone_number.append(new_string[i])
    return(print(''.join(phone_number)))

function("4434###552222311333661")
