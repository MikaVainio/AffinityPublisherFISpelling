import xml.etree.ElementTree as ET

class MaintenanceOperation():
    """For updating the spelling dictionary."""
    def __init__(self, dictionaryFile, encoding):
        
        self.dictionaryFile = dictionaryFile
        self.encoding = encoding

    def addSeveralWordsToDictionaryFile(self, wordList):
        """Adds a list of words to dictionary file, removes duplicates,
        sorts the dictionary and updates the word counter

        Args:
            wordList (list): List of words to add to the dictionary file

        Returns:
            str: Information about the operation
        """
        amntWords = len(wordList)
        with open(self.dictionaryFile, 'a', encoding=self.encoding) as file:
            for word in wordList:
                lineToAdd = word + '\n'
                file.write(lineToAdd)

        results = self.dictionaryWODuplicates()
        numberOfDuplicates = results[1] - results[0]
        distinctWords = results[2]
        sortedDistinctWords = sorted(distinctWords)
        self.writeBackToDictionaryFile(sortedDistinctWords)
        
        result = f'Tryint to add {amntWords} words to the dictionary. {numberOfDuplicates} were finally added'
        return result

    def writeBackToDictionaryFile(self, wordList):
        wordCount = str(len(wordList)) +'\n'
        with open(self.dictionaryFile, 'w', encoding=self.encoding) as file:
            file.write(wordCount)
            file.writelines(wordList)
    
    def dictionaryWODuplicates(self):
        """Removes duplicates from the spelling dictionary.

        Returns:
            tuple: Original Word count (int), Word count after removing duplicates (int)
            and list of words without duplicates. There is a new line character after every word.
        """

        with open(self.dictionaryFile, 'r', encoding=self.encoding) as file:
            originalRowCount = int(file.readline())  # Read the 1st line containing row count
            originalList = file.readlines()
            # Change to a Python dictionary which does not allow duplicate keys
            dictionaryFromList = dict.fromkeys(originalList)
            # Make it an ordinary list again
            distinctList = list(dictionaryFromList)
            rowCount = len(distinctList)
            result = (originalRowCount, rowCount, distinctList)
        return result 

    def readFromJoukahainen(self, xmlFile):
        """Reads words from Joukahainen xml based word dictionary

        Args:
            xmlFile (str): name of the xml file containing Joukahainen dictonary

        Returns:
            list: list of corrected words from Joukahainen
        """
        xmlTree = ET.parse(xmlFile)
        root = xmlTree.getroot()
        words = []
        for node in root.findall('./word/forms/form'):
            correctedWord = node.text.replace('=', '') # Remove egual signs from words
            words.append(correctedWord)

        # TODO: Poista print-komennot kun testattu
        print(words)
        print(len(words))
        return words

    


