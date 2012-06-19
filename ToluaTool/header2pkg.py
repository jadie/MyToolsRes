import os
def ConverHeader2PKG(filePath,fileOutName):
    outputLines = list()
    fileContent = file(filePath)
    fileLines = fileContent.readlines()
    for curLine in fileLines:
        curLine = curLine.strip()
        if curLine.find("#include") != -1:
            outputLines.append("$"+curLine+os.linesep)
        elif curLine.find("CC_SYNTHESIZE") != -1:
            curLine = curLine.replace('CC_SYNTHESIZE','').replace('(','').replace(')','').replace(';','');
            sline = curLine.split(',')
            valueType = sline[0].strip()
            functionName = sline[2].strip()
            setter = "void set"+functionName+"("+valueType+" var);"
            getter = valueType+" get"+functionName+"();"
            outputLines.append(setter+os.linesep)
            outputLines.append(getter+os.linesep)
        else:
            outputLines.append(curLine+os.linesep)
    outputFile = file(fileOutName,'w')
    outputFile.writelines(outputLines);
    outputFile.flush()
    outputFile.close()

ConverHeader2PKG("testHeader.h","test.pkg")
            

