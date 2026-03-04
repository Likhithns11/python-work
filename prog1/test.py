import os
folders = input("enter the folder names: ").split()
for folder in folders:
    files = os.listdir(folder)
    print("=====file in folder "+(folder))
    for file in files:
        print(file)