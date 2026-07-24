import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python program.py <source_file>")
    exit()

source = sys.argv[1]
destination = "Demo.txt"

try:
    with open(source, "r") as f1:
        data = f1.read()

    with open(destination, "w") as f2:
        f2.write(data)

    print("Contents copied successfully.")
except FileNotFoundError:
    print("Source file not found.")


if __name__ == "__main__":
    main()