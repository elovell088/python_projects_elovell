from functions.file_organization_functions import *
from regex.regex_functions import *
from pathlib import Path
import shutil

#os.chdir("..\week_03_FileOrganization_Assignment")
#extractZipFile()
#copyScript()
#extractZipFile("../../../text_files/access_logs.zip")
# string = "The answer to this question is the link is /wp-login.php?action=register and I know that 4 a fact you faggot"
# pattern_exists = searchForLoginPhp(string)
# print(pattern_exists)

createZip()


#copyScript(script)
###---THIS IF CODE FOR LOG PROCESSING---###
"""
log_root_path = getRoot()
log_file_name = 'logs'
write_log_path = log_root_path + log_file_name

path = getRoot()
other = 'logs/access_logs'
start_path = os.path.join(path, other)

os.chdir(start_path)
walk_return = os.walk(start_path)

bad_ip_list = []

for item in walk_return:
    for file in item[2]:
        path = os.path.join(str(item[0]), str(item[2][0]))

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
                        
                        bad_ip_list.append(temp_line[0])
                        log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                        writeToLog(log_string, write_log_path)

                    elif containsInstall:
            
                        bad_ip_list.append(temp_line[0])
                        log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                        writeToLog(log_string, write_log_path)

                    elif constainsLoginPhp:
                        
                        bad_ip_list.append(temp_line[0])
                        log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                        writeToLog(log_string, write_log_path)

                    elif constainsSelect:
                        
                        bad_ip_list.append(temp_line[0])
                        log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                        writeToLog(log_string, write_log_path)

                    elif containsRelativeRoot:
                        
                        bad_ip_list.append(temp_line[0])
                        log_string = "IP: " + temp_line[0] + ", " + "File: " + temp_line[6] + '\n\n'
                        writeToLog(log_string, write_log_path)
"""
                        
