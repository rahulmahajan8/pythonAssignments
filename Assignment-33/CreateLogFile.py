import os
import time

def CreateLog(Duplicate, Deleted, Directory):

    if not os.path.exists("Marvellous"):
        os.mkdir("Marvellous")

    timestamp = time.ctime()
    timestamp = timestamp.replace(" ", "_")
    timestamp = timestamp.replace(":", "-")

    LogFile = "Marvellous/DuplicateRemovalLog_" + timestamp + ".log"

    with open(LogFile, "w") as f:

        f.write("Duplicate File Removal Log\n")
        f.write("-"*50 + "\n")
        f.write("Directory : " + Directory + "\n")
        f.write("Total Duplicate Groups : " + str(len(Duplicate)) + "\n")
        f.write("Files Deleted : " + str(Deleted) + "\n\n")

        for key, value in Duplicate.items():

            if len(value) > 1:
                f.write("Checksum : " + key + "\n")

                for item in value:
                    f.write(item + "\n")

                f.write("\n")

    return LogFile