import lxml.html
import csv

#doc = lxml.html.parse('http://finance.yahoo.com/q/os?s=lly&m=2011-04-15')
#doc = lxml.html.parse('http://finance.yahoo.com/q/os?s=LLY&m=2012-09')
doc = lxml.html.parse('scrape.html')

# find the first table contaning any tr with a td with class yfnc_tabledata1
table = doc.xpath("//table[tr/td[@class='yfnc_tabledata1']]")[0]

print(doc.getpath(table)) 

with open('results.csv', 'wb') as f:
    cf = csv.writer(f)
    # find all trs inside that table:
    for tr in table.xpath('./tr'):
        # add the text of all tds inside each tr to a list
        row = [td.text_content().strip() for td in tr.xpath('./td')]
        # write the list to the csv file:
        cf.writerow(row)
        #print row
