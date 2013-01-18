# -----------------------------------------------------------------------------
def msnMoneyTenYearSummary( symbol, local = False ) :

    import bs4
    import utils

    if not len(symbol) : return None
    url = 'http://investing.money.msn.com/investments/financial-statements?symbol=' + symbol
    url,page = utils.openUrl(url,local)
    print url
    soup = bs4.BeautifulSoup(page,"lxml")

    # Extract tables 
    tables = soup.find_all("table",{"class":"mnytbl"})

    # Parse income statement table
    income = {}
    for row in tables[0].find_all("tr") :
        cols = row.find_all("td")
        if len(cols) == 0 : continue
        tuple = ()
        for icol,col in enumerate( cols ) :
            entry = col.find_all(text=True)[1].strip()
            if icol == 0 :
                try :
                    secs = utils.makeEpochTime(str(entry),'%m/%y')
                    tuple = tuple + (secs,)
                except ValueError : 
                    tuple = tuple + (str(entry),)
            else :
                tuple = utils.extractData(entry,tuple)

        income[tuple[0]] = tuple[1:]

    # Parse balance sheet table
    balance = {}
    for row in tables[1].find_all("tr") :
        cols = row.find_all("td")
        if len(cols) == 0 : continue
        tuple = ()
        for icol,col in enumerate( cols ) :
            entry = col.find_all(text=True)[1].strip()
            if icol == 0 :
                try :
                    secs = utils.makeEpochTime(str(entry),'%m/%y')
                    tuple = tuple + (secs,)
                except ValueError : 
                    tuple = tuple + (str(entry),)
            else :
                tuple = utils.extractData(entry,tuple)
        balance[tuple[0]] = tuple[1:]

    return income,balance
