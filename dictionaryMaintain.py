# MODULE FOR SPELL CHECKING DICTIONARY MAINTENANCE OPERATIONS
# ===========================================================

# LIBRARIES AND MODULES
# ---------------------
import xml.etree.ElementTree as ET
import unicodedata as ud

# CLASS DEFINITIONS
# -----------------


class MaintenanceOperation():
    """For updating the spelling dictionary."""

    def __init__(self, dictionaryFile, encoding):

        self.dictionaryFile = dictionaryFile
        self.encoding = encoding

    # A method to add several words to the spelling dictionary
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
                if word.isalpha():  # Check for non alpha characters
                    lineToAdd = word + '\n'
                    file.write(lineToAdd)
        results = self.dictionaryWODuplicates()
        numberWODuplicates = results[1] - results[0]
        distinctWords = results[2]
        sortedDistinctWords = sorted(distinctWords)
        self.writeBackToDictionaryFile(sortedDistinctWords)
        result = f'Tryint to add {amntWords} words to the dictionary. {numberWODuplicates} were finally added'
        return result

    # A method to write updated data back to the dictionary file
    def writeBackToDictionaryFile(self, wordList):
        wordCount = str(len(wordList)) + '\n'
        with open(self.dictionaryFile, 'w', encoding=self.encoding) as file:
            file.write(wordCount)
            file.writelines(wordList)

    # A method for removing duplicates from the spelling dictionary
    def dictionaryWODuplicates(self):
        """Removes duplicates from the spelling dictionary.

        Returns:
            tuple: Original Word count (int), Word count after removing duplicates (int)
            and list of words without duplicates. There is a new line character after every word.
        """

        with open(self.dictionaryFile, 'r', encoding=self.encoding) as file:
            # Read the 1st line containing row count
            originalRowCount = int(file.readline())
            originalList = file.readlines()
            # Change to a Python dictionary which does not allow duplicate keys
            dictionaryFromList = dict.fromkeys(originalList)
            # Make it an ordinary list again
            distinctList = list(dictionaryFromList)
            rowCount = len(distinctList)
            result = (originalRowCount, rowCount, distinctList)
        return result

    # A method for reading Joukahainen spelling dictionary (xml file) to a list
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
            # Remove egual signs from words
            correctedWord = node.text.replace('=', '')

            # Change the UTF8 encoded words to correct character encoding
            utfNormalized = ud.normalize('NFKC', correctedWord).encode(
                self.encoding, 'ignore').decode(self.encoding)
            words.append(utfNormalized)
        return words


if __name__ == "__main__":
    maintenanceOperation = MaintenanceOperation('testi.dic', 'iso8859-1')
    result = maintenanceOperation.readFromJoukahainen(
        'C:\\Users\\MikaV\\Downloads\\joukahainen.xml')
    print(result)
    print(len(result))
