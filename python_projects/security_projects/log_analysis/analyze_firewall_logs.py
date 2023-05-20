#Security Projects - Eric lovell - Analyzes firewall log entries and 
#Pulls functions from ../functions/log_file_functions.py 

from functions.log_file_functions import *

log_file_path = 'File path to firewall log'
parsed_logs = parse_firewall_log(log_file_path)

output_file_path = 'File path to firewall log'
write_parsed_logs_to_file(parsed_logs, output_file_path)

print(f"Parsed log entries written to: {output_file_path}")