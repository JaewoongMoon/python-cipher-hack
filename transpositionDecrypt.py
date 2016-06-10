# Transposition cipher Decryption
# http://inventwithpython.com/hacking (BSD Licensed)

import math, pypercliip

def main():
    myMessage = 'Cenoonommstmme oo snnio. s s c'
    myKey = 8

    plainText = decryptMessage(myKey, myMessage)

    # Print with a | (called "pipe" character) after it in case
    # there are spaces at the end of the decrypted message. 
    print(plainText + '|')

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    #