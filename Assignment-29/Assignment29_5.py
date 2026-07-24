def main():
    filename = input("demo.txt: ")
    word = input("Marvellous: ")

    try:
        with open(filename, "r") as f:
            data = f.read()

        count = data.count(word)
        print(f'"{word}" appears', count, "times.")

    except FileNotFoundError:
        print("File not found.")


if __name__ == "__main__":
    main()