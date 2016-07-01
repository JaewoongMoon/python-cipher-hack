# Transposition Cipher Hacker

import pyperclip, detectEnglish, transpositionDecrypt

def main():
    # You might want to copy & paste this text from the source code at
    # http://invpy.com/transpositionHacker.py

    myMessage = """Cb b rssti aieih rooaopbrtnsceee er es no npfgcwu  plri ch nitaalr eiuengiteehb(e1  hilincegeoamn fubehgtarndcstudmd nM eu\neacBoltaeteeoinebcdkyremdteghn.aa2r81a\ncondari\nfmps" tad   l t oisn sit u1rnd stara nvhn fsedbh ee,n  e necrg6  8nmisv l nc muiftegiitm tutmg cm shSs9fcie ebintcaets h\n aihda cctrhe ele 1O7 aaoem waoaatdahretnhechaopnooeapece9etfncdbgsoeb uuteitgna.rteoh add\ne,D7c1Etnpneehtn beete" evecoal lsfmcrl iu1cifgo ai.\nsl1rchdnheev sh meBd ies e9t)nh,htcnoecplrrh ,ide hmtlme. pheaLem,toeinfgn t e9yce da\' eN eMp a ffn Fc1o ge eohg dere.eec\ns nfap\nyox hla\nyon. lnrnsreaBoa t,e eitsw il\nulpbdofgBRe bwlmprraio po  droB wtinue r Pieno nc ayieeto\'lulcih sfnc  ownaSserbereiaSm-eaiah, nnrttgcC  maciiritvledastinideI  nn rms iehn tsigaBmuoetcetias rn"""

    myMessage2 = """Uryyb, jrypbzr gb Frphevgl FNXHEN. Jr ubcr lbh'ir rawblrq gur pbasrerapr."""

    hackedMessage = hackTransposition(myMessage2)

    if hackedMessage == None:
        print('Failed to hack encryption.')
    else:
        print('Copying hacked message to clipboard:')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)

def hackTransposition(message):
    print('Hacking...')

    # Python programs can be stopped at any time by pressing Ctrl-C (on
    # Windows) or Ctrl-D (on Mac and Linux)
    print('(Press Ctrl-C or Ctrl-D to quit at any time.)')

    # brute-force by looping through every possible key
    for key in range(1, len(message)):
        print('Trying key #%s...' % (key))

        decryptedText = transpositionDecrypt.decryptMessage(key, message)
#        print('decryptedText : %s' % (decryptedText))

        if detectEnglish.isEnglish(decryptedText):
            # Check with user to see if the decrypted key has been found. 
            print()
            print('Possible encryption hack:')
            print('Key %s: %s' % (key, decryptedText[:100]))
            print()
            print('Enter D for done, or just press Enter to continue hacking:')
            response = input('> ')
            
            if response.strip().upper().startswith('D'):
                return decryptedText

    return None

if __name__ == '__main__':
    main()
