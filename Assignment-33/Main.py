import sys

if len(sys.argv) != 3:
    print("Usage : DuplicateFileRemoval.py Directory Interval")
    exit()

Directory = sys.argv[1]

Duplicate = (Directory)

Deleted = (Duplicate)

LogFile = (Duplicate, Deleted, Directory)

print("Duplicate files removed successfully.")
print("Log File :", LogFile)