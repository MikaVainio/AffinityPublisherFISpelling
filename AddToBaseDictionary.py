# Some ideas for updating the Finnish spelling dictionary

def addSingleWordToDictionary(fileName, wordToAdd):
    """Adds a single new word to the Finnish spelling dictionary 

    Args:
        fileName (str): Name of the Finnish dictionary file
        wordToAdd (str): a word to be added to the dictionary file

    Returns:
        str: has the word been added or has it already been in the dictionary
    """
    # Open the dictionary file for reading 
    file = open(fileName, 'r', encoding='UTF8' )
    rowCount = int(file.readline()) # Read the 1st line containing row count
    wordList = file.readlines() # Build a list from the rest of lines

    # Check if the word is already in the list
    if wordToAdd + '\n' in wordList:
        file.close
        result = f'{wordToAdd} was already in the Finnish dictionary'

    else:
        wordList.append(wordToAdd + '\n') # Add the word and a new line to the list
        sortedWordList = sorted(wordList) # Sort the list
        rowCount = len(sortedWordList) # Create a new row count

        # Build a new dictionary file
        updatedDictionary = []
        updatedWordCount = []
        updatedWordCount.append(str(rowCount) + '\n')
        updatedDictionary = updatedWordCount + sortedWordList
        file.close
        file = open(fileName, 'w', encoding='UTF8' )
        file.writelines(updatedDictionary)
        file.close()
        result = f'{wordToAdd} has been added to the Finnish dictionary'
    return result

if __name__ == "__main__":

    # Some preliminary tests
    result = addSingleWordToDictionary('fi_FI.dic', 'maakellari')
    print(result)