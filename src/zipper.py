from zipfile import ZipFile
import os
from os.path import basename


def zip():
    dirName = ["in", "out"]
    with ZipFile("tests.zip", 'w') as zipObj:
        for dirs in dirName:
            for folderName, subfolders, filenames in os.walk(dirs):
                for filename in filenames:
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath)
