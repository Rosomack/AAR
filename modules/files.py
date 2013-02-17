#!/usr/bin/python

import glob, os, mmap

def findInFiles(fileName):
    """ returns bool if string found in file """
    file = open(fileName)
    fileString = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS.READ)

def replaceInFile(filename, searchstring, replacestring):
    """ replaces the searchstring with the replacestring in given filename """
    thefile = open(filename)
    try:
        filecontent = thefile.read()
        filecontent = filecontent.replace(searchstring, replacestring)
    finally:
        thefile.close()

def fileListOfExtensionsInPath(extension, rootPath):
    """ returns list of files inc full path that have a specified extension
    parameters: 
        extension:string of file extension
        rootPath:the start path to search. the search is recursive through sub directories """
    fileList = []
    for dirPath, dnames, fnames in os.walk(rootPath):
        for f in fnames:
            if f.endswith(extension):
                fileList.append(os.path.join(dirPath, f))
    return fileList


def main():
    """ testing above methods """
    fileList = fileListOfExtensionsInPath("png", "/home/aurel/code/NGA-iOS/")
    print fileList

if __name__ == '__main__':
    main()
