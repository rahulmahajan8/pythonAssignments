def main():
    try:
        fobj = open("demo.txt","r")
        print("file gets opened")

        with open("demo.txt","r") as file:
            lines=file.readlines()

        print("total number of lines in demo.txt:",len(lines))
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__ == "__main__":
    main()