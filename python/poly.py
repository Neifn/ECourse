#!/usr/bin/env python
import sys


try:
    students = int(input("Enter the number of students:" ))
except ValueError:
    print("The number of students has to be integer")
    sys.exit(1)

num_of_langs = []
# Creating list containing number of languages each student knows
for element in range(students):
     try:
         num_of_langs.append(int(input("Enter the number of languages student knows:" )))
     except ValueError:
         print("The number of languages has to be integer")
         sys.exit(1)

# Adding languages known by students to the list of lists
language = [[] for x in range(students)]
for i in range(students):
     for lang in range(num_of_langs[i]):
         print("Enter languages that student " +str(i+1) +" knows")
         language[i].append(input())

# Countig number of languages known by all students
min_lang_list = []
min_lang_count = int()
for lang in min(language):
    if all(lang in item for item in language):
        min_lang_count+=1
        min_lang_list.append(lang)
print("Number of languages known by all students:" +str(min_lang_count))
print("Languages known by all students:")
for lang in sorted(min_lang_list):
    print(lang)

# Creating list of all languages without repetitions
list_of_lang = []
for i in range(len(language)):
    for j in language[i]:
        if j not in list_of_lang:
            list_of_lang.append(j)
print("Number of languages known by students:" +str(len(list_of_lang)))
print("Languages known by some students:")
for lang in sorted(list_of_lang):
    print(lang)


