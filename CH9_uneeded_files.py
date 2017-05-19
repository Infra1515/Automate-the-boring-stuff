# Deleting unneeded files


# calling only os.path.getsize(filename) loops over files in the main folder
# to make it loop over the subfolders I have to use os.path.getsize(foldername + '/' filename)

# another problem was the absolute and relative path. I had forgoten to change the cwd()
import os
os.chdir and os.path.abspath

# TO DO : Make it loop over hidden files aswell
def DeleteUneededFiles (folder):
    folder = os.path.abspath(folder)
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            fileSize = os.path.getsize(foldername + '/' + filename)
            if int(fileSize) < 10000000:
                continue
            #os.unlink(filename) #Commented out to protect against accidental deletion
            print('Deleting ' + filename + '...') #Print only to verify working correctly

            print (filename, fileSize)

DeleteUneededFiles('/home/infra/Pythontest')
