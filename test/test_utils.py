from msn_money import *

do_local = True

option = ["BALANCE"]
symbols = ["AAPL"]
#symbols = ["AAPL","AGNC"]

for symbol in symbols :

    if option.count("ALL") or option.count("BALANCE") :
        names,balance = msnMoneyBalanceSheet(symbol,do_local)
        utils.printPrettyDict(balance)
        print names
        print len(names),[len(balance[x]) for x in balance.keys()]
                
    if option.count("ALL") or option.count("CASH") :
        names,cash = msnMoneyCashFlow(symbol,do_local)
        utils.printPrettyDict(cash)
        print names
        print len(names),[len(cash[x]) for x in cash.keys()]

    if option.count("ALL") or option.count("HIST") :
        titles,prices,dividends = msnMoneyHistoricalPrices(symbol,do_local)
        utils.printPrettyDict(prices)
        print titles
        utils.printPrettyDict(dividends)
        
    if option.count("ALL") or option.count("INCOME") :
        names,income = msnMoneyIncomeStatement(symbol,do_local)
        utils.printPrettyDict(income)
        print names
        print len(names),[len(income[x]) for x in income.keys()]
        
    if option.count("ALL") or option.count("QUOTE") :
        details,highlights = msnMoneyQuote(symbol,do_local)
        utils.printPrettyDict(details)
        utils.printPrettyDict(highlights)

    if option.count("ALL") or option.count("TEN") :
        income,balance = msnMoneyTenYearSummary(symbol,do_local)
        utils.printDict(income)
        utils.printPrettyDict(balance)

    if option.count("ALL") or option.count("PROFILE") :
        length,profile = msnMoneyCompanyProfile(symbol,do_local)
        utils.printDict(length)
        utils.printPrettyDict(profile)

    if option.count("YHIST") :
        from datetime import date
        titles,dict = yahooFinanceHistoricalPrices("AAPL",
                                                   from_date=date(2010,1,1),
                                                   to_date=date.today(),
                                                   freq="d",
                                                   local=False)
        utils.printPrettyDict(dict)
        print len(dict)
        print titles
    
if option.count("DATE") :
    import datetime
    print utils.makeEpochTime( datetime.datetime.now() )
    
    print utils.extractDate("")
    print utils.extractDate("01").isoformat()
    print utils.extractDate("01/12").isoformat()
    print utils.extractDate("01/12/31").isoformat()

    print utils.extractDate("99/12/31").isoformat()
    print utils.extractDate("00/12/31").isoformat()

    print utils.extractDate("1999/12/31").isoformat()
    print utils.extractDate("2000/12/31").isoformat()

    print utils.extractDate("19/12/31").isoformat()
    print utils.extractDate("20/12/31").isoformat()
    print utils.extractDate("21/12/31").isoformat()

