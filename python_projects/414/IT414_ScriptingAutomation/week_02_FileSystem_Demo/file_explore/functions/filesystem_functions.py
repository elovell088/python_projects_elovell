
#
import os
import platform
import shutil


def drawMenu():
    print("What would you like to do?")
    print("To show all files, enter 'S'")
    print("To create a new folder, enter 'N'")
    print("To copy a file, enter 'C'")


def showFiles():
    my_path = getPath()
    os.chdir(my_path)
    print("Printing the contents of " + os.getcwd())
    
    file_list = os.listdir(my_path)

    for file_item in file_list:
        if os.path.isfile(os.path.join(my_path, file_item)):

            temp_file_size = os.path.getsize(os.path.join(my_path, file_item))
            temp_file_divide = temp_file_size / 1000000

            if temp_file_divide < 1:
                print(file_item + "|" + str(temp_file_size) + " Bytes")
            else:
                print(file_item + "|" + str(temp_file_divide) + " Megabytes")

        else:
            print(file_item + " | " + "folder")



def copyFile():
    my_path = getPath()

    file_to_copy = input("What is the name of the file you would like to copy?")
    folder_to_copy_to  = input("What is the name of the folder you would like to copy to?")
    shutil.copy2(file_to_copy, folder_to_copy_to)

    shutil.copy2(file_to_copy, folder_to_copy_to)


def createFolder():
    my_path = getPath()

    new_folder = input("What is the name of the folder you would like to create?")
    os.makedirs(os.path.join(my_path, new_folder))



def getPath():
    my_system = platform.system()
    
    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/Users/ericlovell/"

    final_filepath = os.path.join(root_fs, "file_explore")
    print(final_filepath)
    return final_filepath

