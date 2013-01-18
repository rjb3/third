import time
import mechanize

br = mechanize.Browser()
#br.set_handle_robots(False)   # no robots
#br.set_handle_refresh(False)  # can sometimes hang without this
#br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

url = "http://uk.moneycentral.msn.com/investor/quotes/stockatoz.aspx"
response = br.open(url)
print response.geturl()

#print response.read()      # the text of the page
#response1 = br.response()  # get the response again
#print response1.read()     # can apply lxml.html.fromstring()

for form in br.forms():
#    print "Form name:", form.name
#    print form

#br.select_form("form1")         # works when form has a name
#br.form = list(br.forms())[0]  # use when form is unnamed

#    form.set_all_readonly(False)    # allow everything to be written to

    for control in form.controls:
#        print control
#        print "type=%s, name=%s value=%s" % (control.type, control.name, br[control.name])

        if control.type == "select":  # means it's class ClientForm.SelectControl
#            control.disabled = False
#            for item in control.items:
#                print " name=%s values=%s" % (item.name, str([label.text  for label in item.get_labels()]))

            #print control.value
#            print control  # selected value is starred
            if control.name == "ddCountry" : control.value = ["US"]
            print control
            #if control.name == "ddCountry" : br[control.name] = ["UK"] 
            #print control

        if control.type == "submit":
#            control.disabled = False
#            print control.value
            print control

request2 = form.click()
try:
    response2 = mechanize.urlopen(request2)
except mechanize.HTTPError, response2:
    pass

print response2.geturl()
#for name, value in response2.info().items():
#    if name != "date":
#        print "%s: %s" % (name.title(), value)
#print response2.read() # body
#response2.close()

cj = mechanize.CookieJar()
br2 = mechanize.Browser()
br2.set_cookiejar(cj)
br2.open(request2)

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
html = response4.read()
br3.select_form(nr=1)
print br3.form
#br3.set_all_readonly(False)
#mnext = re.search("""<a id="lnkNext" href="javascript:__doPostBack\('(.*?)','(.*?)'\)">Next >>""", html)
#if not mnext:
#    break
#br3["__EVENTTARGET"] = mnext.group(1)
#br3["__EVENTARGUMENT"] = mnext.group(2)
#response5 = br3.submit()

#for link in br3.links():
#    if link.text == "B" : 
#        print link.text, link.url
#        request4 = br3.click_link(link)
        #print request4
        #response5 = br3.follow_link(link)
        #print response5.geturl()
        #cj3 = mechanize.CookieJar()
        #br4 = mechanize.Browser()
        #br4.set_cookiejar(cj3)
        #response5 = br4.open(request4)
#        break

#br3.select_form("MainForm")
#print br3.form







#from bs4 import BeautifulSoup
#html = response4.read()
#soup = BeautifulSoup(html,"lxml")
#cols = soup.findAll("td")
#print cols[0]

