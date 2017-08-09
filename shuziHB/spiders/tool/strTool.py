from shuziHB.spiders.tool.fileHandle import readFile
import hashlib

def isEqual(fileName=str,src=str):
    lines = readFile(fileName)
    for line in lines:
        if line == src:
            return True
    return False

def strMd5(src = str):
    md5 = hashlib.md5()
    md5.update(src)
    return md5.hexdigest()
