def getEvenLines(inName, outName):
    with open(inName, 'r') as inFile, open(outName, 'w') as outFile:
        outFile.write(''.join(inFile.readlines()[1::2]))
