def main():
    try:
        fobj = open("demo.txt","r")
        print("file gets opened")

        word = input("enter word to search")

        with open("demo.txt","r") as file:
            data=file.read()

        if word in data:
            print(word,"found in file.")

        else:
            print(word,"not found in file.")
    
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__ == "__main__":
    main()