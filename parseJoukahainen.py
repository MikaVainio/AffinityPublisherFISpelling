# FIXME: Älä sisällytä lopulliseen ohjelmaan!

# A MODULE FOR PARSING JOUKAHAINEN XML WORD DICTIONARY
# ====================================================

# LIBRARIES AND MODULES 
import xml.etree.ElementTree as ET


xmlTree = ET.parse('testxml.xml')
root = xmlTree.getroot()
rootName = root.tag
print(rootName)
words = []
for node in root.findall('./word/forms/form'):
    words.append(node.text)
print(words)
print(len(words))   
