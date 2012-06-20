import os
import sys

#tolua++Path = "~/tolua++/bin/tolua++"

def ConverHeader2PKG(filePath,fileOutName):
    outputLines = list()
    fileContent = file(filePath)
    fileLines = fileContent.readlines()
    for curLine in fileLines:
        curLine = curLine.strip()
        if curLine.find("#include") != -1:
            outputLines.append("$"+curLine+os.linesep)
        elif curLine.find("#ifndef") != -1 or curLine.find("#define") != -1 or curLine.find("#end") != -1:
            continue
        elif curLine.find("public:") != -1 or curLine.find("protected:") != -1:
            continue
        elif curLine.find("//") != -1:
            continue
        elif curLine.find("CC_SYNTHESIZE") != -1:
            curLine = curLine.replace('CC_SYNTHESIZE','').replace('(','').replace(')','').replace(';','');
            sline = curLine.split(',')
            valueType = sline[0].strip()
            functionName = sline[2].strip()
            setter = "void set"+functionName+"("+valueType+" var);"
            getter = valueType+" get"+functionName+"();"
            outputLines.append(setter+os.linesep)
            outputLines.append(getter+os.linesep)
        elif curLine.find("CC_PROPERTY") != -1:
            curLine = curLine.replace('CC_PROPERTY','').replace('(','').replace(')','').replace(';','');
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

pre_path = "/Users/glu/SS2_lab/LBT/goal/"
targetFilePath = sys.argv[1]
outputFilePath = sys.argv[2]
ConverHeader2PKG(pre_path + targetFilePath,pre_path + outputFilePath)
            

