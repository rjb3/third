import urllib
from bs4 import BeautifulSoup

# -----------------------------------------------------------------------------
# Methods...

def exchanges( verbose = False ) :
    page = urllib.urlopen("http://eoddata.com/symbols.aspx")
    soup = BeautifulSoup(page,"lxml")
    exchanges = {}
    for option in soup.find_all('option') :
        if verbose : print option['value'],option.string
        exchanges[str(option['value'])] = str(option.string)
    return exchanges

def symbols( url, verbose = False ) :
    if not len(url) : return None
    if verbose : print "Retrieving symbols from: ",url
    page = urllib.urlopen(url)
    soup = BeautifulSoup(page,"lxml")
    dict = {}
    for row in soup.find_all('tr',{"class","ro"}) :
        cells = row.find_all("td")
        if len(cells) == 0 : continue
        tuple = ()
        for cntr,cell in enumerate( cells ) :
            if cell.string == None : continue
            if cntr > 1 : 
                tuple = tuple + (float(cell.string.replace(',','')),)
            else :
                tuple = tuple + (str(cell.string.replace('\"','').replace('\'','')),)
        dict[tuple[0]] = tuple[1:]
    return dict

# -----------------------------------------------------------------------------
# Execute the code...

# 1 = write all symbols 
# 2 = read all symbols
# 3 = skim US options symbols
# 4 = read US options symbols
# ELSE print list of exchanges
option = 4


if option == 1 :

    verbose = False
    base_url = "http://eoddata.com/stocklist/XXX/YYY.htm"
    alphabet = map(chr,range(65,91)) + map(str,range(0,10))

    total = 0
    exch = {}
    for key,value in exchanges(True).items() :
        if verbose : print "Exchange:",value,"Code:",key
        symb = {}
        for letter in alphabet :
            url = base_url.replace('XXX',key).replace('YYY',letter)
            if verbose : print value,key,letter,url
            symb = dict(symb.items() + symbols(url,True).items())
        exch[key] = symb
        total = total + len(exch[key].items())
        print "#:",len(exch),", Exchange:",value,", Code:",key,", Number of symbols:",len(exch[key])
    print "Total number of symbols:",total
            
    from utils import printPrettyDict
    printPrettyDict(exch,40)
    
    import pickle
    pickle.dump( exch, open("ticker_symbols","w") )

elif option == 2 : 

    tmp = exchanges(True)

    import pickle
    from utils import printPrettyDict
    file = open("ticker_symbols","r")
    exch = pickle.load(file)
    #printPrettyDict( exch, 40 )

    total = 0
    for key1,value1 in exch.items() :
        print "Exchange code:",key1,"Number of businesses:",len(exch[key1])
        total = total + len(exch[key1])
#        for key2,value2 in exch[key1].items() :
#            print "Ticker symbol:",key2,"Business name:",value2[0]
    print "Total number of businesses:",total

    temp = {}
    tuple = ("OPRA",tmp["OPRA"])
    temp[tuple] = exch["OPRA"]
    print len(temp[tuple])

    import pickle
    pickle.dump( temp, open("symbols_us_options.pkl","w") )

elif option == 3 : # skim US options symbols

    tmp = exchanges(True)

    import pickle
    from utils import printPrettyDict
    file = open("symbols_all.pkl","r")
    exch = pickle.load(file)

    temp = {}
    tuple = ("OPRA",tmp["OPRA"])
    temp[tuple] = exch["OPRA"]
    print len(temp[tuple])

    import pickle
    pickle.dump( temp, open("symbols_us_options.pkl","w") )

elif option == 4 : # read US options symbols

    import pickle
    #from utils import printPrettyDict
    file = open("symbols_us_options.pkl","r")
    exch = pickle.load(file)
    utils.printPrettyDict( exch, 40 )

else : 

    print exchanges()
