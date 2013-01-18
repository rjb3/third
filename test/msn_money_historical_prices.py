
# -----------------------------------------------------------------------------
def msnMoneyHistoricalPrices( symbol, local = False ) :

    import bs4
    import utils

    if not len(symbol) : return None
    url = 'http://investing.money.msn.com/investments/equity-historical-price/?PT=7&D4=1&DD=1&D5=0&DCS=2&MA0=0&MA1=0&CF=0&nocookie=1&SZ=0&symbol='+symbol
#    url = 'http://investing.money.msn.com/investments/equity-historical-price/?symbol=us%3a' + symbol + '&CA=0&CB=0&CC=0&CD=0&D4=1&DD=1&D5=0&DCS=2&MA0=0&MA1=0&C5=0&C5D=0&C6=0&C7=0&C7D=0&C8=0&C9=0&CF=4&D8=0&DB=1&DC=1&D9=0&DA=0&D1=0&SZ=0&PT=11'

    url,page = utils.openUrl(url,local)
    print url
    soup = bs4.BeautifulSoup(page,"lxml")

    rows = soup.find_all("tr") 

    titles = []
    prices = {}
    dividends = {}
    for irow,row in enumerate( rows ) :
        cols = row.find_all("td")

        # Extract titles from table header 
        headers = row.find_all("th")
        for header in headers :
            entries = header.find_all(text=True)
            entry = entries[1].strip()
            if not len(entry) : continue
            titles.append(str(entry))

        # Extract ex-dividend dates, dividends paid, and share price
        if len(cols) == 3 :
            date = 0
            div = 0.
            price = 0.
            try :
                entries = cols[0].find_all(text=True)
                entry = entries[1].strip()
                if len(entry) : date = utils.makeEpochTime(str(entry),'%m/%d/%Y')
            except ValueError :
                date = 0
            try :
                entries = cols[1].find_all(text=True)
                entry = entries[1].strip().split(' ')[0]
                if len(entry) : div = float(entry)
            except ValueError :
                div = 0.
            try :
                if irow < len(rows) :
                    entries = rows[irow+1].find_all("td")[4].find_all(text=True)
                    entry = entries[1].strip()
                    price = float(entry) 
                else : 
                    price = 0.
            except ValueError : 
                price = 0.
            if date != 0 :
                dividends[date] = (div,price)

        # Loop through rows and extract share prices
        else :
            tuple = ()
            if len(cols) != 6 : continue
            for icol,col in enumerate( cols ) :
                entries = col.find_all(text=True)
                entry = entries[1].strip()
                if not len(entry) : continue
                try :
                    secs = utils.makeEpochTime(str(entry),'%m/%d/%Y')
                    tuple = tuple + (secs,)
                except ValueError : 
                    tuple = utils.extractData(entry,tuple)
            prices[tuple[0]] = tuple[1:]

    return titles,prices,dividends
