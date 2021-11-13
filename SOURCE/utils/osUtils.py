from os import listdir
import pathlib
from os.path import isfile, join


def getRootDir():
    currentDir = pathlib.Path().resolve()
    rootDir = str(currentDir).split('SOURCE')[0]
    return rootDir


def getFilesInDir(dir):
    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    return files
