#Extracting java dependencies to prepare dependency graph

import csv
import os
import re


def checkImportStatement(line):
    """Checks if the given line contains a import statement and returns the java file if found else returns False"""
    expression = re.compile(r"^import (.+)\s")  # regex for import statement
    javaFile = re.search(expression, line)
    if javaFile is None:
        return False
    return javaFile[1]


def checkImportedFile(file):
    """Checks if the imported file is a java library file or user-defined
        Returns True if the file is user-defined else returns False"""
    # os.path.exists checks if the file imported is user-defined or standard library
    file_exists = os.path.exists("/java_files/" + str(javaimportedFile))
    return file_exists


def traverseJavaFile(file):
    """Traverses the given java program file and calls the checkImportStatement function to check
        import statements in the file
        Returns a list of user-defined java files imported in the program"""
    pass


def outputData(importedFiles):
    """Receives a dictionary containing filename as key and list of user-defined imported java files as values
        Writes the data into a csv file"""
    pass


def getJavaFiles():
    """This function returns list of names of all the java files present in the 'java_files' folder"""
    pass

if __name__ == '__main__':
    javaFiles = getJavaFiles()
    data = {} #containing filename as key and list of user-defined imported java files as values

    for i in javaFiles:
        data[i] = traverseJavaFile(i)

    outputData(data)