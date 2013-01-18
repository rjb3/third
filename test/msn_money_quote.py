# -----------------------------------------------------------------------------
def msnMoneyQuote( symbol, local = False ) :
    
    import bs4
    import utils

    if not len(symbol) : return None
    url = 'http://investing.money.msn.com/investments/stock-price?symbol=' + symbol
    url,page = utils.openUrl(url,local)
    print url
    soup = bs4.BeautifulSoup(page,"lxml")

    # Extract date stamp from below "details" table
    footers = soup.find_all("span",{"class":"foot"})
    string = footers[0].find_all(text=True)[0].strip().split(' ')[2]
    date = utils.makeEpochTime(string,'%m/%d/%Y')

    # Extract tables 
    tables = soup.find_all("table",{"class":"mnytbl"})

    # Parse "details" table
    details = {}
    tuple = ()
    cntr = 0
    for row in tables[0].find_all("tr") :
        cells = row.find_all("td")
        if len(cells) == 0 : continue
        data = cells[1].find_all(text=True)[1].strip()
        tuple = utils.extractData(data,tuple)
        cntr = cntr + 1
    details[date] = tuple

    # Parse "financial highlights" table
    highlights = {}
    tuple = ()
    cntr = 0
    for row in tables[1].find_all("tr") :
        cells = row.find_all("td")
        if len(cells) == 0 : continue
        index = 2 if ( cntr == 2 or cntr == 3 ) else 1
        data = cells[1].find_all(text=True)[index].strip()
        tuple = utils.extractData(data,tuple)
        cntr = cntr + 1
    highlights[date] = tuple

    return details,highlights
