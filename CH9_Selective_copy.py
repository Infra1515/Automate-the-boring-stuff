# #  Selective copy - ATBS CH 9
# # Program to copy only certain kind of files
import os, shutil

print ('Enter a source directory : ')
dirpath = '/home/infra/GitHub/Automate-the-boring-stuff'
print ('Enter a destination directory: ')
destination = '/home/infra/GitHub/selectiveCopy_test1'

for element in os.listdir(dirpath):
    if element.endswith('.txt'):
        shutil.copy(element,destination )
        print (element)


print ('Elements copied from %s to %s' % (dirpath, destination))

# for element in os.listdir('/home/infra/GitHub/Automate-the-boring-stuff'):
#     if element.startswith('09'):
#         element = element + '.txt'
#     print (element)


print (os.listdir(destination))
