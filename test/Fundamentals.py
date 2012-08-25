class Fundamentals :

    """A class holding Fundamentals of a given company."""

    # Ticker name
    self.ticker_symbol = ""

    # Default constructor
    def __init__(self):
        self.ticker_symbol = ""


        
    # EPS (Earnings per share)
    
        
    i = 12345
    
    def f(self):
        return 'hello world'


import urllib

# Open webpage
url = 'http://investing.money.msn.com/investments/financial-statements?symbol=AAPL'
page = urllib.urlopen(url)

# Parse webpage
from bs4 import BeautifulSoup
soup = BeautifulSoup(page,"lxml")

# Find tables 
table = soup.find_all("table",{"class":" mnytbl"})

from datetime import date

# Income statement
for row in table[0].find_all("tr"):
    d = date(1,1,1)
    for cell in row.find_all("td"):
        # cell data
        data = cell.find_all(text=True)[1].strip()
        print data
        if data.count('/') > 0 :
            if ( data.split('/')[0] > int(date.today().year)-2000 ) : 
                d = date(int(data.split('/')[0])+2000,int(data.split('/')[1]),1)
            else :
                d = date(int(data.split('/')[0])+1900,int(data.split('/')[1]),1)
            print "date:",d.isoformat()
        else :
            if data.count(' Mil') > 0 :
                print "millions:", float(data.replace(' Mil',''))*1.e6
            elif data.count(' Bil') > 0 :
                print "billions:", float(data.replace(' Bil',''))*1.e9
            else :
                print "normal:",float(data)
                

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
