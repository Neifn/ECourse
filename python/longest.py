#!/usr/bin/env python
user_input = "lokori llo lard hardery labradorium"
user_list = user_input.split()
list_of_longs = []
for element in user_list:
    check_value = False
    for i in user_list:
        if len(element) >= len(i):
            check_value = True
        else:
            check_value = False
    if check_value == True: 
        list_of_longs.append(element)
print(list_of_longs)

