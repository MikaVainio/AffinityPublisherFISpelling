# CODE FOR DICTIONARY MAINTENANCE APPLICATION'S DIALOGS
# =====================================================

# LIBRARIES AND MODULES
import os
import json
import dictionaryMaintain
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from qt_material import apply_stylesheet  # For theme adjustments

# CLASS DEFINITIONS


class SettingsHandler(QDialog):
    """Reads and writes application settings file."""

    def __init__(self):
        super().__init__()

        loadUi('settingsDialog.ui', self)
        self.setWindowTitle('Sanakirja-asetukset')

        # Read the settings file
        self.settings = settingsFromJsonFile('settings.json')
        scale = self.settings['scale']
        self.extra = {'density_scale': f'{scale}'}
        apply_stylesheet(self, theme=self.settings['theme'], extra=self.extra)
        self.currentDictionary = self.settings['dictionary']
        self.characterEncoding = self.settings['encoding']
        self.densityScale = self.settings['scale']

        # UI elements
        self.browsePB = self.browsePushButton
        self.browsePB.clicked.connect(self.fileDialog)
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveSettings)
        self.fileLE = self.fileLineEdit
        self.fileLE.setText(os.path.normpath(self.currentDictionary))
        self.encodingCB = self.characterEncodingComboBox
        self.encodingCB.setCurrentText(self.characterEncoding)

    # A Method for changing the spelling dictionary
    def fileDialog(self):
        self.fileLE.setText(self.currentDictionary)
        fileName, check = QFileDialog.getOpenFileName(
            None, 'Valitse sanakirja', self.currentDictionary, 'Sanakirjat (*.dic *.aff)')
        if fileName:
            self.fileLE.setText(os.path.normpath(fileName))

    # Method for save dictionary settings
    def saveSettings(self):
        self.settings['dictionary'] = self.fileLE.text()
        self.settings['encoding'] = self.encodingCB.currentText()
        saveSettingsToJsonFile('settings.json', self.settings)
        self.close()


class SetSize(QDialog):
    """Increases or decreases the size of UI elements."""

    def __init__(self):
        super().__init__()

        loadUi('sizeDialog.ui', self)
        self.setWindowTitle('Muuta elementtien kokoa')

        # Load settings from json file
        self.settings = settingsFromJsonFile('settings.json')
        scale = self.settings['scale']
        self.extra = {'density_scale': f'{scale}'}
        apply_stylesheet(self, theme=self.settings['theme'], extra=self.extra)
        self.newSize = 0

        # UI elements
        self.sizeSB = self.sizeSpinBox
        self.sizeSB.setRange(-5, 9)
        self.sizeSB.setValue(int(scale))
        self.sizeSB.valueChanged.connect(self.changeSize)
        self.savePB = self.saveSizePushButton
        self.savePB.clicked.connect(self.saveSizeSetting)

    def changeSize(self):
        self.newSize = str(self.sizeSB.value())
        self.newExtra = {'density_scale': f'{self.newSize}'}
        apply_stylesheet(
            self, theme=self.settings['theme'], extra=self.newExtra)

    def saveSizeSetting(self):
        self.settings['scale'] = self.newSize
        saveSettingsToJsonFile('settings.json', self.settings)
        self.close()


