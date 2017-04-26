## Write a program that opens all .txt files in a folder and searches for any
#line that matches a user-supplied regular expression. The results should be printed to the screen.

# Open all files in a folder
import os
import re

print ('Please select a directory(i.e /home/user/xx)')
dir_path = input()
os.chdir(dir_path)
list_of_files = os.listdir(dir_path)
print ('What is your search term?')
search_term = input()


for index, element in enumerate(list_of_files):
    open_file = open(element, 'r')
    filetext = open_file.read()
    matches = re.findall(search_term, filetext)
    print ('Number:' + str(index) + '  Name of file:'+ element + '  Matches:' + str(matches))
    open_file.close()
