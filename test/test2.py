import time
import mechanize

br = mechanize.Browser()
#br.set_handle_robots(False)
#br.set_handle_refresh(False)
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = "A.htm"

response = br.open(url)
print response.geturl()

#for form in br.forms():
#    for control in form.controls:
#        if control.type == "select": 
#            #control.readonly = False
#            control.disabled = False
#            if control.name == "ddCountry" : control.value = ["US"]
#            if control.name == "ddMarket" : control.value = ["58"]
#
#br.select_form("MainForm")
#br.set_all_readonly(False)
#mnext = re.search("""<a href="javascript:__doPostBack\('(.*?)','(.*?)'\)">""", html5)
#if mnext != None :
#    br["__EVENTTARGET"] = mnext.group(1)
#    br["__EVENTARGUMENT"] = mnext.group(2)
#    br.find_control("btnSearch").disabled = True
#    response2 = br.submit()
#
#
#
##symbols = {}
##import re
##for link in br.links(url_regex='symbol='):
##    symbol = link5.url.split('symbol=')[1]
##    if len(symbol) : symbols[ symbol ] = link5.text
##import pprint
##pprint.pprint(symbols)
