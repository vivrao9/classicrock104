import requests, bs4, time, datetime, csv, json, os
from twilio.rest import TwilioRestClient

XHRrequest = 'https://api.live365.com/v1/station/b47785?cb=180712'

headers = {
    "User-Agent": "my [personal] web scraping program. contact me at xxx@gmail.com"
}

while os.path.getsize('Classic Rock 104.csv') <= 1000000000:

    res = requests.get(XHRrequest, headers=headers)
    dictionary = json.loads(res.text)
    nowPlaying = dictionary.get("current-track", "none")
    dictionary = dict(nowPlaying)

    trackName = dictionary.get('title')
    artist = dictionary.get('artist')
    artwork = dictionary.get('art')
    timestamp = dictionary.get('start')
    buy_link = dictionary.get('itune_buy_link')

    adName = dictionary.get('full_track')

    outputFile = open('Classic Rock 104.csv', 'a', newline='\n')
    outputWriter = csv.writer(outputFile)
    try:
        outputWriter.writerow([timestamp, trackName, artist, artwork, buy_link])
    except:
        outputWriter.writerow([timestamp, adName, artist])
        
    outputFile.close()
    time.sleep(120)

accountSID = 'xxx'
authToken = 'xxx'
twilioCli = TwilioRestClient(accountSID, authToken)
myTwilioNumber = '+xxx'
myCellPhone = '+xxx'
message = twilioCli.messages.create(body='Congrats! You now have 1 Gb of Classic Rock radio station data.', from_=myTwilioNumber, to=myCellPhone)
                                    

#spoke to owner Jamie Daveson (Davidson?) over the phone. He said it was okay to
#scrape website every 90-120 seconds. He also added that, if I wanted, I could
#reach out to the DJ Matthew Gunter through the website's Contact form to
#request a list of commonly played songs
