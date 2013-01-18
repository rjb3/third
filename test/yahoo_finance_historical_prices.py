
# -----------------------------------------------------------------------------
def yahooFinanceHistoricalPrices( symbol, 
                                  from_date = None, 
                                  to_date = None, 
                                  freq = "d", 
                                  local = False ) :

    #http://www.gummy-stuff.org/Yahoo-data.htm
    import urllib2
    import csv
    import StringIO
    import datetime 

    if from_date == None :
        print "not set from"
        from_date = date.date(1900,1,1)

    if to_date == None :
        print "not set to"
        to_date = date.date.today()

    if ["d","w","m","v"].count(freq) != 1 :
        freq = "d"

    url = "http://ichart.finance.yahoo.com/table.csv?s=" + symbol
    if not local :
        url = 'http://ichart.finance.yahoo.com/table.csv?' + \
            's=' + symbol + \
            '&a=' + str(from_date.month-1) + \
            '&b=' + str(from_date.day) + \
            '&c=' + str(from_date.year) + \
            '&d=' + str(to_date.month-1) + \
            '&e=' + str(to_date.day) + \
            '&f=' + str(to_date.year) + \
            '&g=' + freq + \
            '&ignore=.csv' 

    print url
    url,f = openUrl(url,local)

    if local : data = StringIO.StringIO(f.read())
    else : data = StringIO.StringIO(f.read())

    dialect = csv.Sniffer().sniff(data.read(1024))
    data.seek(0)
    prices = csv.reader(data,dialect)

    titles = []
    dict = {}
    for row in prices :
        tuple = ()
        for icol,col in enumerate(row) :
            entry = col.strip()
            if icol == 0 :
                try :
                    secs = makeEpochTime(str(entry),'%Y-%m-%d')
                    tuple = tuple + (secs,)
                except ValueError : 
                    tuple = tuple + (str(entry),)
            else :
                tuple = extractData(entry,tuple)
        if tuple[0] != "Date" :
            dict[tuple[0]] = tuple[1:]
        else :
            titles = [x for x in tuple[1:]]

    return titles,dict
