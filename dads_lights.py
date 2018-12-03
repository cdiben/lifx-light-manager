# dads_lights.py 
#
# a script for querying the 'status' of the response
#
# author - Dylan DiBenedetto 11.30.18

import requests
from lifxHelper import convertToLIFXResponse

def main():
    token = "cc0b9aaa33fca0742dc6524071bf4c9ebb274ca8b8a447861d4a1e9a3a2a0afe"

    headers = {
        "Authorization": "Bearer {}".format(token),
    }

    payload = {
        "power": "on",
    }
    response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    # converted response as a dictionary
    r_dict = convertToLIFXResponse(response, asObject=False)

    # converted response as an LIFXResponse object (see lifxHelper.py)
    r_obj = convertToLIFXResponse(response)

    # now you can query the values in the dictionary 'r_dict', or the properties
    # of the LIFXResponse obejct, 'r_obj'.
    print("'{0}' status: '{1}'".format(r_dict['label'], r_obj.status))

main()
