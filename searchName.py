import json

# load the periodic elements into a list
periodicElementsList = json.load(open('PeriodicElements.json', 'r')) 
# this variable is for the periodic symbols
periodicSymbolsList = [i['Symbol'] for i in periodicElementsList]


# the function for finding the periodic eleements in name
def searchName(sentence: str)-> list:
    # splits the sentence into multiple words
    words = sentence.split(' ')
    # this is the list that will be returned containing the names and periodic symbols
    elementalNameList = []

    # iterating over the words 
    for names in words:

        # this is the dictionary that is going to be added to elementalnamelist for every word
        elementalNameDict = {
            'found': False,
        }
        
        # searching through every letter
        for letters in range(0,len(names)):
            
            # checks if it the letter and its sequential is a periodic symbol
            if names[letters:letters+2].capitalize() in periodicSymbolsList:

                elementalNameDict['found'] = True
                elementalNameDict['beforeElement'] = names[:letters]
                elementalNameDict['Element'] = periodicElementsList[periodicSymbolsList.index(names[letters:letters+2].capitalize())]
                elementalNameDict['afterElement'] = names[letters+2:]
                break

            # checks if the letter is a periodic symbol
            elif names[letters].upper() in periodicSymbolsList:

                elementalNameDict['found'] = True
                elementalNameDict['beforeElement'] = names[:letters]
                elementalNameDict['Element'] = periodicElementsList[periodicSymbolsList.index(names[letters].upper())]
                elementalNameDict['afterElement'] = names[letters+1:]
                break
                
        # after searching through every letter, if it can not be found, the name is just added to the list
        if not elementalNameDict['found']:
            elementalNameDict['name'] = names

        elementalNameList.append(elementalNameDict)
            
    return elementalNameList

