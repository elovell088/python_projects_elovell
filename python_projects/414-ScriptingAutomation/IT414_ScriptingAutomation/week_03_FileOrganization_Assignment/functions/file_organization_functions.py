#IT 414 - Eric Lovell - File Organization Functions
from regex.regex_functions import *
from pathlib import Path
import os
import platform
import shutil
import send2trash
import zipfile




def showFiles():
    """"""
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
    """"""
    file_to_copy = input("What is the name of the file you would like to copy?")
    folder_to_copy_to  = input("What is the name of the folder you would like to copy to?")

    shutil.copy2(file_to_copy, folder_to_copy_to)


def createFolder():
    """"""
    my_path = getPath()

    new_folder = input("What is the name of the folder you would like to create?")
    os.makedirs(os.path.join(my_path, new_folder))



def copyScript(script_path):
    """"""
    root_path = getRoot()
    destination_path = "/log_processing"

    final_destination_path = os.path.join(root_path, destination_path)
    
    shutil.copytree(script_path, final_destination_path)



def extractZipFile():
    """"""
    root_path = getRoot()
    source_path = 'log_processing/text_files/access_logs.zip'
    final_source_path = os.path.join(root_path, source_path)

    file_path = "/logs"
    final_destination_path = os.path.join(root_path, file_path)

    extract_zip = zipfile.ZipFile(final_source_path)
    extract_zip.extractall(final_destination_path)
    extract_zip.close()



def createZip():
    """"""
    root_path = getRoot()
    folder_name = 'logs'
    source_file_path = os.path.join(root_path, folder_name)
    result_zip_file = zipfile.ZipFile('week_03_FileOrganization_Assignment/text_files/results.zip', 'w')

    walk_return = os.walk(source_file_path)
    for folder, subfolder, filenames in walk_return:
        result_zip_file.write(folder)
        for filename in filenames:
            result_zip_file.write(os.path.join(folder, filename))
    result_zip_file.close()



def findScript():
    """Walks from the root of the system and identifies the location of the script file"""

    print("Preparing script...")
    start_path = getRoot()

    script_found = False
    my_return = os.walk(start_path)
    for item in my_return:
        if script_found:
            break
        else:
            for filename in item[2]:
                if filename == 'main_week_03.py':
                    output_path = item[0]
                    print(output_path)
                    script_found = True
                    break
    
    return(output_path)



def getPath(passed_path):
    """"""
    my_system = platform.system()
    
    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs, passed_path)
    print(final_filepath)
    return final_filepath



def getRoot():
    """"""
    my_system = platform.system()
    
    if my_system == "Windows":
        root_fs = "C:\\"
    else:
        root_fs = "/"

    final_filepath = os.path.join(root_fs)
    
    return final_filepath



def deleteFile():
    """"""
    my_path = getPath()

    file_to_delete = input("What is the name of the file\\folder you would like to move delete?")

    send2trash.send2trash(os.path.joine(my_path + file_to_delete), os.path.join(my_path, file_to_delete))



def moveFile():
    """"""
    my_path = getPath()
    my_root = getRoot()

    file_to_move = input("What is the name of the file you would like to move?")
    folder_to_move_to  = input("What is the name of the folder you would like to move to?")

    shutil.copy2(os.path.join(my_path + file_to_move), os.path.join(my_root, folder_to_move_to))



def renameFile(original_file_name_path, new_name_file_path):
    """"""
    shutil.move(original_file_name_path, new_name_file_path)



def writeToLog(passed_string, passed_destination_path):
    """Function that creates a log file
    Arguments:
        passed_string {String Value} -- String value that consists of the string to write to the log file
        passed_destination_path {String Value} -- String value that consists of the file path to the destination
        
    Returns:
        None -- Creates file called log.txt and places it in the file system"""
    
    #Change directory to destination
    os.chdir(passed_destination_path)
    log_file = 'matches.txt'
    
    if not os.path.isfile(os.path.join(passed_destination_path, log_file)):
        try:
            with open(log_file, "w") as text_file:
                text_file.write(passed_string)  
        except:
            pass
    else:
        with open(log_file, "a") as text_file:
                text_file.write(passed_string)



def processLogs():
    """"""
    log_root_path = getRoot()
    log_file_name = 'logs'
    write_log_path = log_root_path + log_file_name

    path = getRoot()
    other = 'logs\\access_logs'
    start_path = os.path.join(path, other)

    os.chdir(start_path)
    walk_return = os.walk(start_path)

    bad_ip_list = []

    for item in walk_return:
        for line in item[2]:
            dir_path = str(item[0])
            file_name = str(item[2][0])
            new_file_name = "processed_" + file_name
            new_path = os.path.join(dir_path, new_file_name)
            
            path = os.path.join(dir_path, file_name)

            matches_found = False
            with open(path) as log_file:
                for line in log_file:
                    containsInstall = searchForInstall(line)
                    constainsLoginPhp = searchForLoginPhp(line)
                    constainsSelect = searchForSelect(line)
                    containsRelativeRoot = searchForRelativeRoot(line)
                    containsHttpStatus = searchforHttpStatus(line)

                    temp_line = line.split()

                    if temp_line[0] in bad_ip_list:
                        pass
                    else:
                        if containsHttpStatus:
                            matches_found = True
                            bad_ip_list.append(temp_line[0])
                            log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                            writeToLog(log_string, write_log_path)

                        elif containsInstall:
                            matches_found = True
                            bad_ip_list.append(temp_line[0])
                            log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                            writeToLog(log_string, write_log_path)

                        elif constainsLoginPhp:
                            matches_found = True
                            bad_ip_list.append(temp_line[0])
                            log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                            writeToLog(log_string, write_log_path)

                        elif constainsSelect:
                            matches_found = True
                            bad_ip_list.append(temp_line[0])
                            log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                            writeToLog(log_string, write_log_path)

                        elif containsRelativeRoot:
                            matches_found = True
                            bad_ip_list.append(temp_line[0])
                            log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                            writeToLog(log_string, write_log_path)
                
            if matches_found:
                renameFile(path, new_path)
            else:
                send2trash.send2trash(dir_path)