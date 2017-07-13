#!/usr/bin/env python
import sys
import re


alphabet = 'abcdefghijklmnopqrstuvwxyz'
cypher_key = 'aaaaabbbbbabbbaabbababbaaababaab'
key = sys.argv[1].replace(" ", "")


# Cheks if number of arguments is equal to one
if (len(sys.argv) != 2):
    print("function allows only one argument")
    sys.exit(1)


# Cheks if argument contains only letters
if not key.isalpha():
    print("Argument has to contain only letters")
    sys.exit(1)


# Main calls for Decryption and Transform functions to decypher incrypted message
def main():
    decrypted_msg = ""
    decryption_dict_var = Decryption_dict(alphabet, cypher_key)
    for i in TransformPhrase(key):
        try:
            decrypted_msg += decryption_dict_var.get(i)
        except TypeError:
            print("The message is crypted by unknown key")
            sys.exit(1)
    print(decrypted_msg)


# Function creates dictionary in which every character in alphabet corresponds to specific part of the key var
def Decryption_dict(alphabet, cypher_key):
    # Transformation of alphabet var into list
    alphabet = re.sub(r'([a-z])', r',\1', alphabet)
    alphabet = alphabet[1:]
    alphabet_list = alphabet.split(",")
    # Creation of the dictionary
    cypher_dict = {}


    # Assigning parts of the key to elements of the alphabet list
    for i in range(len(alphabet_list)):
        cypher_dict[alphabet_list[i]] = cypher_key[i:5+i]
    cypher_dict = {v: k for k, v in cypher_dict.items()}
    return(cypher_dict)


# Transformation of the argument
def TransformPhrase(key):
    n = 0
    # Checking if length of the key can be divided by 5 and replacing all lowercase characters by 'a'
    if (len(key) + n) % 5 != 0:
        while True:
            if (len(key) + n) % 5 != 0:
                n = n -1
            else:
                key = re.sub(r'([a-z])', r'a', key[:n])
                break
    else:
        key = re.sub(r'([a-z])', r'a', key)
    # Replacing all uppercase characters by 'b' and dividing string into list with elements of length 5
    key = re.sub(r'([A-Z])', r'b', key)
    key = re.findall('.....', key)
    return(key)


(__name__ == '__main__') and main()
