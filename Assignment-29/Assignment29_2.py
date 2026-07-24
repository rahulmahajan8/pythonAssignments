def main():

    filename = input("demo.txt: ")

    try:
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()