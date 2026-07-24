def main():
    try:
        fobj = open("demo.txt","r")
        print("file gets opened")

        with open("demo.txt", "r") as file:
            data=file.read()

        words=data.split()
        print("total number of words in data.txt:",len(words))

        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__ == "__main__":
    main()