import os

folders = input("please provide lsit of folders names with spaces in betwee :").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name, looks like this folder does not exist" + folder)
        break
    except PermissionError:
        break

    print(" ==== listing fies for the folder - " + folder)

    for file in files:
        print(file)



 