import webbrowser, sys, pyperclip


#! Python 3
# mapIt.py - Launches google maps in the browser using adress from the
# command line or the clipboard

if len(sys.argv) > 1:
    adress = ' '.join(sys.argv[1:])
else:
    adress = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + adress)
