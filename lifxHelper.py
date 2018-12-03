# lifxHelper.py
#
# A few utilities for converting responses from LIFX api.

import json

class LIFXResponse:
    # a datastructure to hold the 'results' portion of the response
    def __init__(self, id, status, label):
        self.id = id
        self.status = status
        self.label = label

def convertToLIFXResponse(response, asObject=True):
    '''
    takes as an argument the 'response' that 'requests.put()' returns, and it
    returns the inner 'results' list item(s) converted to an object if 'asObject' is 'True'
    (the default behavior) or a dictionary if 'asObject' is 'False'.

    if there are multiple items in the 'results' list, then this returns a
    list of converted objects/dictionaries, if there is only one item, then it returns
    that single converted item (not a list).
    '''

    results_list = response.json()["results"]

    converted_items_list = []

    for item in results_list:
        if (asObject):
            r = LIFXResponse(item['id'], item['status'], item['label'])
            converted_items_list.append(r)
        else:
            converted_items_list.append(item)

    # check how many total 'results' items there were.
    if (len(converted_items_list) == 1):
        return converted_items_list[0]
    else:
        return converted_items_list

    '''
    In case you are curious how it works:

    calling 'response.json()' will convert the response to a series of dictionaries
    and arrays. The outer dictionary has a single key, 'results', whose value is a list
    that contains a single item (in this case), which is another dictionary, with
    keys 'id', 'status' and 'label'.  So the ["results"] and the [0] index just
    traverse the structure (outlined below) so that all you get is the internal 'results'
    dictionary, converted to an object (or left as a dictionary if you prefer that).

    the response.json() object structure....
    {
       'results': [
          {
             'id': 'd073d5299516',
             'status': 'offline',
             'label': 'Kitchen',
          }
       ]
    }

    '''
