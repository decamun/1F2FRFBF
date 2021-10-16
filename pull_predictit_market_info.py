import time
import os
import json
import xmltodict
import requests


#loop
error = False #flag an error
last_dump = time.time()
last_read = time.time()

predict_it_url = 'https://www.predictit.org/api/marketdata/all/'

all_mkt_info = {}

def parse_response(response):
    if response.status_code != 200:
        #bad response
        print('Bad response. Status code: ' + str(response.status_code) +  '\nContent:\n' + str(response))
    print(response)
    return json.loads(response.content)

while error == False:
    time_this_loop = time.time()

    if time_this_loop > last_read + 30.0: #it's time to read market info
        print('Pulling Market Info...')

        #read mkt info
        response = requests.get(predict_it_url) #request the data frm the API
        all_mkt_info[time_this_loop] = parse_response(response) #convert the API response to a dict
        last_read = time_this_loop

    if time_this_loop > last_dump + 60.0*10:
        print('Saving all data...')

        #save mkt info
        filename = './data/predictit/' + str(int(last_dump)) + '.json'

        json_mkt_info= json.dumps(all_mkt_info, indent = 4)

        with open(filename, "w") as outfile:
            outfile.write(json_mkt_info)

        all_mkt_info = {}
        last_dump = time_this_loop
