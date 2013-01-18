import mechanize
import re

br = mechanize.Browser()
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
response = br.open("http://data.fingal.ie/ViewDataSets/")

for i in range(10):
    print "PAGE NUMBER:",i,"#####################"
    html = response.read()
#    print html
#print "Page %d :" % i, html
    br.select_form(nr=0)
    #print br.form
    br.set_all_readonly(False)
    mnext = re.search("""<a id="lnkNext" href="javascript:__doPostBack\(\&\#39;(.*?)\&\#39;,\&\#39;(.*?)\&\#39;\)">Next >>""", html)
#    print mnext
    if mnext == None: break
    br["__EVENTTARGET"] = mnext.group(1)
    br["__EVENTARGUMENT"] = mnext.group(2)
    br.find_control("btnSearch").disabled = True
    for link in br.links():
        print link.text#, link.url
    response = br.submit()

#<a href="javascript:__doPostBack('StockData','Page$2')">








