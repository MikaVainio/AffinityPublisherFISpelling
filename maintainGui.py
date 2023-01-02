
import sys # For accessing system parameters
import os # For file path handling
from PyQt5 import QtCore, QtWidgets # For the Qt functionality
from PyQt5.uic import loadUi
from qt_material import QtStyleTools, apply_stylesheet # For theme adjustments

# Class for the main window
class MainWindow(QtWidgets.QMainWindow, QtStyleTools):
    """Creates a main window"""

    # Constructor
    def __init__(self):
        super().__init__()

        # Create the main window using the latest custom theme
        self.main = loadUi('MainWindow.ui', self)
        apply_stylesheet(self.main, theme='my_theme.xml')
        self.setWindowTitle('Sanakirjan ylläpito')
        iconPixmap = QtWidgets.QStyle.SP_DialogApplyButton
        icon = self.style().standardIcon(iconPixmap)
        self.setWindowIcon(icon)

        # MENU ACTIONS

        # Set the dark theme
        self.actionDark.triggered.connect(self.setDarkTheme)

        # Set the light theme
        self.actionLight.triggered.connect(self.setLightTheme)

        # Set the default theme
        self.actionDefaultTheme.triggered.connect(self.setDefaultTheme)

        # Set custon theme
        self.actionAdjustTheme.triggered.connect(self.setCustomTheme)

        # PUSH BUTTONS

        # Lisää kaikki push button, adds all words to the dictionary file
        self.saveAllPB = self.addAllPushButton
        self.saveAllPB.setEnabled(False) 
        self.saveAllPB.clicked.connect(self.saveAll)

        # Lisää valitut push button, adds selected words to the dictionary file
        self.saveSelectedPB = self.addChosenPushButton
        self.saveSelectedPB.setEnabled(False)
        self.saveSelectedPB.clicked.connect(self.saveSelected)

        # INPUTS & OUTPUTS
        self.wordInput = self.wordToAddLineEdit
        self.wordInput.returnPressed.connect(self.addToList)

        self.wordsList = self.wordsListWidget
        self.wordsList.itemDoubleClicked.connect(self.wordsListEdit)
        self.wordsList.itemSelectionChanged.connect(self.enableSaveSelectedPB)

    def setDarkTheme(self):
        apply_stylesheet(self.main, theme='dark_amber.xml')

    def setLightTheme(self):
        apply_stylesheet(self.main, theme='light_cyan_500.xml')

    def setDefaultTheme(self):
        apply_stylesheet(self.main, theme='default_theme.xml')

    def setCustomTheme(self):
        self.show_dock_theme(self.main)

    def addToList(self):
        item = self.wordInput.text().strip()
        if item != '':
            self.wordsList.addItem(item)
            self.wordInput.clear()
            self.enableSaveAll()

    def wordsListEdit(self, item):
        row = self.wordsList.row(item)
        toBeEdited = self.wordsList.takeItem(row)
        self.wordInput.setText(toBeEdited.text())
        self.enableSaveAll()

    def saveSelected(self):
        selectedItems = self.wordsList.selectedItems()
        for item in selectedItems:
            row = self.wordsList.row(item)
            print(item.text())
            self.wordsList.takeItem(row)
        self.saveSelectedPB.setEnabled(False)       

    def saveAll(self):
        count = self.wordsList.count()
        for row in range(count):
            print(self.wordsList.item(row).text())
        self.wordsList.clear()
        self.saveAllPB.setEnabled(False)

    def enableSaveAll(self):
        count = self.wordsList.count()
        if count > 0:
            print(count)
            self.saveAllPB.setEnabled(True)
        else:
            self.saveAllPB.setEnabled(False)

    def enableSaveSelectedPB(self):
        selections = len(self.wordsList.selectedItems())
        if selections > 0:
            self.saveSelectedPB.setEnabled(True)
        else:
            self.saveSelectedPB.setEnabled(False)

if __name__ == "__main__":

    # Create the application
    app = QtWidgets.QApplication(sys.argv)
    
    # Create the Main Window object from MainWithWebView Class and show it on the screen
    appWindow = MainWindow()
    appWindow.main.show()  # This can also be included in the main window's class
    sys.exit(app.exec())
