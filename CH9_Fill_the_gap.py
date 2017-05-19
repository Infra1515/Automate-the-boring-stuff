# Fill the gap CH9

# How to find missing integers in a number line ( list) :
# lis = [1,3,6,9,13]
# lis.sort(reverse=True)
# i = 0
# print (lis)
#
# while i < len(lis) - 1 :
#     # if lis[i] - lis[i+1] > 1 and lis[i] - lis[i+1] < 2 :
#     #     print (lis[i], lis[i+1])
#     #     missingElem = lis[i] - 1
#     #     print (missingElem)
#     if lis[i] - lis[i+1] > 1:
#         print (lis[i], lis[i+1])
#         for missingNum in range(lis[i+1]+1, lis[i]):
#             print (missingNum)
#         # print (missingElem)
#
#     i += 1


## But my goal is to sort filenames which have both text and numbers inside a string
# so calling sort() on os.listdir(os.getcwd()) gives me a sorted ASCII list, not
# a sorted alphabetical list. I need to do "human sorting"
# http://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside
# in order to do that I Have to split the string to text and numbers

# functions to sort a list of strings in natural(human)(alphabetical) order
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    return [ atoi(c) for c in re.split('(\d+)', text) ]




import os, re, shutil
# define a regEx in order to separate letters from numbers
r = re.compile("([a-zA-Z]+)([0-9]+)")
# define the folder where the files are located
lis = os.listdir('/home/infra/GitHub/Automate-the-boring-stuff/crap')
os.chdir('/home/infra/GitHub/Automate-the-boring-stuff/crap')
lis.sort(key=natural_keys)
# define an empty list to store the numbers
s = []
# iterate through lis and search for suitable files
for elem in lis:
    # skip files that do not meet the regEx req
    mo = r.search(elem)
    if mo == None:
        continue
    # add the number to the empty list s[]
    s.append((r.match(elem).group(2)))
    # define the first part as namePart
    namePart = mo.group(1)
# convert the list from strings to integers in order to sort them
s_int = [int(x) for x in s]
s_int.sort(reverse=True)
# find the missing number in the number line
i = 0
missingNums = []
while i < len(s_int) - 1 :
    if s_int[i] - s_int[i+1] > 1:
        for missingNum in range(s_int[i+1]+1, s_int[i]):
            missingNums.append(missingNum)
    i += 1
# append the missing numbers to the end of the list and sort them
for num in missingNums:
    s_int.append(num)

s_int.sort()


# remove the biggest(last) elements from the list so it matches the original size
# which is the size in the number of files in range of missingNums
# or instead of removing print the elements the sorted elements from first to last
# in range of i+1 - its at the range of the numbers of elements appended up
finalList = []
for num in range(i+1):
    finalList.append(s_int[num])
# convert from int to string with list comprhho
finalList_strings = [str(x) for x in finalList]

# Finally create the new filename
# for c in range(len(lis)):
# for c in range(len(lis)):
#     print (namePart + '' + finalList_strings[c])
#     newName = namePart + finalList_strings[c]

for index, elem in enumerate(lis):
    newName = namePart + finalList_strings[index]
    print ('Renaming %s to %s..'% (elem, newName))
    shutil.move(elem, newName)
