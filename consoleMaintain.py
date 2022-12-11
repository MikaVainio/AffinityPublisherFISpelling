# TOOLS FOR MAINTAINING TEH FINNISH HUNSPELL DICTIONAY FROM CONSOLE
# =================================================================

# LIBRARIES AND MODULES


# CLASS DEFINITIONS
# -----------------

class MaintainDictionary:
    """Methods for maintaining the Finnish spelling dictionary
        Args:
            fileName (str): Name of the Finnish dictionary file
            encoding (str): Character encoding used, defaults to UTF8
    
    """
    def __init__(self, fileName, encoding='UTF8'):
        self.fileName = fileName
        self.encoding = encoding

    def sortDictionary(self):
        """Reads the dictionary from file and return original rowcount,
        actual row count and sorted list of words

        Returns:
            tuple: Original word count, real word count, list of words 
        """
        with open(self.fileName, 'r', encoding=self.encoding) as file:
            originalWordCount = file.readline()
            unsortedDictionary = file.readlines()
            sortedDictionary = sorted(unsortedDictionary)
            realWordCount = str(len(sortedDictionary)) +'\n'
            result = (originalWordCount, realWordCount, sortedDictionary)
        return result

    def addSingleWordToUnorderedDictionaryFile(self, wordToAdd):
        """Adds a single new word to the Finnish spelling dictionary
        which may not be in alphabetical order. Reads trough entire dictionary
        before adding the word. Does not add the word if it already exists.
        Sorts the dictionary if word has been added and updates word count. 

        Args:
            wordToAdd (str): A word to be added to the dictionary file

        Returns:
            str: Has the word been added or has it already been in the dictionary
        """
        # Open the dictionary file for reading
        file = open(self.fileName, 'r', encoding=self.encoding)
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
            file = open(self.fileName, 'w', encoding=self.encoding)
            file.writelines(updatedDictionary)
            file.close()
            result = f'{wordToAdd} has been added to the Finnish dictionary'
        return result

    def scanFromOrderedDictionaryFile(self, wordToFind):
        """Scans for a given word in the spelling dictionary file. 
        Assumes that file is in alphabetical order.

        Args:
            wordToFind (str): Word to find in the dictionary

        Returns:
            tuple: Found (bool), row in the dictionary (int), informational text about the scan (str)
        """
        # Open the dictionary file for reading
        file = open(self.fileName, 'r', encoding=self.encoding)
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
                resultFound = False
                resultRow = curentRow
                continueSacan = False

            # Check if the end of dictionary is reached (word may be the last word to add to the dictionary)
            elif curentRow == rowCount + 2:  # First row is the rowcount and there is an additional empty row at the end of dictionary
                resultText = f'{wordToFind} was not found in the Finnish dictionary, scanned from index until the word was {dictionaryWord}'
                resultFound = False
                resultRow = curentRow
                continueSacan = False

        # Close the file and build the tuple containig results
        file.close
        result = (resultFound, resultRow, resultText)
        return result

    def addWordToDictinaryFileWOCheck(self, wordToAdd, finalize=False):
        """Adds a single word to the spelling dictionary. When finalized dictionary will be sorted
        and word count updated to actual number words in the dictionary. Does not check if alredy exists
        in the dictionary

        Args:
            wordToAdd (_type_): A word to add to the dictionary
            finalize (bool, optional): Should the dictionary be sorted and word count updated. Defaults to False.

        Returns:
            str: Information about the operation
        """
        
        with open(self.fileName, 'a', encoding=self.encoding) as file:
            file.write(wordToAdd + '\n')
            result = f'{wordToAdd} has been appended to the dictionary'
            
        if finalize == True:
            with open(self.fileName, 'r+', encoding=self.encoding) as file:
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

    def dictionaryWODuplicates(self):
        """Removes duplicates from the spelling dictionary.

        Returns:
            tuple: Original Word count (int), Word count after removing duplicates (int)
            and list of words without duplicates. There is a new line character after every word.
        """

        with open(self.fileName, 'r', encoding=self.encoding) as file:
            originalRowCount = int(file.readline())  # Read the 1st line containing row count
            originalList = file.readlines()
            # Change to a Python dictionary which does not allow duplicate keys
            dictionaryFromList = dict.fromkeys(originalList)
            # Make it an ordinary list again
            distinctList = list(dictionaryFromList)
            rowCount = len(distinctList)
            result = (originalRowCount, rowCount, distinctList)
        return result 

    def writeBackToDictionaryFile(self, wordList):
        wordCount = str(len(wordList)) +'\n'
        with open(self.fileName, 'w', encoding=self.encoding) as file:
            file.write(wordCount)
            file.writelines(wordList)

    def addSeveralWordsToDictionaryFile(self, wordList):
        """Adds a list of words to dictionary file, removes duplicates,
        sorts the dictionary and updates the word counter

        Args:
            wordList (list): List of words to add to the dictionary file

        Returns:
            str: Information about the operation
        """
        amntWords = len(wordList)
        with open(self.fileName, 'a', encoding=self.encoding) as file:
            for word in wordList:
                lineToAdd = word + '\n'
                file.write(lineToAdd)

        results = self.dictionaryWODuplicates()
        numberOfDuplicates = results[1] - results[0]
        distinctWords = results[2]
        sortedDistinctWords = sorted(distinctWords)
        self.writeBackToDictionaryFile(sortedDistinctWords)
        result = f'Added {amntWords - numberOfDuplicates} words to the dictionary. {numberOfDuplicates} were duplicates'
        return result

if __name__ == "__main__":
    maintainDictionary = MaintainDictionary('fi_FI.dic')
    # result = maintainDictionary.addWordToDictinaryWOCheck('koodari', True)
    # print(result)
    '''result = maintainDictionary.sortDictionary()
    print(result[0])
    result = maintainDictionary.dictionaryWODuplicates()
    originalRowCount = result[0]
    currentRowCount = result[1]
    distinctWords = result[2]

    print('alunperin', originalRowCount, 'poiston jälkeen', currentRowCount)
    maintainDictionary.writeBackToDictionaryFile(distinctWords)
    '''
    wordList = ['kasettipesä', 'aurauskulma', 'kotiavustaja']
    result = maintainDictionary.addSeveralWordsToDictionaryFile(wordList)
    print(result)
    