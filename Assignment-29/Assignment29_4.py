import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py <file1> <file2>")
    exit()

try:
    with open(sys.argv[1], "r") as f1:
        data1 = f1.read()

    with open(sys.argv[2], "r") as f2:
        data2 = f2.read()

    if data1 == data2:
        print("Success")
    else:
        print("Failure")

except FileNotFoundError:
    print("File not found.")


if __name__ == "__main__":
    main()