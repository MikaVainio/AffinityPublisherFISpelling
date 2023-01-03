# CODE FOR DICTIONARY MAINTENANCE APPLICATION'S DIALOGS
# =====================================================

# LIBRARIES AND MODULES
import os
import json
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from qt_material import QtStyleTools, apply_stylesheet # For theme adjustments

# CLASS DEFINITIONS

class SettingsHandler(QDialog):
    """Reads and writes application settings file."""
    def __init__(self):
        super().__init__()
    
        loadUi('settingsDialog.ui', self)
        self.setWindowTitle('Asetukset')
        self.settings = settingsFromJsonFile('settings.json')
        apply_stylesheet(self, theme=self.settings['theme'])
        self.currentDictionary = self.settings['dictionary']
        self.browsePB = self.browsePushButton
        self.browsePB.clicked.connect(self.fileDialog)
        self.savePB = self.savePushButton
        self.savePB.clicked.connect(self.saveSettings)
        self.fileLE = self.fileLineEdit
        self.fileLE.setText(os.path.normpath(self.currentDictionary))

    def fileDialog(self):     
        self.fileLE.setText(self.currentDictionary)
        fileName, check = QFileDialog.getOpenFileName(None, 'Valitse sanakirja', self.currentDictionary, 'Sanakirjat (*.dic *.aff)')
        if fileName:
            self.fileLE.setText(os.path.normpath(fileName))

    def saveSettings(self):
        self.settings['dictionary'] = self.fileLE.text()
        saveSettingsToJsonFile('settings.json', self.settings)
        self.close()

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
    
    settingsFile = open(file, 'w') # Opens settings file for writing
    json.dump(settingData, settingsFile) # Write dictionary in JSON format to file
    settingsFile.close() # Close the file after