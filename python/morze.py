#!/usr/bin/env python
import re
import sys


alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
alphabet = alphabet.split(",")
morze_key= ["^_^^^","^^^_^_^_^","^^^_^_^^^_^","^^^_^_^","^","^_^_^^^_^","^^^_^^^_^","^_^_^_^","^_^","^_^^^_^^^_^^^","^^^_^_^^^","^_^^^_^_^","^^^_^^^","^^^_^","^^^_^^^_^^^","^_^^^_^^^_^","^^^_^^^_^_^^^","^_^^^_^","^_^_^","^^^","^_^_^^^","^_^_^_^^^","^_^^^_^^^","^^^_^_^_^^^","^^^_^_^^^_^^^","^^^_^^^_^_^"]

# Creating dictionary and assigning to the letters corresponding morze values
morze_dict = {}
for i in range(len(alphabet)):
    morze_dict[alphabet[i]] = morze_key[i]


# Use this function to translate morze code into latin characters
def decode_morze(encoded):
    # inverting dictionary
    inv_dict = {v: k for k, v in morze_dict.items()}
    decoded = ""
    n = ""

    # Checking for characters not in morze code
    check_code = re.sub('_______', '___', encoded)
    check_code = check_code.split("___")
    for element in check_code:
        if element not in morze_key:
            print("Enter text containing only symbols from morze code")
            sys.exit(1)
    

    # Spliting user input into words and than letters and tranlating them
    encoded = encoded.split("_______")
    for i in encoded:
        n = i.split("___")
        for letter in range(len(n)):
            if letter != len(n)-1:
                decoded+=str(inv_dict.get(n[letter])) 
            else:
                decoded+=str(inv_dict.get(n[letter])) + " "
    decoded = decoded[:-1]
    return decoded


# Use this function to translate latin characters into morze code
def encode_morze(text):
    text = text.lower()
    check_text = re.sub(' ', '', text)

    # Checking for characters not in latin alphabet
    for element in check_text:
        if element not in alphabet:
            print("Enter text containing only letters from latin alphabet and spaces")
            sys.exit(1)

    # Tranlating user input into morze
    new_text=""
    text = text.split(" ")
    for i in text:
        for n in range(len(i)):
            if n != len(i)-1:
                new_text+=str(morze_dict.get(i[n])) + "___"
            else:
                new_text+=str(morze_dict.get(i[n])) + "_______"
    new_text = new_text[:-7]
    return new_text
