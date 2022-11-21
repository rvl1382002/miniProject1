import csv
import os
import re


def checkImportStatement(line):
    """Checks if the given line contains a import statement and returns a boolean value"""
    expression = re.compile(r"^import (.+)\s")  # regex for import statement
    javaFile = re.search(expression, line)
    if javaFile is None:
        return False
    return javaFile[1]


if __name__ == '__main__':
    print(checkImportStatement("import google.acsm "))
    
