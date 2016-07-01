# python-auto-test.py

import requests
import re

def main():
    
#    url = 'http://localhost/test.php'
    url = 'http://10.248.90.236/testsite/ctf1.php'
    answer = ''
    sessionId = 'k9e5dpsdsl29t6h15us189ska5'
    cookies = {'PHPSESSID':sessionId}
    
    for i in range(0,120):
        payload = {'answer':answer}
        res = requests.get(url, params=payload, cookies=cookies)
        print(res.text)
        exp = re.findall('\d [\+\-\/\*] \d', str(res.text))
        for e in exp:
#            print(e)
            answer = eval(e)
    

if __name__ == '__main__':
    main()
