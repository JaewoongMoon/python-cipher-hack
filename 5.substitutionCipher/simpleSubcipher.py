# Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip, sys, random

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    myMessage = 'If a man is offered a fact which goes against his instincts, he will scrutinize it closely, and unless the evidence is overwhelming, he will refuse to believe it. If, on the other hand, he is offered something which affords a reason for acting in accordance to his instincts, he will accept it even on the slightest evidence. The origin of myths is explained in this way. - Bertrand Russell'

    myMessage2 = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. - Facjclxo Ctrramm'

    myKey = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    myMode = 'decrypt' # set to 'encrypt' or 'decrypt'

    checkValidKey(myKey)

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage2)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage2)
    print('Using key %s' % (myKey))
    print('The %sed message is :' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard')


# A simple substitution key string value is only valid 
# if it has each of the characters in the symbol set 
# with no duplicate or missing letters. 
# We can check if a string value is a valid key by sorting it
# and the symbol set into alphabetical order and checking if are equal.
# (Although LETTERS is already in alphabetical order, 
# we still need to sort it since it could be expanded 
# to contain other characters.
def checkValidKey(key):
    keyList = list(key)
    letterList = list(LETTERS)
    keyList.sort()
    letterList.sort()
    if keyList != letterList:
        sys.exit('This is an error in the key or symbol set.')

def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')

def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


# The encryption process is very simple: for each letter in the message parameter,
# we look up its index in LETTERS and replace it with the letter at that 
# same index in the key parameter. 
# To decrypt we de the opposite: we look up the index in key and replace it
# with the letter at the same index in the LETTERS. 

def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. 
        # We just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

    # loop through each symbol in the message
    for symbol in message:
        if symbol.upper() in charsA:
            # encrypt/decrypt the symbol 
            symIndex = charsA.find(symbol.upper())
            if symbol.isupper():
                translated += charsB[symIndex].upper()
            else:
                translated += charsB[symIndex].lower()
        else:
            # symbol is not in LETTERS, just add it
            translated += symbol 

    return translated

def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
