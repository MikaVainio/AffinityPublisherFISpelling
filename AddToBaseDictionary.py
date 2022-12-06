# Some ideas for updating the Finnish spelling dictionary

def addSingleWordToDictionary(fileName, wordToAdd):
    """Adds a single new word to the Finnish spelling dictionary
    which may not be in alphabetical order. Reads trough entire dictionary.
    Sorts the dictionary if word has been added and updates word count. 

    Args:
        fileName (str): Name of the Finnish dictionary file
        wordToAdd (str): A word to be added to the dictionary file

    Returns:
        str: Has the word been added or has it already been in the dictionary
    """
    # Open the dictionary file for reading
    file = open(fileName, 'r', encoding='UTF8')
    rowCount = int(file.readline())  # Read the 1st line containing row count
    wordList = file.readlines()  # Build a list from the rest of lines

    # Check if the word is already in the list
    if wordToAdd + '\n' in wordList:
        file.close
        result = f'{wordToAdd} was already in the Finnish dictionary'

    else:
        # Add the word and a new line to the list
        wordList.append(wordToAdd + '\n')  # The word and a new line character
        sortedWordList = sorted(wordList)  # Sort the list
        rowCount = len(sortedWordList)  # Create a new row count

        # Build a new dictionary file
        updatedDictionary = []
        updatedWordCount = []
        updatedWordCount.append(str(rowCount) + '\n')
        updatedDictionary = updatedWordCount + sortedWordList
        file.close
        file = open(fileName, 'w', encoding='UTF8')
        file.writelines(updatedDictionary)
        file.close()
        result = f'{wordToAdd} has been added to the Finnish dictionary'
    return result


def scanFromOrderedDictionary(fileName, wordToFind):
    """Scans for a given word in the spelling dictionary file. 
       Assumes that file is in alphabetical order.

    Args:
        fileName (str): Name of the dictionary file
        wordToFind (str): Word to find in the dictionary

    Returns:
        tuple: Found (bool), row in the dictionary (int), informational text about the scan (str)
    """
    # Open the dictionary file for reading
    file = open(fileName, 'r', encoding='UTF8')
    rowCount = int(file.readline())  # Read the 1st line containing row count
    continueSacan = True
    curentRow = 2

    # Scan the dictionary until word is found or a word with greater alphabetical index is foud
    while continueSacan:
        dictionaryWord = file.readline()  # Read a single row
        curentRow += 1  # Increase the row counter

        # Check if the word is in the dictionary
        if dictionaryWord == wordToFind + '\n':  # In the dictionary there is a new line on every row
            resultText = f'{wordToFind} was already in the Finnish dictionary at row {curentRow}'
            resultFound = True
            resultRow = curentRow
            continueSacan = False

        # Check if the dictionary row has greater alphabetical index than the word
        elif dictionaryWord > wordToFind + '\n':
            resultText = f'{wordToFind} was not found in the Finnish dictionary, scanned {curentRow} rows, last word before exit was {dictionaryWord}'
            resultFound = True
            resultRow = curentRow
            continueSacan = False

        # Check if the end of dictionary is reached (word may be the last word to add to the dictionary)
        elif curentRow == rowCount + 2:  # First row is the rowcount and there is an additional empty row at the end of dictionary
            resultText = f'{wordToFind} was not found in the Finnish dictionary, scanned entire dictionary, last word was {dictionaryWord}'
            resultFound = False
            resultRow = curentRow
            continueSacan = False

    # Close the file and build the tuple containig results
    file.close
    result = (resultFound, resultRow, resultText)
    return result


def addToDictionaryWOChecking(fileName, wordToAdd, finalize=True):
    """Adds a word to the Finnish dictionary without checking if the word alredy exist in the dictionary

    Args:
        fileName (str): Name of the dictionary file
        wordToAdd (str): A word to add to the dictionary
        finalize (bool, optional): Should the dictionry be ordered and row count updated after insert. Defaults to True.

    Returns:
        _type_: _description_
    """

    # Append the word to the end of dictionary file
    # Open the dictionry for append and read mode
    file = open(fileName, 'a+', encoding='UTF8')
    file.write(wordToAdd + '\n')
    result = f'{wordToAdd} has been appended to the dictionary'

    if finalize:
        file.seek(0)  # Move to the start of the file
        currentRowCount = file.readline()
        actualRowCount = []
        listToWriteBack = []
        unorderedList = file.readlines()  # Read the rest of lines in the dictionary
        print(unorderedList)
        orderedList = sorted(unorderedList)  # Sort the list
        # Calculate actual number of words
        actualRowCount.append(str(len(orderedList)) + '\n')
        file.close()
        # Updated contents of the dictionary
        listToWriteBack = actualRowCount + orderedList
        print(listToWriteBack)
        file = open(fileName, 'w')
        file.writelines(listToWriteBack)
        file.close()
        result = result + ' and dictionary has been sorted and word count updated'
    else:
        file.close()
    return result


