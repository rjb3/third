# -----------------------------------------------------------------------------
def printPrettyDict( dict, width = 100, file = "" ) :
    import sys
    import pprint
    if len(file) > 0 :
        pprint.pprint(dict,open(file,"w"),1,width)
    else :
        pprint.pprint(dict,sys.stdout,1,width)

# -----------------------------------------------------------------------------
def printDict( dict, width = 100, file = "" ) :
    import sys
    for key, value in dict.items():
        print makeDateString(key),value

# -----------------------------------------------------------------------------
def makeEpochTime( string, pattern = '%Y-%m-%d %H:%M:%S' ) :
    import time
    seconds_since_epoch = int(time.mktime(time.strptime(string,pattern)))
    return seconds_since_epoch 

# -----------------------------------------------------------------------------
def makeDateString( secs, pattern = '%Y/%m/%d' ) :
    from datetime import date
    return date.fromtimestamp(secs).strftime(pattern)

# -----------------------------------------------------------------------------
def openUrl( url, local = False ) :
    if ( local ) :
        url = url.replace(':','-').replace('/',':')
        url = '/Users/bainbrid/Sites/' + url + ".html"
        return url,open(url)
    else :
        if True :
            import urllib
            return url,urllib.urlopen(url)
        else :
            print "TEST TEST"
            import urllib
            import urllib2
            headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:14.0) Gecko/20100101 Firefox/14.0.1'}
            request = urllib2.Request(url,None,headers)
            try:
                response = urllib2.urlopen(request)
                print response.read()
                return url,response
            except urllib2.HTTPError, error:
                print "ERROR: ", error.read()
                return url,error

# -----------------------------------------------------------------------------
def extractData( data, tuple ) :
    from datetime import datetime
    try :                              # Check if straight-forward float
        tuple = tuple + (float(data),) 
    except ValueError :
        if data.count(' Bil') :            # Billions
            tuple = tuple + (float(data.replace(' Bil',''))*1.e9,)
        elif data.count(' Mil') :          # Millions
            tuple = tuple + (float(data.replace(' Mil',''))*1.e6,)
        elif data.count(',') :             # Thousands
            try :                              
                tuple = tuple + (float(data.replace(',','')),) 
            except ValueError :       
                if data.count('%') :       # Percent change
                    data = data.replace('%','')
                    if data.count('+') :   # Positive change
                        tuple = tuple + (float(data.replace('+','')),)
                    elif data.count('-') : # Negative change
                        tuple = tuple + (-1.*float(data.replace('-','')),)
                    else :
                        try :                  # Check if straight-forward float
                            tuple = tuple + (float(data),) 
                        except ValueError :    # Else just assume string
                            tuple = tuple + (str(data),)
        else :                                 # Otherwise just assume string
            tuple = tuple + (str(data),)

    return tuple

# -----------------------------------------------------------------------------
#def extractDate( str ) :
#    '''Construct datatime object from string containing date of form YY/MM/DD'''
#    from datetime import datetime
#    str = str.strip()
#    if len(str) == 0 : return None
#    else :
#        yy = "Y" if bool( int(str.split('/')[0]) > 99 ) else "y"
#        if str.count('/') == 0 :
#            return datetime.strptime(str,"%"+yy)
#        elif str.count('/') == 1 :
#            return datetime.strptime(str,"%"+yy+"/%m")
#        elif str.count('/') == 2 :
#            return datetime.strptime(str,"%"+yy+"/%m/%d")

# -----------------------------------------------------------------------------
#def extractData( data, tuple ) :
#    from datetime import datetime
#    if data.count('/') > 0 : 
#        tuple = tuple + (makeEpochTime(data,'%y/%m'),)
#    else :
#        if data.count(' Mil') > 0 :
#            tuple = tuple + (float(data.replace(' Mil',''))*1.e6,)
#        elif data.count(' Bil') > 0 :
#            tuple = tuple + (float(data.replace(' Bil',''))*1.e9,)
#        else :
#            try :
#                tuple = tuple + (float(data),)
#            except ValueError :
#                tuple = tuple + (str(data),)
#    return tuple
