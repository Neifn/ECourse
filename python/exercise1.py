#!/usr/bin/env python

encodings=['UTF-8', 'CP1251', 'Latin-1']
def function(text):
    # Transforming into unicode
    text=text.encode('UTF-8')
    for i in encodings:
        # Decoding into other encodings
        print(text.decode(i))

function("Привет")
