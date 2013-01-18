# -----------------------------------------------------------------------------
# Methods...

import urllib
from bs4 import BeautifulSoup

def exchanges( print_pretty = False ) :

    """ Scrape list of exchanges from eoddata.com """

    page = urllib.urlopen("http://eoddata.com/symbols.aspx")
    soup = BeautifulSoup(page,"lxml")
    exchanges = {}
    for option in soup.find_all('option') :
        exchanges[str(option['value'])] = str(option.string)

    if print_pretty :
        from utils import printPrettyDict
        printPrettyDict( exchanges, 40 )

    return exchanges

def symbols( url, verbose = False ) :

    """ Scrape list of symbols from given url """

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

def scrape( filter ) :

    """ Scrape all symbols from eoddata.com """
    
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
    pickle.dump( exch, open("symbols.pkl","w") )

    return output_filename

def filter( input_filename, filter_list, keep ) :

    """ Filter symbols from pickled dictionary """
    
    import pickle
    input_file = open(input_filename,"r")
    input_dict = pickle.load(input_file)
    input_file.close()
    
    output_dict = {}
    for key,value in input_dict.items() :
        if keep and filter_list.count(key) == 0 : continue
        elif not keep and filter_list.count(key) > 0 : continue
        output_dict[key] = value

    output_filename = input_filename.split('.',1)

    if keep : output_filename = output_filename[0]+"_skimmed_"+'_'.join(filter_list)+"."+output_filename[1]
    else : output_filename = output_filename[0]+"_removed_"+'_'.join(filter_list)+"."+output_filename[1]

    output_file = open(output_filename,"w")
    pickle.dump( output_dict, output_file )
    output_file.close()

    return output_filename

def skim( i, f ) : return filter( i, f, True )
def remove( i, f ) : return filter( i, f, False )

def slim( input_filename ) :

    import pickle
    input_file = open(input_filename,"r")
    input_dict = pickle.load(input_file)
    input_file.close()
    
    output_dict = {}
    for key1,value1 in input_dict.items() :
        nested_dict = {}
        for key2,value2 in input_dict[key1].items() :
            nested_dict[key2] = value2[0]
        output_dict[key1] = nested_dict
    
    output_filename = input_filename.split('.',1)
    output_filename = output_filename[0]+"_slimmed."+output_filename[1]

    output_file = open(output_filename,"w")
    pickle.dump( output_dict, output_file )
    output_file.close()

    return output_filename

def number( input_filename ) :

    exchs = exchanges()

    import pickle
    file = open(input_filename,"r")
    exch = pickle.load(file)

    total = 0
    for key1,value1 in exch.items() :
        print "Exchange code:",key1,", Exchange name:",exchs[key1],", Number of businesses:",len(exch[key1])
        total = total + len(exch[key1])
    print "Total number of businesses:",total

def pretty( input_filename ) :

    import pickle
    input_file = open(input_filename,"r")
    input_dict = pickle.load(input_file)

    output_filename = input_filename.split('.',1)
    output_filename = output_filename[0]+"_pretty.txt"

    from utils import printPrettyDict
    printPrettyDict( input_dict, 40, output_filename )

    return output_filename

def histo( input_filename ):

    exch = exchanges()

    import pickle
    input_file = open(input_filename,"r")
    input_dict = pickle.load(input_file)

    import ROOT as r
    c = r.TCanvas("c1","c1",800,800);
    h = r.TH1F("Price","Price", 200,0.,20.);
    for key1,value1 in input_dict.items() :
        for key2,value2 in input_dict[key1].items() :
#            diff = value2[1]-value2[3]
            h.Fill( value2[3] );
#            if diff > 0. and diff < 0.01 : print key1,exch[key1],key2,value2
    h.Draw();
    c.Print("histo.pdf")

# -----------------------------------------------------------------------------
# Execute the code...

#printPretty( "symbols.pkl" )

#filter( "symbols.pkl", ["OPRA"], True )
#number( remove( "symbols.pkl", ["OPRA","OTCBB"] ) )
#number( skim( "symbols.pkl", ["NYSE"] ) )

#print pretty( slim( skim( "symbols.pkl", ["NASDAQ"] ) ) )

print pretty( slim( skim( "symbols.pkl", ["FOREX"] ) ) )

#print pretty("symbols_skimmed_NYSE.pkl")

#exchanges(True)

#histo( remove( "symbols.pkl", ["OPRA","OTCBB","NYMEX","CFE","LIFFE","FOREX"] ) )
#histo( skim( "symbols.pkl", ["OTCBB"] ) )

