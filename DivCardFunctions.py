import os
import requests
import json
import sys

from DivCard import *

def SortDivCards(loadtext):
    print("Starting Sort...")
    divList = []
    divValueArrays = []
    names50 = []
    names10 = []
    names2  = []
    namesBad = []

    loadtext = loadtext["lines"]
    for line in loadtext:  
        divName = ""
        divValue = 0.0
        for key in line:
            value = line[key]
            if key == "name":
                divName = value
            if key == "chaosValue":
                divValue = value
        newCard = DivCard(divName, divValue)
        divList.append(newCard)
        pass
    pass

    for card in divList:
        if card.chaosValue >= 50:
            names50.append(card.name)
        elif card.chaosValue >= 10:
            names10.append(card.name)
        elif card.chaosValue >= 2:
            names2.append(card.name)
        elif card.chaosValue < 1:
            namesBad.append(card.name)
        else:
            pass

    divValueArrays.append(names50)
    divValueArrays.append(names10)
    divValueArrays.append(names2)
    divValueArrays.append(namesBad)
    print("Sort Complete!\n")
    return divValueArrays

def WriteDivCards(SortedArray):
    print("Starting Write...")
    current_directory = os.getcwd()
    f = open(os.path.join(current_directory, 'FilterData.txt'), 'w')
    f.write('# Section: Divination Cards\n\n')
    f.write('Hide\n\tClass "Divination Card"\n\tBaseType')
    for name in SortedArray[3]:
        f.write(' "' + name + '"')
    f.write('\n\n')

    f.write('Show # Divination Cards - 50c+\n')         
    f.write('\tClass "Divination Card"\n\tBaseType')
    for name in SortedArray[0]:
        f.write(' "' + name + '"')
    f.write('\n\tSetTextColor 0 0 0\n\tSetBackgroundColor 0 255 255 200\n\tSetBorderColor 0 0 0\n\tSetFontSize 45\n\tMinimapIcon 0 Blue Square\n\tPlayEffect Blue\n\n')

    f.write('Show # Divination Cards - 10c - 49c\n')
    f.write('\tClass "Divination Card"\n\tBaseType')
    for name in SortedArray[1]:
        f.write(' "' + name + '"')
    f.write('\n\tSetTextColor 0 0 0\n\tSetBackgroundColor 0 255 255 200\n\tSetBorderColor 0 0 0\n\tSetFontSize 43\n\tMinimapIcon 0 Blue Square\n\tPlayEffect Blue\n\n')

    f.write('Show # Divination Cards - 2c - 9c\n')
    f.write('\tClass "Divination Card"\n\tBaseType')
    for name in SortedArray[2]:
        f.write(' "' + name + '"')
    f.write('\n\tSetTextColor 0 0 0\n\tSetBackgroundColor 0 255 255 200\n\tSetBorderColor 0 0 0\n\tSetFontSize 42\n\n')

    f.write('Show # Divination Cards - Others\n')
    f.write('\tClass "Divination Card"\n\tSetTextColor 0 255 255\n\tSetBorderColor 0 255 255\n\tSetFontSize 40')
    print("Write Complete!\n")
    f.close()