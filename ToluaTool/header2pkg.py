import os
import sys

#tolua++Path = "~/tolua++/bin/tolua++"

def ConverHeader2PKG(filePath,fileOutName):
    outputLines = list()
    fileContent = file(filePath)
    fileLines = fileContent.readlines()
    exporting = True
    for curLine in fileLines:
        curLine = curLine.strip()
        if curLine.find("#include") != -1:
            outputLines.append("$"+curLine+os.linesep)
        elif curLine.find("#ifndef") != -1 or curLine.find("#define") != -1 or curLine.find("#end") != -1:
            continue
        elif curLine.find("public:") != -1:
            exporting = True
            continue
        elif curLine.find("protected:") != -1:
            exporting = False
            continue
        elif curLine.find("//") == 0:
            continue
        elif curLine.find("CC_SYNTHESIZE") != -1 and exporting == True:
            curLine = curLine.replace('CC_SYNTHESIZE','').replace('(','').replace(')','').replace(';','');
            sline = curLine.split(',')
            valueType = sline[0].strip()
            functionName = sline[2].strip()
            setter = "void set"+functionName+"("+valueType+" var);"
            getter = valueType+" get"+functionName+"();"
            outputLines.append(setter+os.linesep)
            outputLines.append(getter+os.linesep)
        elif curLine.find("CC_PROPERTY") != -1 and exporting == True:
            curLine = curLine.replace('CC_PROPERTY','').replace('(','').replace(')','').replace(';','');
            sline = curLine.split(',')
            valueType = sline[0].strip()
            functionName = sline[2].strip()
            setter = "void set"+functionName+"("+valueType+" var);"
            getter = valueType+" get"+functionName+"();"
            outputLines.append(setter+os.linesep)
            outputLines.append(getter+os.linesep)
        elif curLine.find("};") != -1:
            outputLines.append(curLine+os.linesep)
        elif exporting == True:
            outputLines.append(curLine+os.linesep)
    outputFile = file(fileOutName,'w')
    outputFile.writelines(outputLines);
    outputFile.flush()
    outputFile.close()

def ConverToOutputFileName(inputFileName):
    return replace(inputFileName, ".h", "Lua.pkg")

#pre_path = "/Users/glu/SS2_lab/LBT/goal/"
#targetFilePath = sys.argv[1]
#outputFilePath = sys.argv[2]

#f:single file
#fd:all header files in folder
#fl:file list
#setprepath:set the pre path for global config
paramType = sys.argv[1]
param = sys.argv[2]
per_path = ""

if paramType == "setperpath":
    pre_path = param
if paramType == "f":
    outputFileName = ConverToOutputFileName(param)
    ConverHeader2PKG(pre_path + param, pre_path + outputFileName)
elif paramType == "fd":
    for root, dirs, files in os.walk(param):
        print 'Processing Data in Folder',root
        for name in files:
            if name.find('.h') != -1:
                print '    Processing File',name
                outputFileName = ConverToOutputFileName(name)
                ConverHeader2PKG(per_path + param, pre_path + outputFileName)
elif paramType == "fl":
ConverHeader2PKG(pre_path + targetFilePath,pre_path + outputFilePath)
            

