#! python3
#multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok = True) # store comics in ./xkcd

def download_xkcd(startComic, endComic):
    for url_number in range(startComic, endComic):
        # Download the page
        print('Downloading page http://xkcd.com/%s...' % (url_number))
        res = requests.get('http://xkcd.com/%s'% (url_number))
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'lxml')
        # find the URL of the comic image.
        comicElem = soup.select('#comic img')

        if comicElem == []:
            print('Could not find comic image')
        else:
            comicUrl = 'https:' + comicElem[0].get('src')
            # download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # save image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

# Create and start the Thread objects.

download_threads = [] # a list of all the Thread objects
for i in range(0,1700,100): # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    download_threads.append(downloadThread)
    downloadThread.start()
    print (download_threads)


for downloadThread in download_threads:
    downloadThread.join()
print('Done.')

print (download_threads)