def addWordToDictinaryWOCheck(fileName, wordToAdd, finalize=False):
    """Adds a single word to the spelling dictionary. When finalized dictionary will be sorted
       and word count updated to actual number words in the dictionary. Does not check if alredy exists
       in the dictionary

    Args:
        fileName (str): Name of the dictionary file
        wordToAdd (_type_): A word to add to the dictionary
        finalize (bool, optional): Should the dictionary be sorted and word count updated. Defaults to False.

    Returns:
        str: Information about the operation
    """
    
    with open(fileName, 'a', encoding='UTF8') as file:
        file.write(wordToAdd + '\n')
        result = f'{wordToAdd} has been appended to the dictionary'
        
    if finalize == True:
        with open(fileName, 'r+', encoding='UTF8') as file:
            actualRowCount = []
            orderedList = []
            currentRowCount = file.readline() # Read the word count
            unorderedList = file.readlines()  # Read the rest of lines in the dictionary
            orderedList = sorted(unorderedList)  # Sort the list
            # Calculate actual number of words
            actualRows = str(len(orderedList))
            actualRowCount.append(actualRows + '\n')
            listToWriteBack = actualRowCount + orderedList
            file.seek(0)
            file.writelines(listToWriteBack)

        result += f'which has been sorted and word count updated to {actualRows}, was {currentRowCount} '
    return result

# TODO: Complete this function
def fullDictionaryScan(fileName, wordToFind):
    """Scans the entire dictionary assuming it has not been sorted

    Args:
        fileName (str): Name of the dictionary file
        wordToFind (str): A word to search in the dictionary

    Returns:
        bool: True if found
    """
    found = False
    return found

# TODO: Complete this function
def checkDictionary(fileName):
    """Checks the integrity of the spelling dictionary
    ie. it is in alphabethical order an the word count is correct

    Args:
        fileName (_type_): _description_

    Returns:
        _type_: _description_
    """
  
    wordCountCorrect = False
    sortedCorrectly = False
    result = (wordCountCorrect, sortedCorrectly)
    return result

def removeDuplicates(fileName):
    """Removes duplicates from the spelling dictionary

    Args:
        fileName (str): Name of the dictionary file

    Returns:
        list: Word list without duplicates new line character after every word
    """

    with open(fileName, 'r', encoding='UTF8') as file:
        rowCount = int(file.readline())  # Read the 1st line containing row count
        originalList = file.readlines()
        # Change to a Python dictionary which does not alloe duplicate keys
        dictionaryFromList = dict.fromkeys(originalList)
        # Make it an ordinary list again
        distinctList = list(dictionaryFromList)
    return distinctList 

# TODO: Complete this
def writeBackToDictionary(fileName, wordList):

    wordCount = len(wordList)
    pass

if __name__ == "__main__":

    # SOME PRELIMINARY TESTS

    # Try to add a word alredy into the dictionary, already in the dictionary
    result = addSingleWordToDictionary('fi_FI.dic', 'maastopyörä')
    print(result)

    # Scan for the word in the dictionary
    result = scanFromOrderedDictionary('fi_FI.dic', 'maastopyörä')
    print(result)

    # Scan for the plural of the previous word (missing in the dictionary)
    result = scanFromOrderedDictionary('fi_FI.dic', 'maastopyörät')
    print(result)

    #result = addToDictionaryWOChecking('fi_FI_testDictionary.dic', 'sakkeli', True)
    #print(result)

    result = addWordToDictinaryWOCheck('fi_FI_testDictionary.dic', 'kuukkeli', True)
    print(result)

    listWODuplicates = removeDuplicates('fi_FI_testDictionary.dic')
    print(listWODuplicates)