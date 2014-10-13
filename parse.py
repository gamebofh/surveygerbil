# Needs to read in mech.out
# Then we'll parse

# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
from bs4 import BeautifulSoup

f = open('mech.out', 'r+')

contents = f.read()

print (contents)

soup = BeautifulSoup(open("index.html"))

soup = BeautifulSoup("<html>data</html>")



# Moving to bottom so we have it, but don't need it right now
# http://axialcorps.com/2013/09/27/dont-slurp-how-to-read-files-in-python/
