import lxml.html
import csv

doc = lxml.html.parse('http://investing.money.msn.com/investments/stock-cash-flow/?symbol=us%3AAAPL&stmtView=Ann')

# find the first table contaning any tr with a td with class yfnc_tabledata1
table = doc.xpath("//table/tbody/tr/td[@id='PurchaseofFixedAssets']")[0] 

with open('free_cash_flow.csv', 'wb') as f:
    cf = csv.writer(f)
    # find all trs inside that table:
    for tr in table.xpath('./tr'):
        # add the text of all tds inside each tr to a list
        row = [td.text_content().strip() for td in tr.xpath('./td')]
        # write the list to the csv file:
        #cf.writerow(row)
        print row
