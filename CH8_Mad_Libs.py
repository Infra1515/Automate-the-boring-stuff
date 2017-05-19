import os
# Define where the file is located + open and read it
print ('Enter the file path: ')
dir_path = input()
madLib = open(dir_path)
madLibs = madLib.read()
# how many . or , are in the file
comma_and_dot = madLibs.count('.') + madLibs.count(',')
# Loop to remove the dot so it can be a standalone element in the list
# In order to avoid writing more boolean conditions
# You have to define a new variable ti store replace() because strings are immutable
# and at the end of the loop the string is not changed
for i in range(comma_and_dot):
    if '.' in madLibs:
        x = madLibs.replace('.', ' .')
    elif ',' in madLibs:
        x  =  madLibs.replace(',', ' ,')
# define a tuple with words that have to be replaced
AVN = ('ADJECTIVE', 'NOUN', 'VERB')
# define an empty list to add the new words
newMadLib = []
# The most important part: a for loop with index and word in enumerate()
# This loop goes through the list of words and appends each one of it to the
# new list. If a word is detected to be in the AVN tuple the user is prompted to
# replace it. The important part here is the use of newMadLib[index]. The word
# gets replaced by its index.
# I tried to do something simmilar with a double nested for loop but it gave me
# string index out of range.

for index, word in enumerate(x.split()):
    newMadLib.append(word)
    if word in AVN:
        print ('Enter ' + word +':')
        newMadLib[index] = input()
almost_final =' '.join(newMadLib)

# add back the dots to right place
for i in range(comma_and_dot):
    if ' .' in almost_final:
        x = almost_final.replace(' .', '.')
    elif ' ,' in madLibs:
        x  =  almost_final.replace(' ,', ',')
print (x)


# So the lesson to take: If you want to replace words inside a string or a list
# without using a long if elif else chain condition
# then you have to define the words to be replaced in a tuple
# a new list to store the results
# and call a for loop with enumerate(list) in order loop through the index and words
# and then add the new word with input() BASED ON THE INDEX


## to do  : define the two for loops(dots) inside two functions

## P.S there is no need for a loop. After you separate the dots you can just call string.replace(x,y)
# with if clause
