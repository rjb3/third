# -----------------------------------------------------------------------------
def msnMoneyCompanyProfile( symbol, local = False ) :

    import bs4
    import utils
    import datetime

    if not len(symbol) : return None
    url = 'http://investing.money.msn.com/investments/company-report?symbol=' + symbol
    url,page = utils.openUrl(url,local)
    print url
    soup = bs4.BeautifulSoup(page,"lxml")

    tables = soup.find_all("table",{"class":"mnytbl"})
    text = tables[1].find_all("span")[0].find_all(text=True)[0].strip().encode("utf-8")

    d = datetime.date(1900,1,1)

    length = {0:len(text)}
    profile = {0:text}
    
    return length,profile
