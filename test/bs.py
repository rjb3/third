import urllib

f = open('./output.txt', 'w')

#url = 'http://investing.money.msn.com/investments/stock-cash-flow/?symbol=us%3AAAPL&stmtView=Ann'
#url = 'http://finance.yahoo.com/q/os?s=LLY&m=2012-09'
url = 'http://finance.yahoo.com/q/op?s=AAPL'

page = urllib.urlopen(url)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page,"lxml")

#for link in soup.find_all('a'):
#    print(link.get('href'))

#print(soup.get_text())

#f.write(soup.prettify())

#print(soup.find_all('table'))

#len(list(soup.descendants))

#print(soup.findAll(text="AAPL120824C00560000")[0].parent.parent.parent).prettify()

optionsTable = [[x.text for x in y.parent.contents] for y in soup.findAll('td', attrs={"class" : "yfnc_h", "nowrap" : "nowrap"})]

for y in soup.findAll('td', attrs={"class" : "yfnc_h", "nowrap" : "nowrap"}) :
    print "y: " 
    for x in y.parent.contents :
        print x.text

table = soup.find("table",{"class": "class_name"})
for row in table.findAll("tr"):
    for cell in row.findAll("td"):
        print cell.findAll(text=True)
 
#for table in soup.find_all('table') :
#    for tr in table.find_all('tr') :
#        for td in tr.find_all('td') :
#            #if ( td['class'][0] == 'yfnc_tabledata1' ) :
#                #print(td)
#            print(td.get('class'))
#



#optionsTable = [[x.text for x in y.parent.contents] for y in soup.findAll('td', attrs={"class" : "yfnc_h", "nowrap" : "nowrap"})]

#print(optionsTable)

#soup.findAll(text="AAPL120824C00560000")
