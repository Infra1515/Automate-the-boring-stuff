#! Python 3
# Program that gets the weather forecast in a simple manner
import sys, requests, json, pprint
if len(sys.argv) < 2:
    print('This is a simple weather forecast downloader')
    print('Please enter your desired location')
    sys.exit()

location = ' '.join(sys.argv[1:])
url ='http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&units=metric&APPID=ea574594b9d36ab688642d5fbeab847e' % (location)
# 78a55ae1dced71f858c8035deeb305c9 - my API key
# there is a difference between the original program and the current version
# api key is needed and url is changed
response = requests.get(url)
response.raise_for_status()
weather_data = json.loads(response.text)
w = weather_data['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print('Tempreture Morning/Day/Evening: ' +  str(w[0]['temp']['morn']) + 'c /' , str(w[0]['temp']['day']) + 'c /' + str(w[0]['temp']['eve']) + 'c ')
print('MAX/MIN Tempreture:' + str(w[0]['temp']['max']) + 'c / ' + str(w[0]['temp']['min']) + 'c ')
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print('Tempreture Morning/Day/Evening: ' +  str(w[1]['temp']['morn']) + 'c /' , str(w[1]['temp']['day']) + 'c /' + str(w[1]['temp']['eve']) + 'c ')
print('MAX/MIN Tempreture:' + str(w[1]['temp']['max']) + 'c / ' + str(w[1]['temp']['min']) + 'c ')
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-',w[2]['weather'][0]['description'])
print('Tempreture Morning/Day/Evening: ' +  str(w[2]['temp']['morn']) + 'c /' , str(w[2]['temp']['day']) + 'c /' + str(w[2]['temp']['eve']) + 'c ')
print('MAX/MIN Tempreture:' + str(w[2]['temp']['max']) + 'c / ' + str(w[2]['temp']['min']) + 'c ')


# to-do - use a for loop to analyze all of the data ( 6 days)
# add a feature to connect to several weather apis, show each result and calculate the median
