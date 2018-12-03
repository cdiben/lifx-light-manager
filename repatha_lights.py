# repatha_lights.py
#
# a script for querying the 'status' of the response
#
# author - Dylan DiBenedetto 11.30.18 & Christian DiBenedetto 12.1.18

import requests
from lifxHelper import convertToLIFXResponse
from datetime import date
import calendar
import time

def main():

    while True:
        
        # success is set to 1 if the status from the light is ok
        success = 0

        # test if the day is a multiple of 14 days from the starting day
        oldDate = date(2018,11,27)
        myDate = date.today()
        diffDate = myDate-oldDate
        theDay = diffDate.days % 14

        # loop when the day is correct and the light has not responded with ok
        while (theDay==0 and success == 0):
        
            token = "cc0b9aaa33fca0742dc6524071bf4c9ebb274ca8b8a447861d4a1e9a3a2a0afe"

            headers = {
                "Authorization": "Bearer {}".format(token),
            }

            payload = {
                "power": "on",
                "color": "red"
            }
            response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

            # converted response as a dictionary
            r_dict = convertToLIFXResponse(response, asObject=False)

            # converted response as an LIFXResponse object (see lifxHelper.py)
            r_obj = convertToLIFXResponse(response)

            # now you can query the values in the dictionary 'r_dict', or the properties
            # of the LIFXResponse obejct, 'r_obj'.
            if (r_obj.status == 'ok'):
                success = 1
            time.sleep(60)
            
        waitToNextMidnight()
    

def waitToNextMidnight():
    '''Wait to tomorrow 2:00 am.'''
    t = time.localtime()
    t = time.mktime(t[:3] + (0,0,0) + t[6:])
    time.sleep(7200 + t + 24*3600 - time.time())

main()
