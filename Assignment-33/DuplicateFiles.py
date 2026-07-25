import os

def FindDuplicate(Marvellos):

    Duplicate = {}

    for FolderName, SubFolder, FileNames in os.walk(Marvellos):

        for File in FileNames:

            path = os.path.join(FolderName, File)

            checksum = (path)

            if checksum in Duplicate:
                Duplicate[checksum].append(path)
            else:
                Duplicate[checksum] = [path]

    return Duplicate