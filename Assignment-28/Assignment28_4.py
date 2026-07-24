def main():
    try:
        fobj = open("demo.txt","r")
        print("file gets opened")

        with open("demo.txt","r") as file1:
            data = file1.read()
        
        with open("declare.txt","w") as file2:
            file2.write(data)

        print("Content copied succesfully")
        
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory")
if __name__ == "__main__":
    main()