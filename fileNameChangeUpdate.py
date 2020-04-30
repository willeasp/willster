import os

def removeFromFileName(dirName, subString):
    dirList = os.listdir(dirName)

    for entry in dirList:
        fullPath = os.path.join(dirName, entry)

        if os.path.isdir(fullPath):
            removeFromFileName(fullPath, subString)
        else:
            if subString in entry:
                str(entry).replace(str(subString), "")

cwd = os.getcwd()
stringToBeRemoved = input("vilken sträng vill du ta bort? Tänk på att ta med mellanslag.")
removeFromFileName(cwd, stringToBeRemoved)
