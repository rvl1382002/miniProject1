#Extracting java dependencies to prepare dependency graph

import csv
import os
import re


def checkImportStatement(line):
    """Checks if the given line contains a import statement and returns the java file if found else returns False"""
    expression = re.compile(r"import (\S+)\s")  # regex for import statement
    javaFile = re.search(expression, line)
    if javaFile is None:
        return False
    return javaFile[1]


def checkImportedFile(file):
    """Checks if the imported file is a java library file or user-defined
        Returns True if the file is user-defined else returns False"""
    # os.path.exists checks if the file imported is user-defined or standard library
    file_exists = os.path.exists("java_files/" + file.strip()+".java")
    return file_exists


def traverseJavaFile(javaFile):
    """Traverses the given java program file and calls the checkImportStatement function to check
        import statements in the file
        Returns a list of user-defined java files imported in the program"""
    dependencies = []
    with open(javaFile,"r") as file:
        lines = file.readlines()
        for line in lines:
            javaDependency = checkImportStatement(line)
            if javaDependency:
                isUdfDependency = checkImportedFile(javaDependency)
                # Checking if the dependency is user defined
                if isUdfDependency:
                    dependencies.append(javaDependency)
    return dependencies


def processData(data):
    """Receives the data in dictionary format and returns it in a format so that it can be written into csv file"""
    processedData = []
    for i in data:
        allFiles = dict(zip(data.keys(), [False] * len(data)))
        allFiles["Dependency"] = i
        for j in data[i]:
            allFiles[j] = True
            # processedData.append()
            # processedData[rowCount][i] = True
        processedData.append(allFiles)
    return processedData



def outputData(importedFiles):
    """Receives a dictionary containing filename as key and list of user-defined imported java files as values
        Writes the data into a csv file"""
    processedData = processData(data)
    #importedFiles = {file1:[file2,file3,file4],file2:[file3,file4]}
    with open("java_dependencies.csv","w") as csvFile:
        head=list(importedFiles.keys())
        head.insert(0,"Dependency")
        csvWriter = csv.DictWriter(csvFile,fieldnames=head)
        csvWriter.writeheader()
        csvWriter.writerows(processedData)




def getJavaFiles():
    #Riddhish
    """This function returns list of names of all the java files present in the 'java_files' directory"""
    javaFiles=[]
    pathToJavaFiles = 'java_files'
    allFiles = os.listdir(pathToJavaFiles)
    for i in allFiles:
        if i.endswith(".java"):
            javaFiles.append(i)
    return javaFiles

if __name__ == '__main__':
    javaFiles = getJavaFiles()
    data = {} #containing filename as key and list of user-defined imported java files as values
    for file in javaFiles:
        data[file[:-5]] = traverseJavaFile("java_files/"+file)
    outputData(data)