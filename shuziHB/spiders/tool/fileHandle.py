# -*- coding: utf-8 -*-
def readFile(fileName):

    file_obj = open("./file/"+fileName,'r')
    try:
        all_text = file_obj.readlines()
    finally:
        file_obj.close()
    file_obj.close()
    text = []
    for line in all_text:
        text.append(line.replace("\n",""))
    return text

def writeFile(fileName,content):
    output = open("./file/"+fileName,'a+')
    output.write(content+"\n")
    output.close()

def fileTruncate(fileName=str):
    file = open("./file/"+fileName,'r+')
    file.truncate()
    file.close()
