# Needs to read in mech.out
# Then we'll parse
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/
# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python

from bs4 import BeautifulSoup

f = open('mech.out', 'r+')

contents = f.read()

# print (contents)

# have BS open the file mech.out and store it in soup.

soup = BeautifulSoup(open("mech.out"))

# now store the string inside the qoutes into the variable soup

# soup = BeautifulSoup("<html>data</html>")

# Now print soup

print (soup)

# Moving to bottom so we have it, but don't need it right now
# http://axialcorps.com/2013/09/27/dont-slurp-how-to-read-files-in-python/
