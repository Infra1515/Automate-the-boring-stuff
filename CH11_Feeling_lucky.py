# 'Im feeling lucky' Google search
# This is what your program does:
#     Gets search keywords from the command line arguments.
#
#     Retrieves the search results page.
#
#     Opens a browser tab for each result.
# 
# This means your code will need to do the following:
#
#     Read the command line arguments from sys.argv.
#
#     Fetch the search result page with the requests module.
#
#     Find the links to each search result.
#
#     Call the webbrowser.open() function to open the web browser.

# Open a new file editor window and save it as lucky.py.
#! Python 3
# lucky.py
import sys,webbrowser,requests, bs4

adress = ''.join(sys.argv[1:])
res = requests.get('http://google.com/search?q=' + adress)
res.raise_for_status()
nSS = bs4.BeautifulSoup(res.text, 'lxml')
linkElems = nSS.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

#############
