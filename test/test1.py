import time
import mechanize

symbols = {}

br = mechanize.Browser()
br.set_handle_robots(False)   # no robots
br.set_handle_refresh(False)  # can sometimes hang without this
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = "http://uk.moneycentral.msn.com/investor/quotes/stockatoz.aspx"
response = br.open(url)
print response.geturl()

#print response.read()

for form in br.forms():
    for control in form.controls:
        if control.type == "select":  # means it's class ClientForm.SelectControl
            if control.name == "ddCountry" : control.value = ["US"]
            print control
        if control.type == "submit":
            print control

request2 = form.click()
try:
    response2 = mechanize.urlopen(request2)
except mechanize.HTTPError, response2:
    pass

cj = mechanize.CookieJar()
br2 = mechanize.Browser()
br2.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br2.set_cookiejar(cj)
response3 = br2.open(request2)

for form2 in br2.forms():
    for control2 in form2.controls:
        if control2.type == "select":
            if control2.name == "ddMarket" : control2.value = ["58"]
            print control2
            for item2 in control2.items:
                print " name=%s values=%s" % (item2.name, str([label2.text  for label2 in item2.get_labels()]))


request3 = form2.click()
try:
    response3 = mechanize.urlopen(request3)
except mechanize.HTTPError, response3:
    pass

cj2 = mechanize.CookieJar()
br3 = mechanize.Browser()
br3.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br3.set_cookiejar(cj2)
response4 = br3.open(request3)

import re
for i in range(2):
    print "PAGE NUMBER:",i,"#####################"
 
    for link5 in br3.links(url_regex='symbol='):
        symbol = link5.url.split('symbol=')[1]
        if len(symbol) : symbols[ symbol ] = link5.text

    #html5 = br3.response()
    html5 = response4.read()
    if i == 1 : print html5
    try:
        br3.select_form("MainForm")
    except:
        "PRINT"
        break
    #print br3.form
    br3.set_all_readonly(False)
#    mnext = re.search("""<a id="lnkNext" href="javascript:__doPostBack\(\&\#39;(.*?)\&\#39;,\&\#39;(.*?)\&\#39;\)">Next >>""", html5)
#    mnext = re.search("""<td><a href="javascript:__doPostBack\(\&\#39;(.*?)\&\#39;,\&\#39;(.*?)\&\#39;\)">""", html5)
    mnext = re.search("""<a href="javascript:__doPostBack\('(.*?)','(.*?)'\)">""", html5)

#<a href="javascript:__doPostBack('StockData','Page$2')">2

    print mnext,mnext.group(1),mnext.group(2)
    if mnext == None: break
    br3.form.new_control('hidden', '__EVENTTARGET', {'value':mnext.group(1)})
    br3.form.new_control('hidden', '__EVENTARGUMENT', {'value':mnext.group(2)})
    #br3["__EVENTTARGET"] = mnext.group(1)
    #br3["__EVENTARGUMENT"] = mnext.group(2)
    br3.form.fixup()
    #br3.find_control("btnSearch").disabled = True
#    for link in br.links():
#        print link.text#, link.url
    response4 = br3.submit()



#for link in br3.links(url_regex='symbol='):
##    if link.text == "B" : 
#    symbol = link.url.split('symbol=')[1]
#    if len(symbol) : symbols[ symbol ] = link.text
#        #request4 = br3.click_link(link)
        #print request4
        #response5 = br3.follow_link(link)
        #print response5.geturl()
        #cj3 = mechanize.CookieJar()
        #br4 = mechanize.Browser()
        #br4.set_cookiejar(cj3)
        #response5 = br4.open(request4)
        #break

import pprint
pprint.pprint(symbols)

#br3.select_form("MainForm")
#print br3.form







#from bs4 import BeautifulSoup
#html = response4.read()
#soup = BeautifulSoup(html,"lxml")
#cols = soup.findAll("td")
#print cols[0]

