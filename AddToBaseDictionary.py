# Some ideas for updating the Finnish spelling dictionary

def addSingleWordToDictionary(fileName, wordToAdd):
    """Adds a single new word to the Finnish spelling dictionary
    which may not be in alphabetical order. Reads trough entire dictionary.
    Sorts the dictionary if word has been added and updates word count. 

    Args:
        fileName (str): Name of the Finnish dictionary file
        wordToAdd (str): a word to be added to the dictionary file

    Returns:
        str: has the word been added or has it already been in the dictionary
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
        wordList.append(wordToAdd + '\n')
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
    """Scans for a given word in the Finnish dictionary file. 
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
        if dictionaryWord == wordToFind + '\n':
            resultText = f'{wordToFind} was already in the Finnish dictionary at row {curentRow}'
            resultFound = True
            resultRow = curentRow
            continueSacan = False

        # Check if the dictionary row has greater alphabetical index than the word
        elif dictionaryWord > wordToFind + '\n':
            resultText = f'{wordToFind} was not found in the Finnish dictionary, scanned {curentRow} rows, last word was {dictionaryWord}'
            resultFound = True
            resultRow = curentRow
            continueSacan = False

        # Check if the end of dictionary is reached (word may be the last word to add to the dictionary)
        elif curentRow == rowCount + 2:  # First row is the rowcount and there is an additional empty row at the end of dictionary
            resultText = f'{wordToFind} was not found in the Finnish dictionary, scanned entire dictionary, last word was {dictionaryWord}'
            resultFound = False
            resultRow = curentRow
            continueSacan = False
    result = (resultFound, resultRow, resultText)
    return result


if __name__ == "__main__":

    # Some preliminary tests
    result = addSingleWordToDictionary('fi_FI.dic', 'maastopyörä')
    print(result)

    result = scanFromOrderedDictionary('fi_FI.dic', 'maastopyörä')
    print(result)
