from bs4 import BeautifulSoup
from urllib import urlopen
tarurl = "http://securityblog.jp/security_wordlist.html"

res = urlopen(tarurl).read().decode('utf-8')
soup = BeautifulSoup(res, 'html.parser')

tmp = soup.find_all('a')
for links in tmp:
     if links.get('href')[0:28] == "http://securityblog.jp/words":
        cont = urlopen(links.get('href')).read().decode('utf-8')
        contSoup = BeautifulSoup(cont, 'html.parser')
        try:
            tmpTitle = contSoup.find('h1').get_text(strip=True).encode('utf-8', 'ignore').decode('utf-8')
            print "Title : %s" % tmpTitle
            print "Contents : "
            for conts in contSoup.find(id='words').find_all('p'):
                print conts.get_text(strip=True).encode('utf-8', 'ignore').decode('utf-8')
        except:
            print "One more~~"
