0# Project: Renaming Files with American-Style Dates to European-Style Dates

# Say your boss emails you thousands of files with American-style dates (MM-DD-YYYY)
#  in their names and needs them renamed to European-style dates (DD-MM-YYYY).
#  This boring task could take all day to do by hand! Let’s write a program to do it instead.
#
# Here’s what the program does:
#
#     It searches all the filenames in the current working directory for American-style dates.
#
#     When one is found, it renames the file with the month and day swapped to make it European-style.
#
# This means the code will need to do the following:
#
#     Create a regex that can identify the text pattern of American-style dates.
#
#     Call os.listdir() to find all the files in the working directory.
#
#     Loop over each filename, using the regex to check whether it has a date.
#
#     If it has a date, rename the file with shutil.move().
#

# 1. Create the files
import os,shutil, re

print ('Specify the working directory : ')
osdir = input()
os.chdir(osdir)
# print ('Specify how many files you would like to create: ')
# number_of_files = int(input())
#
# for i in range(number_of_files):
#     create_file = open('09-%s-1992.txt' % (i+1), 'w')

list_of_files =  os.listdir(osdir)

datePattern = re.compile(r"""^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3?)\d)-
    ((19|20)\d\d)
    (.*?)$
    """, re.VERBOSE)

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart  = mo.group(2)
    dayPart    = mo.group(4)
    yearPart   = mo.group(6)
    afterPart  = mo.group(8)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart + '.txt'

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))
    #shutil.move(amerFilename, euroFilename) # uncomment after testing
