#!/usr/bin/env python
def sort_list(user_input):
    import sys


    newlist=[]
    # Checking if user input is of list type
    if type(user_input) != list:
        print("User input has to be a list")
        sys.exit(1)
    # Checking if an item from 'user_input' list is already added to 'newlist'
    for i in user_input:
        if i not in newlist:
            newlist.append(i)
    return(newlist)
