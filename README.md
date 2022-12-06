# Files for Finnish hyphenation and spelling in Affinity Publisher

This repository conntains 3 files needed in Affinity Publisher to hyphenate and spell check Finnish language. Files have been forked from https://www.apt-browse.org/browse/debian/wheezy/main/all/myspell-fi/0.7-18/file/usr/share/hunspell. At the moment original hunspell dictionary contains some repeating and unsorted word blocks. Removed in this repository.

## Files to start with Finnish spelling and hyphenation

The`fi_FI.aff` file contains basic information how Finnish words are consturcted. In the begining there is an instruction to set a correct character set. Original files use **UTF8** encoding. According to tests I have been able to conduct UTF8 works well with Finnish Windows 10. Further tests will be made with different operating systems and language versions in the future. There may be other sources of these files with **ISO8859-1** encoding. In those files the character setting on 1st row must be `SET ISO8859-1` to make spelling and hyphenation function properly. Wrong character encoding settings may add duplicate suggestions or dislpaly strange characters. The following screen shot shows  correct suggestions when set UTF8:

![image](https://user-images.githubusercontent.com/24242044/205984577-ac7ab74b-f8fe-4bb8-8969-bd34ba0f276a.png)

if setting is ISO8859-1 incorrect suggestions are shown:

![image](https://user-images.githubusercontent.com/24242044/205985457-24b283d5-182d-477e-9edb-06203626bf6b.png)

and some suggestions are duplicated

![image](https://user-images.githubusercontent.com/24242044/205986888-da047e28-2280-4256-a0e1-70709af388b5.png)

but when the character setting is correct no odd behavior is seen:

![image](https://user-images.githubusercontent.com/24242044/205987987-97b25ae8-9c62-4960-a032-e59973fcd8a2.png)

The `fi_FI.dic` file is a bag of Finnish words. There is a word counter at the beginig of the file. Affinity Publisher does not update this file. If you teach new words to Publisher they are stored elswhere not in this file.

The `hyph_fi_FI.dic` file contains instructions how to split words for hyphens. There is also a character set definition at the 1st row. 

## Installing files 
You can download dictionary files by clicking the green Code button on top right hand corner. Unzip contents to Affinitys Dictionaries folder. You can find this location in the app from `Edit - Preferences - Tools`

![image](https://user-images.githubusercontent.com/24242044/205483402-095cd467-d668-45f7-826c-2dee38fca26b.png)

Open the folder by clicking `Open` then copy unzipped files to this folder.

## Tools for updating and cleaning spelling dictionary
The structure of `fi_FI.dic` is very simple: on the 1st row there is a word counter and the rest of rows contain words in alphabetical order. The purpose of this repostitory is provide simple tools for adding, sorting and removing duplicates from the spelling dictionary. With appropriate tools dictionary can be maintained and expanded to meet our requirements. Tools will be added as they are ready to be published. Some rough ideas written in Python can be found in the development branch. Hope we have standalone tools with a GUI in the future. As tools are ready for use instructions can be found on this repositorys Wiki pages.
