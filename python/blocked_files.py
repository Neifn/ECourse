#!/usr/bin/env python3


import sys


def access(text):
    text_list=text.split('\n')

    # Check
    try:
        number_of_files=int(text_list[0])
        number_of_actions=int(text_list[number_of_files+1])
    except ValueError:
        print('Input data isn\'t correct')
        sys.exit(1)

    # Check
    if len(text_list) != number_of_files+number_of_actions+2:
        print('Input data isn\'t correct')
        sys.exit(1)
    check_list=[]
    for item in range(1, number_of_files+1):
            check_list.append(text_list[item].split(' ')[0])

    # Main Cycle
    for i in range(number_of_files+2, len(text_list)):
        action_list=text_list[i].split(' ')

        # Check
        if action_list[1] not in check_list or len(action_list) < 2:
            print('Input data isn\'t correct')
            sys.exit(1)

        for j in range(1, number_of_files+1):
            item_list=text_list[j].split(' ')
            if action_list[0] == 'read':
                if action_list[1] in item_list[0]:
                    if 'R' in item_list and 'R' != item_list[0]:
                        print('OK')
                    else:
                        print('Access denied')
            elif action_list[0] == 'write':
                if action_list[1] in item_list[0]:
                    if 'W' in item_list and 'W' != item_list[0]:
                        print('OK')
                    else:
                        print('Access denied')
            elif action_list[0] == 'execute':
                if action_list[1] in item_list[0]:
                    if 'X' in item_list and 'X' != item_list[0]:
                        print('OK')
                    else:
                        print('Access denied')
            else:
                print('Unknown operation {}'.format(action_list[0]))


access("4\nhelloworld.exe R X\npinglog W R\nnya R\ngoodluck X W R\n5\nread nya\nwrite helloworld.exe\nexecute nya\nread pinglog\nwrite pinglog")
