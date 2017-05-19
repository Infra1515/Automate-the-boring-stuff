

# # Back up an entire site by following all of its links.
# The program will have to do download each separate .html page and save it
# It will have to follow the links, <a href> and download each link
# So whats the plan?
# 1. Download the main page with the request module
# 2. Download and save the new opened webpage on the hard drive with iter_content()
# 3. Find the next link url <href> , open it and download it
# 4. Repeat for every link
# 5. Let's try !


#! python3
import os, sys, requests, bs4

print ('This program is a BackUp/Link verificator.')
print('It will attempt to download all html pages as backup')
print('And show an error if a hyperlink is dead')
print('Enter the desired site:')
url = input()

os.makedirs(url, exist_ok = True)
os.chdir(os.getcwd()+ '/' + url)
# while not url.endswith('#'):

res = requests.get(url)
res.raise_for_status
soup = bs4.BeautifulSoup(res.text, 'lxml')
href_tags = soup.find_all(href=True)
only_href = []
# curpath = os.path.abspath(os.curdir)

# for index, tag in enumerate(href_tags):
#     only_href.append(href_tags[index].get('href'))

for i in range(1,len(href_tags)):
    only_href.append(href_tags[i].get('href'))


i = 0
for tag in only_href:
    if 'https://' in tag:
        tag = tag
    elif 'http://' not in tag:
        tag = url + tag
    print ('downloading %s...' % (tag))
    try:
        res = requests.get(tag)
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        print ('File %s UNREACHABLE - HTTPError 503' % (str(tag)))
        continue
    # playfile = str(tag)

    # print ('Current path is %s' % (curpath))
    # with open(os.path.join('ATBS', playfile, 'wb')) as outfile:
    with open('new_file_%s' % (i), 'wb') as outfile:
        for chunk in res.iter_content(100000):
            outfile.write(chunk)

    i += 1
# # The program works. The problem is with line 151 - I cant get to format
# # the name so it accepts the 'tag' name as string - gives files does not exist
# # the problem is with absolute and relative path which I do no understand
# # otherwise good job !


# # ALso for Link Verification
#
# Write a program that, given the URL of a web page, will attempt to download every
# linked page on the page. The program should flag any
# pages that have a 404 “Not Found” status code and print them out as broken links.
