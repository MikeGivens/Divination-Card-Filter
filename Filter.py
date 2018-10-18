import os
import requests
import json
import sys

from DivCardFunctions import *

r = requests.get('https://poe.ninja/api/Data/GetDivinationCardsOverview?league=Delve')
if r.status_code != 200:
    print("Incorrect URL or poe.ninja is unavailable at this time.\n")
else:
    print("API request successful!\n")
    j = json.loads(r.text)
    SortedArray = SortDivCards(j) # Sorts the Divination Cards into a single array.
    WriteDivCards(SortedArray) # Writes the Divination Card loot filter code into a file.
    print("Filter Complete & Saved to FilterData.txt in current directory!")
    # Result is in FilterData.txt file in current directory.