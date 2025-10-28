from pathlib import Path
import os

def readFileAndFolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i + 1} : {items}")

def createFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of your file :")
        p = Path(name)
        if not p.exists():
            with open (p,'w')as fs:
                data = input("What you have to write in this file :")
                fs.write(data)
            print("File has been created successfully!")
        else:
            print("The file already exists")
    except Exception as err:
        print(f"The error occured as {err}")                

def readFile():
    try:
        readFileAndFolder()
        name = input("Which file you want to read : ")
        p = Path(name)
        if p.exists and p.is_file:
            with open(p,'r') as fs:
                data = fs.read()
                print(data)

            print("Readed Successfully!")

        else:
            print("File doesnot exists")        

    except Exception as err:
        print(f"The eror occured as {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("Enter the name of your file you want to update : ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for updating the name of your file : ")
            print("Press 2 for overwriting the content in your file : ")
            print("press 3 for appending the content in your file : ")

            res = int(input("Enter your response : "))

            if res == 1:
                name2 = input("Enter the name to update your file name : ")
                p2 = Path(name2)
                p.rename(p2)
            if res == 2:
                with open(p,'w') as fs:
                    data = input("Enter what you want to overwrite in your file : ")
                    fs.write(data)
            if res == 3:
                with open(p,'a') as fs:
                    data = input("Enter what you want to overwrite in your file : ")
                    fs.write(data)
        else:
            print("File doesnot exists")

    except Exception as err:
        print(f"The error occured as {err}")

def deleteFile():
    try:
        readFileAndFolder()
        name = input("Enter a file name you want to delete : ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
        else:
            print("file doesnot exists")
    except Exception as err:
        print(f"The error occured as {err}")            




print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")


check = int(input("Please tell your response :"))

if check == 1:
    createFile()
if check == 2:
    readFile()
if check == 3:
    updateFile()  
if check == 4:
    deleteFile()        



