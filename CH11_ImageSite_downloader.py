

# #
# Image Site Downloader
#
# Write a program that goes to a photo-sharing site like Flickr or Imgur,
# searches for a category of photos, and then downloads all the resulting images.
# You could write a program that
# works with any photo site that has a search feature.
#
# PLan : 1. User define search term
# 2. Use requests and soup to find all the objects
# 3. DOwnload them

import os, sys, requests, bs4

print('This is an Image Site downloader for IMGUR.')
print('It downloads all the pictures in the search term query')
print('Please enter your search term')
search_termin = input()

url = 'http://imgur.com/search/score/all?q=' + search_termin

os.makedirs('IMGUR', exist_ok = True)
os.chdir(os.getcwd()+ '/IMGUR')

res = requests.get(url)
res.raise_for_status
soup = bs4.BeautifulSoup(res.text, 'lxml')
img_elem = soup.find_all(src=True)

img_links = []
for elem in img_elem:
    img_links.append(elem.get('src'))

only_img = []
for i in range(len(img_links)):
    if '//i.imgur.com/' in img_links[i]:
        only_img.append(img_links[i])

# Right now I have a list of the img links, but i need to remove the [:-5] letter
# 'b' because with it I get only the thunbnail
# I have a list of strings. Strings are immutable. So I need to split() each element
# of the list, remove the [:-5] and then join the together.
# Or just remove 'b', easier
only_img_fullsize = []
i = 0
for element in only_img:
    s = list(element)
    s.remove('b')
    z =''.join(s)
    final_ = 'http:' + z
    only_img_fullsize.append(final_)

for link in only_img_fullsize:
    print('Downloading %s..' % (str(link)))

    res = requests.get(link)
    res.raise_for_status

    with open('new_file_%s' % (i), 'wb') as outfile:
        for chunk in res.iter_content(100000):
            outfile.write(chunk)

    i+= 1

# The program works. GOOD JOB ! Now I need to upgrade its functionality
# ATM it only downloads the first images that are loaded. I want to somehow
# scroll down or load them in a separate page and download the rest

# 2. To make it download all images from a gallery
