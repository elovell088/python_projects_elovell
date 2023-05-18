#IT 414 - Eric Lovell - Main 
from functions.file_organization_functions import *

script_path = findScript()
copyScript(script_path)
extractZipFile()
processLogs()
createZip('C:\\logs')