class SanitizeDictionary(QDialog):
    """Sorts dictionary, removes duplicates and updates the word counter."""

    def __init__(self):
        super().__init__()

        loadUi('sanitizeDictionary.ui', self)
        self.setWindowTitle('Sanakirjan tarkistus ja korjaus')
        self.settings = settingsFromJsonFile('settings.json')
        scale = self.settings['scale']
        self.extra = {'density_scale': f'{scale}'}
        apply_stylesheet(self, theme=self.settings['theme'], extra=self.extra)
        self.currentDictionary = self.settings['dictionary']
        self.characterEncoding = self.settings['encoding']
        self.sanitizedWordList = []
        self.sanitizedWordCount = 0

        self.inFileLcd = self.inFileLcdNumber
        self.actualLcd = self.actualLcdNumber
        self.finalLcd = self.finalLcdNumber

        self.okPB = self.okPushButton
        self.okPB.clicked.connect(self.saveSanitized)

        self.anlyzeData = self.sanitize(
            self.currentDictionary, self.characterEncoding)
        self.inFileLcd.display(int(self.anlyzeData[0]))
        self.actualLcd.display(int(self.anlyzeData[1]))
        self.finalLcd.display(int(self.anlyzeData[2]))

    def sanitize(self, dictionary, encoding):
        """Reads the spelling dictionary, remove duplicates, sort and recount words

        Args:
            dictionary (str): file name of the dictionary
            encoding (str): character encoding of the dictonary

        Returns:
            tuple: original, actual and final row counts
        """
        with open(dictionary, 'r', encoding=encoding) as file:
            originalWordCount = file.readline()
            unsortedDictionary = file.readlines()
            sortedDictionary = sorted(unsortedDictionary)
            realWordCount = str(len(sortedDictionary)) + '\n'
            # Change to a Python dictionary which does not allow duplicate keys
            dictionaryFromList = dict.fromkeys(sortedDictionary)
            # Make it an ordinary list again
            distinctList = list(dictionaryFromList)
            finalRowCount = len(distinctList)
            result = (originalWordCount, realWordCount, finalRowCount)
            self.sanitizedWordCount = finalRowCount
            self.sanitizedWordList = distinctList
        return result

    def saveSanitized(self):
        with open(self.currentDictionary, 'w', encoding=self.characterEncoding) as file:
            file.write(str(self.sanitizedWordCount) + '\n')
            file.writelines(self.sanitizedWordList)
        self.close()


class JoukahainenDialog(QDialog):
    """Dialog for getting words from Joukahainen dictionary."""

    def __init__(self):
        super().__init__()

        loadUi('joukahainenDialog.ui', self)
        self.setWindowTitle('Sanojen nouto Joukahaisesta')
        self.settings = settingsFromJsonFile('settings.json')
        scale = self.settings['scale']
        self.extra = {'density_scale': f'{scale}'}
        apply_stylesheet(self, theme=self.settings['theme'], extra=self.extra)
        self.currentDictionary = self.settings['dictionary']
        self.characterEncoding = self.settings['encoding']

        self.xmlLE = self.xmlFileLineEdit
        self.browsePB = self.browsePushButton
        self.browsePB.clicked.connect(self.fileDialog)
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.joukahainenToDictionary)

    def fileDialog(self):
        """A methtod to create Dialog window for choosing Joukahainen xml file
        """
        defaultDirectory = os.path.expanduser('~') + '\\Downloads'
        self.xmlFileName, check = QFileDialog.getOpenFileName(
            None, 'Valitse Joukahaisen sanasto', defaultDirectory, 'xml-tiestostot (*.xml)')
        if self.xmlFileName:
            self.xmlLE.setText(os.path.normpath(self.xmlFileName))

    def joukahainenToDictionary(self):
        """A Method to convert and save words of Joukahainen to the spelling dictionary
        """
        maintenanceOperation = dictionaryMaintain.MaintenanceOperation(
            self.currentDictionary, self.characterEncoding)
        self.joukahainenWords = maintenanceOperation.readFromJoukahainen(
            self.xmlFileName)
        result = maintenanceOperation.addSeveralWordsToDictionaryFile(
            self.joukahainenWords)
        print(result)


# A function for reading settings from a JSON file
def settingsFromJsonFile(file):
    """Reads settings from json file and converts
        json to pyhthon dictionary format
    Args:
        file (str): Name of JSON file containing setting parameters
    Returns:
        dict: Setting parameters
    """

    settingsFile = open(file, 'r')
    settingsData = json.load(settingsFile)
    settingsFile.close()
    return settingsData

# A method to save connection settings to a JSON file


def saveSettingsToJsonFile(file, settingData):
    """Writes settings to json file.
    Args:
        file (str): Name of the file to write
        settingData (dict): Dictionary of settings
    """

    settingsFile = open(file, 'w')  # Opens settings file for writing
    # Write dictionary in JSON format to file
    json.dump(settingData, settingsFile)
    settingsFile.close()  # Close the file after
