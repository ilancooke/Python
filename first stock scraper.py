 
import urllib
import re

symbolslist = ["AAPL", "SPY", "GOOG", "NFLX"]

for symbol in symbolslist:
    url = "http://finance.yahoo.com/q?s=%s&ql=1"%(symbol)     
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_l84_%s">(.+?)</span>'%(symbol.lower())
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print "The price of ",symbol," is ",price