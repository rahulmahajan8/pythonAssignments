import os

def DeleteDuplicates(Duplicate):

    count = 0

    for value in Duplicate.values():

        if len(value) > 1:

            for file in value[1:]:
                os.remove(file)
                count += 1

    return count