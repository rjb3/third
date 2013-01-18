# -----------------------------------------------------------------------------
def msnMoneyCashFlow( symbol, local = False ) :

    import bs4
    import utils

    if not len(symbol) : return None
    url = 'http://investing.money.msn.com/investments/stock-cash-flow/?symbol=' + symbol + '&stmtView=Ann'
    url,page = utils.openUrl(url,local)
    print url
    soup = bs4.BeautifulSoup(page,"lxml")

    rows = soup.find_all("tr") 
    ncols = len(rows[-1].find_all("td"))-1
    titles = []
    tuples = [() for x in range(ncols)]
    for irow,row in enumerate( rows ) :
        for icol,col in enumerate( row.find_all("td") ) :
            entries = col.find_all(text=True)
            index = None
            if len(entries) == 1 : index = 0
            elif len(entries) == 3 : index = 1
            elif len(entries) == 7 : index = 4
            else : continue
            entry = entries[index].strip()
            if len(entry) : 
                if icol == 0 : 
                    titles.append(str(entry))
                else :
                    dates = {1:'%Y',2:'%m/%d/%Y',5:'%m/%d/%Y'}
                    try :
                        date = dates[irow]
                        secs = utils.makeEpochTime(str(entry),date)
                        tuples[icol-1] = tuples[icol-1] + (secs,)
                    except KeyError : 
                        tuples[icol-1] = utils.extractData(entry,tuples[icol-1])
                
    dict = {}
    for col in range(len(tuples)) :
        dict[tuples[col][0]] = tuples[col][1:]

    return titles,dict
